# -*- coding: utf-8 -*-
"""
第 03 章：表达式 —— Python 真正"干活"的地方
============================================================

本章学什么（6 条）：
  1. 表达式 vs 语句：搞清"一定有值"和"只是一条命令"的区别。
  2. 各种字面量：数字（二进制/八进制/十六进制/科学计数/复数/超大整数）、
     字符串（三种引号、转义、原始字符串）、布尔与 None。
  3. f-string 格式化：对齐、补零、千分位、百分比、调试神器 {x=}；
     顺带对比老式的 % 和 .format()，说明为什么现在都用 f-string。
  4. 条件表达式、切片表达式、推导式（列表/字典/集合/生成器）。
  5. 常用"表达式式"内置函数、lambda 表达式。
  6. 布尔上下文（哪些值是"假值"）、短路求值与副作用、常见坑汇总。

怎么运行：
  用 VS Code 打开本文件，点右上角 ▶ 运行，或按 Ctrl+F5；也可以在终端执行
  python 03_expressions.py。各节互相独立，可以选中一节单独运行。

会看到什么：
  终端里一段一段打印"某某 = 某某"，每节用 ===== 或 ----- 分隔。
  程序自己跑完就结束，不会卡住、不需要你输入任何东西。
"""

# ============================================================
# 1. 表达式 vs 语句：表达式一定有值
# ============================================================
# 表达式（expression）算完一定"产生一个值"，如 3 + 4、x > 1、len("abc")；
# 语句（statement）只是"做一件事"，如赋值 / import / if / for，本身没有值。
# 一句话记法：表达式能塞进 print() 当参数，语句塞不进去。
print("\n" + "=" * 60)
print("1. 表达式 vs 语句")
print("=" * 60)
print("type(3 + 4) =", type(3 + 4))    # <class 'int'>，说明 3+4 的值就是 7
print("type(3 > 1) =", type(3 > 1))    # <class 'bool'>，比较也是表达式
print("len('abc')  =", len("abc"))      # 函数调用同样是表达式
# ⚠️ 坑：x = 1 是语句不是表达式，所以写成 print(x = 1) 会直接 SyntaxError。

# ============================================================
# 2. 字面量表达式：数字、字符串、布尔、None
# ============================================================
print("\n" + "=" * 60)
print("2. 字面量表达式")
print("=" * 60)
big_pretty = 1_000_000      # 下划线只是给人看的分隔符，Python 计算时忽略它
binary = 0b1010             # 0b = 二进制，值是 10
octal = 0o17                # 0o = 八进制，值是 15
hex_num = 0xFF              # 0x = 十六进制，值是 255
sci = 1.5e3                 # 科学计数法 = 1.5 × 10³ = 1500.0
complex_num = 1 + 2j        # 复数，j 表示虚部
huge = 2 ** 100             # Python 整数无上限，自动升级为"大整数"
print(f"1_000_000 = {big_pretty}")
print(f"0b1010 = {binary}, 0o17 = {octal}, 0xFF = {hex_num}")
print(f"1.5e3 = {sci}（注意它变成了 {type(sci)}）")
print(f"1+2j = {complex_num}，实部 = {complex_num.real}")
print(f"2 ** 100 = {huge}，共 {len(str(huge))} 位数字")
# ⚠️ 坑1：0o17 里的 o 是字母 o（octal）；写成 017 在 Python3 里是语法错误。
# ⚠️ 坑2：下划线不能放开头、结尾或紧挨小数点：_100 / 100_ / 1._5 都非法。
# ⚠️ 坑3：0.1 + 0.2 != 0.3（浮点二进制精度问题），比大小要用 math.isclose。

single, double = '单引号', "双引号"          # 单双引号完全等价
triple = """三引号可以
跨越多行，
还保留换行符"""
escaped = "第一行\n第二行\t制表符\\反斜杠\'撇号"   # \n 换行 \t 制表 \\ 反斜杠
raw = r"C:\new\test"        # r 开头 = 原始字符串，\n \t 不再被转义
print(f"单引号 = {single}，双引号 = {double}")
print(f"三引号 = {triple!r}")              # !r 显示原样，能看见 \n
print(f"escaped = {escaped!r}")
# 重点：r"" 与普通串的"实际字符长度"不同，这正是 Windows 路径的经典坑！
normal_path = "C:\new\test"      # \n 变成换行、\t 变成制表符，各占 1 个字符
print(f"r 版本  len = {len(raw)}  → {raw}")
print(f"普通版本 len = {len(normal_path)}  → {normal_path!r}")
# ⚠️ 坑：Windows 路径 "C:\new\test" 里的 \n \t 会被当转义符，路径就毁了。
#        写法二选一：原始字符串 r"C:\new\test"，或反斜杠双写 "C:\\new\\test"。

is_ready, nothing = True, None   # 注意 True 首字母大写；true / FALSE 都是错的
print(f"True = {is_ready}，None = {nothing}，type(None) = {type(None)}")
print(f"None is None → {nothing is None}")     # 判空要用 is，不要用 ==
print(f"bool 其实是 int 的子类：True + True = {True + True}")
# ⚠️ 坑：函数忘写 return 时结果就是 None，对 None 做运算会抛 TypeError。

# ============================================================
# 3. f-string 格式化：把值漂亮地塞进字符串
# ============================================================
print("\n" + "=" * 60)
print("3. f-string 格式化")
print("=" * 60)
name, score, count, ratio = "小明", 93.4567, 1234567, 0.2375
width, prec = 8, 2           # 这两个变量会被"嵌套"进格式说明里
d = {"k": "字典的值"}
print(f"基本插值      : {name} 考了 {score} 分")
print(f"!r 显示原样   : {name!r}")
print(f"保留两位 .2f  : {score:.2f}")
print(f"右对齐 :>10   : [{name:>10}]")
print(f"左对齐 :<10   : [{name:<10}]")
print(f"居中   :^10   : [{name:^10}]")
print(f"补零   :08.2f : {score:08.2f}")
print(f"千分位 :,     : {count:,}")
print(f"百分比 :.1%   : {ratio:.1%}")
print(f"带符号 :+d    : {42:+d} / {-42:+d}")
print(f"调试神器 x=   : {score=}")               # 直接打印"变量名=值"
print(f"字典取值      : {d['k']}")
print(f"表达式调函数  : {len(name) * 10}")
print(f"对齐嵌套变量  : [{score:>{width}.{prec}f}]")
print(f"格式化后 price = {score:.2f}")           # 节末关键结果
# ⚠️ 坑：Python 3.10 / 3.11 里 f-string 内外不能用同一种引号！
#     f"{d["k"]}"   ← 3.12 之前直接 SyntaxError
#     f"{d['k']}"   ← 内外引号换着写，3.10 起合法（本文件就是这么写的）

# ============================================================
# 4. 老式格式化对比：% 与 .format()，为什么推荐 f-string
# ============================================================
print("\n" + "=" * 60)
print("4. 老式格式化对比")
print("=" * 60)
print("百分号写法   : %s 考了 %.2f 分" % (name, score))        # 参数顺序要对上
print("format 写法  : {} 考了 {:.2f} 分".format(name, score))  # 可写索引 {1} {0}
print(f"f-string 写法: {name} 考了 {score:.2f} 分")            # 变量就近可见
print("提示：想输出一个百分号要用两个百分号连着写，否则会被当成占位符。")
# 推荐 f-string 的三个理由：
#   1) 可读性：变量名直接写在位置上，不用回头数 %s 是第几个参数。
#   2) 不易错位：% 方式参数顺序写错不报错，会静默输出错误内容。
#   3) 性能：f-string 在编译期就拼好，通常比 % 和 .format() 更快。
# ⚠️ 坑：'%d' % "abc" 类型不匹配会抛 TypeError，f-string 会自动调用 str()。


# ============================================================
# 5. 条件表达式：a if cond else b
# ============================================================
print("\n" + "=" * 60)
print("5. 条件表达式")
print("=" * 60)
age = 20
label = "成年" if age >= 18 else "未成年"      # 先判条件，再选一个分支当结果
print(f"age = {age} → {label}")
x = -3
sign = "正" if x > 0 else ("零" if x == 0 else "负")   # 嵌套：像 else if
print(f"x = {x} → {sign}")

def grade(s):
    return "及格" if s >= 60 else "不及格"      # 直接用在函数返回里

print(f"grade(59) = {grade(59)}，grade(60) = {grade(60)}")
nums = [1, 2, 3, 4, 5]
kinds = ["偶" if n % 2 == 0 else "奇" for n in nums]   # 也能用在推导式里
print(f"{nums} 的奇偶 → {kinds}")
# ⚠️ 坑：a if cond else b 整体是一个"表达式"，所以反过来写成
#     "成年" if age >= 18 else "未成年" = label 是语法错误。
#     嵌套超过两层就改回 if / elif / else 语句，可读性优先。


# ============================================================
# 6. 切片表达式：s[start:stop:step]
# ============================================================
print("\n" + "=" * 60)
print("6. 切片表达式")
print("=" * 60)
s = "PYTHON"
print(f"原串       : {s}")
print(f"[1:4]      : {s[1:4]}     ← 左闭右开：含 1 不含 4")
print(f"[:3]       : {s[:3]}      ← 省略 start 默认从头开始")
print(f"[3:]       : {s[3:]}      ← 省略 stop 默认到结尾")
print(f"[-3:]      : {s[-3:]}     ← 负数索引从右数，-1 是最后一个")
print(f"[::-1]     : {s[::-1]}     ← step=-1 实现反转，常用技巧")
print(f"[::2]      : {s[::2]}     ← 每隔一个取，即下标 0,2,4")
print(f"[1::2]     : {s[1::2]}")
print(f"[100:200]  : {s[100:200]!r}  ← 越界不报错，返回空串")
lst, tup = [10, 20, 30, 40, 50], (1, 2, 3, 4, 5)
print(f"list[1:4]  : {lst[1:4]}     ← 切片对 list / tuple / str 通用")
print(f"tuple[::-1]: {tup[::-1]}")
# ⚠️ 坑1：切片越界"不报错"（返回空或自动截断），所以写错下标它不会提醒你。
# ⚠️ 坑2：切片返回新对象，改切片不影响原串；但它不复制里层的嵌套元素。


# ============================================================
# 7. 推导式：列表 / 字典 / 集合 / 生成器
# ============================================================
print("\n" + "=" * 60)
print("7. 推导式")
print("=" * 60)
doubled = [n * 2 for n in range(5)]                   # 把"循环 + append"压缩
squares = [n * n for n in range(1, 6) if n % 2 == 1]  # 带 if 过滤
pairs = [(a, b) for a in range(2) for b in "xy"]      # 多重 for = 嵌套循环
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [v for row in matrix for v in row]             # 嵌套推导式：二维展平
print(f"n*2            : {doubled}")
print(f"奇数平方 (if)  : {squares}")
print(f"多重 for       : {pairs}")
print(f"二维展平       : {flat}")
word = "banana"
counts = {ch: word.count(ch) for ch in sorted(set(word))}   # 字典推导式 {k: v}
print(f"字符计数(字典) : {counts}")
uniq_len = {len(w) for w in ["a", "bb", "cc", "ddd"]}        # 集合推导式，自动去重
print(f"长度集合       : {sorted(uniq_len)}")
gen = (n * n for n in range(10))       # 生成器表达式：圆括号，惰性求值
print(f"gen 类型 = {type(gen)}，next() 第一个 = {next(gen)}")
print(f"再取一个 next() = {next(gen)}")    # 用到才算，不一次性算完
# ⚠️ 坑：生成器只能遍历一次，走完就"空了"（不报错，很迷惑）：
gen2 = (n for n in range(3))
print(f"先 sum = {sum(gen2)}，再 list = {list(gen2)}   ← 第二次就空了")
# ⚠️ 坑：Python 3 里推导式的循环变量"不会泄漏"到外面（Python 2 会）：
items = [i for i in range(3)]
try:
    print(f"推导式外访问 i = {i}")
except NameError:
    print("推导式外访问 i → NameError（好事，说明变量没泄漏）")


# ============================================================
# 8. 常用"表达式式"内置函数（都返回一个值，能当表达式用）
# ============================================================
print("\n" + "=" * 60)
print("8. 常用内置函数")
print("=" * 60)
data = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"len    长度          : {len(data)}")
print(f"sum    求和          : {sum(data)}")
print(f"max / min            : {max(data)} / {min(data)}")
print(f"sorted 默认升序      : {sorted(data)}")
print(f"sorted reverse=True  : {sorted(data, reverse=True)}")
print(f"sorted key=len       : {sorted(['ccc', 'a', 'bb'], key=len)}")
print(f"abs    绝对值        : {abs(-7)}")
print(f"round  保留 2 位     : {round(3.14159, 2)}")
print(f"zip    拉链配对      : {list(zip('abc', [1, 2, 3]))}")
print(f"enumerate 带下标     : {list(enumerate('ab', start=1))}")
print(f"map    逐个转换      : {list(map(str, [1, 2, 3]))}")
print(f"filter 过滤          : {list(filter(lambda n: n > 3, data))}")
print(f"any    有一个真就行  : {any([0, '', 3])}")
print(f"all    全部为真才行  : {all([1, 'x', 0])}")
print(f"reversed 反序迭代器  : {list(reversed(data))}")
print(f"isinstance 类型判断  : {isinstance(3, int)} / {isinstance('a', (int, str))}")
# ⚠️ 坑：zip / map / filter / reversed 返回迭代器而不是列表，直接 print 会看到
#     <zip object ...>，要用 list() 包一下才看得到内容。
# ⚠️ 坑：sorted() 返回新列表；而 list.sort() 原地修改并返回 None。


# ============================================================
# 9. lambda 表达式：一个"没有名字的小函数"
# ============================================================
print("\n" + "=" * 60)
print("9. lambda 表达式")
print("=" * 60)
add = lambda a, b: a + b          # 语法：lambda 参数: 表达式
print(f"(lambda a, b: a + b)(3, 4) = {add(3, 4)}")
students = [("小明", 88), ("小红", 95), ("小刚", 72)]
print(f"按分数降序 : {sorted(students, key=lambda st: st[1], reverse=True)}")
words = ["bb", "a", "ccc"]
print(f"map 大写   : {list(map(lambda w: w.upper(), words))}")
print(f"filter 长度>1 : {list(filter(lambda w: len(w) > 1, words))}")
# ⚠️ 坑：lambda 冒号后面只能写"一个表达式"，写语句会语法错误：
#     lambda x: print(x); x + 1   ← SyntaxError
#     逻辑超过一行、要赋值或要循环时，请老老实实写 def。
# ⚠️ 坑：lambda 里的外部变量是"运行时才查"，在循环里创建 lambda 要用默认参数固定值。


# ============================================================
# 10. 布尔上下文与真值测试：哪些是"假值"
# ============================================================
print("\n" + "=" * 60)
print("10. 布尔上下文与真值测试")
print("=" * 60)
for v in [0, 0.0, 0j, "", [], (), {}, set(), None, range(0)]:
    print(f"bool({v!r:>10}) = {bool(v)}")     # 这些都是"假值"
print(f"bool(' ')= {bool(' ')}    ← 只有一个空格的串是 True，容易翻车")
print(f"bool([0])= {bool([0])}    ← 列表里装着 0，但列表非空，所以是 True")
print(f"bool(-1) = {bool(-1)}     ← 负数也是 True")

class Box:
    def __init__(self, size):
        self.size = size
    def __bool__(self):
        return self.size > 0       # 自定义对象：空盒子为假

print(f"bool(Box(3)) = {bool(Box(3))}，bool(Box(0)) = {bool(Box(0))}")
# ⚠️ 坑：' '（空格串）、[0]、"0" 都是 True，别以为"看起来空"就是 False。
# ⚠️ 坑：判断有没有值写 if x:，别写 if x == True:（后者对 1 也成立，语义不同）。


# ============================================================
# 11. 求值顺序与副作用：短路求值时右边根本不执行
# ============================================================
print("\n" + "=" * 60)
print("11. 求值顺序与短路求值")
print("=" * 60)
log = []                            # 用一个"会记账"的函数证明谁真的被求值了
def marked(tag, value):
    log.append(tag)                 # 被调用就记账
    return value

log.clear()
r1 = marked("左", False) and marked("右", True)
print(f"False and ... → {r1}，实际求值过：{log}   ← 右边没执行！")
log.clear()
r2 = marked("左", True) or marked("右", "不该出现")
print(f"True or ...   → {r2}，实际求值过：{log}   ← 右边也没执行！")
user_input = ""                              # 用户没填，可能是空串
nickname = user_input or "匿名用户"           # 空串是假值，于是取右边的默认值
print(f"'{user_input}' or '匿名用户' → {nickname}")
# ⚠️ 坑：短路会让右边表达式的"副作用"消失。若右边是 save() 这类有副作用的调用，
#        条件不满足时它不会执行——有时是好事，有时正是 bug 的来源。
# ⚠️ 坑：and / or 返回的是"操作数本身"，不是 True / False！
print(f"3 and 5 = {3 and 5}，0 or 'x' = {0 or 'x'!r}   ← 返回原值，不是 bool")


# ============================================================
# 12. 常见坑汇总
# ============================================================
print("\n" + "=" * 60)
print("12. 常见坑汇总")
print("=" * 60)
# 坑 A：a = b = [] 时两个名字指向同一个列表，改一个另一个也变
a = b = []
a.append(1)
print(f"a = b = [] 再 a.append(1) → a = {a}, b = {b}   ← 是同一个对象！")
c, e = [], []           # 正确写法：各自造一个新列表
c.append(1)
print(f"c, e = [], [] 分别赋值     → c = {c}, e = {e}   ← 互不影响")
print(f"a is b → {a is b}，c is e → {c is e}")
# 坑 B：运算符优先级记不住就加括号，可读性永远优先
print(f"2 + 3 * 4 = {2 + 3 * 4}（先乘后加），(2 + 3) * 4 = {(2 + 3) * 4}")
print(f"not 1 == 1 = {not 1 == 1}   ← 比较先于 not，等价 not (1 == 1)")
# 坑 C：循环里用 += 拼字符串性能差（每轮都新建一个字符串）
pieces = ["a", "b", "c", "d"]
bad = ""
for p in pieces:
    bad += p
print(f"循环 += 拼接 : {bad!r}")
print(f"''.join()    : {''.join(pieces)!r}   ← 推荐，一次性分配内存")
print(f"'-'.join()   : {'-'.join(pieces)!r}   ← 还能指定分隔符")
# 坑 D：可变默认参数只在"定义时"创建一次，下次调用还用它（经典大坑）
def append_bad(item, box=[]):
    box.append(item)
    return box

print(f"append_bad(1) = {append_bad(1)}，append_bad(2) = {append_bad(2)}   ← 留着上次的 1！")
# 正确写法：默认值写 None，函数里再判断 if box is None: box = []（每次调用新建）。


# ============================================================
# 动手练习
# ============================================================
# 请把答案写在下方（或新建 try_exercise.py 练手），用 print() 验证结果。
# 参考答案在文件最末尾的三引号里，全部做完再看。
#
# 1. 用 type() 证明 "3 * 'ab'" 是一个表达式，打印它的值和类型。
# 2. 用二进制、八进制、十六进制字面量各写一个 255，打印它们是否相等。
# 3. 用下划线写出一千万，并打印它有几位数字（len(str(...))）。
# 4. 已知 s = "Hello, Python!"，只切片打印出 "Python"（不含逗号）。
# 5. 打印 r"C:\temp\note.txt" 的实际长度，并说明为什么不带 r 的写法更短。
# 6. 用 f-string 把 3.14159 格式化成：①两位小数 ②宽度 10 居中
#    ③整数 1234567 加千分位 ④0.456 转成百分比（保留一位小数）。
# 7. 一行列表推导式，取出 1..20 中能被 3 整除的数的平方。
# 8. 用字典推导式把 {"a": 1, "b": 2} 的键和值对调，得到 {1: "a", 2: "b"}。
# 9. 用 lambda 作为 key，把 ["ccc", "a", "bb"] 按长度降序排序。
# 10. 用生成器表达式求 1..10 中所有偶数的和（提示：sum 里直接放生成器）。
# 11. 写一个表达式：只有当 items 非空时输出它的长度，否则输出 "空"。

print("\n" + "=" * 60)
print("练习区结束 —— 往下是参考答案（做完再看！）")
print("=" * 60)


"""
================ 动手练习参考答案 ================

1. 表达式证明：3 * 'ab' 能被 type() 接收，说明它算出了值。
     print(type(3 * "ab"))     # <class 'str'>
     print(3 * "ab")           # ababab

2. 三种进制写法：
     print(0b11111111, 0o377, 0xFF)      # 255 255 255
     print(0b11111111 == 0o377 == 0xFF)  # True

3. 一千万 + 位数：
     n = 10_000_000
     print(len(str(n)))        # 8

4. 切出 "Python"：
     s = "Hello, Python!"
     print(s[7:13])            # Python（也可写 s[7:-1]）

5. 原始字符串长度：
     print(len(r"C:\temp\note.txt"))   # 16
     print(len("C:\temp\note.txt"))    # 14
     不带 r 时 \t 是"制表符"、\n 是"换行"，各只占 1 个字符，于是整体少 2。

6. f-string 四连：
     x = 3.14159
     print(f"{x:.2f}")          # 3.14
     print(f"[{x:^10.2f}]")     # [  3.14   ]
     print(f"{1234567:,}")      # 1,234,567
     print(f"{0.456:.1%}")      # 45.6%

7. 能被 3 整除的数的平方：
     print([n * n for n in range(1, 21) if n % 3 == 0])

8. 键值对调：
     d = {"a": 1, "b": 2}
     print({v: k for k, v in d.items()})     # {1: 'a', 2: 'b'}

9. 按长度降序排序：
     words = ["ccc", "a", "bb"]
     print(sorted(words, key=lambda w: len(w), reverse=True))

10. 偶数求和（生成器直接喂给 sum）：
     print(sum(n for n in range(1, 11) if n % 2 == 0))   # 2+4+6+8+10 = 30

11. 非空才输出长度：
     items = []
     print(len(items) if items else "空")    # 空（items 是空列表 → 假值）
     items = [1, 2, 3]
     print(len(items) if items else "空")    # 3

================ 小提醒 ================
- 做错的题不要只改结果，回头看看是"表达式写错"还是"思路错"。
- 打印出 <zip object ...> / <generator ...> 这类东西时，记得用 list() 包一下。
- 下一章会把这些表达式组合进 if / for / 函数，真正写出完整程序。
"""
