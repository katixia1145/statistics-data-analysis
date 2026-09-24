# -*- coding: utf-8 -*-
"""
============================================================
第 01 章：变量 —— 名字与对象的绑定
============================================================

【本章学什么】
1. 变量不是“装值的盒子”，而是“贴在对象上的名字”，用 id() 亲眼验证。
2. 赋值的本质：重新赋值、多重赋值、链式赋值、交换、星号解包。
3. 命名规则（合法标识符 / 关键字 / 大小写）与风格（snake_case / UPPER_CASE），
   以及覆盖内置名（list / str / id / type / sum）的严重后果。
4. type() 与 isinstance() 看类型，理解“动态类型”，并与 C / Java 的静态类型对比。
5. id() 与 is：小整数缓存、字符串驻留、is 与 == 的区别（同一对象 vs 值相等）。
6. 可变 vs 不可变对象、别名陷阱、深浅拷贝、del、常量约定、作用域、
   类型注解，以及一堆新手常见坑。

【怎么运行】
   · VS Code 里点右上角 ▶ 或按 Ctrl+F5 跑整个文件；想逐段跑就选中若干行，
     右键 “Run Selection/Line in Python Terminal”（Shift+Enter），按小节顺序跑。
   · 命令行：python 01_variables.py
   · 本文件零交互、零联网、零读写磁盘、没有死循环，跑完自动退出，不会卡住。

【会看到什么】
   · 一串带 “---” 分隔线的分节输出，每节末尾用 print(f"...") 打印关键结果；
     带 “⚠️ 坑：” 的注释是新手最常踩的雷，建议逐条看。
   · id() 打印的是一长串内存地址，每次运行都可能不同，只需看两次是不是同一个数。
   · 文件底部有 10 道动手练习，参考答案在最后一个三引号字符串里，只是文本、不执行。
"""

import copy        # 演示浅拷贝 copy.copy 与深拷贝 copy.deepcopy
import keyword     # 查看 Python 的全部关键字
import sys         # 演示 sys.intern() 字符串驻留

print("=" * 60)
print("第 01 章：变量")
print("=" * 60)


# ============================================================
# 1. 变量不是“盒子”，是“名字绑定对象”
# ============================================================
# C 语言教材说“变量是装值的盒子”，Python 完全不是这个模型：
#     变量 = 名字      值 = 对象      赋值 = 让名字指向某个对象
# 把对象想成桌上的球，变量名是贴在球上的标签：一个球能贴多张标签，标签也能撕下来换球。
a = 10
print(f"a = {a} | type(a) = {type(a)} | id(a) = {id(a)}")   # 值 | 类型 | 身份
b = a          # 不是“把 10 复制给 b”，而是给同一个对象再贴一张标签
print(f"b = {b} | id(b) = {id(b)} | a is b -> {a is b}   # True：同一个对象")
a = 20         # 重新赋值：把 a 这张标签撕下来，贴到新对象上
print(f"a = {a} | id(a) = {id(a)}")
print(f"b = {b} | id(b) = {id(b)}   # b 没受影响，它还贴着那个旧对象")
# 一句话：a = X 只做两件事 —— 先算出右边的对象 X，再让名字 a 指向它。
print("-" * 60)


# ============================================================
# 2. 赋值的本质：重新赋值只是换个绑定
# ============================================================
score = 60
print(f"score = {score} | id = {id(score)}")
score = 60                       # 再赋一次完全相同的值
print(f"score = {score} | id = {id(score)}   # 猜猜 id 变了吗？")
# ⚠️ 坑：两次 id 相同，不代表“赋值把值塞进了盒子”。这是编译器把同一段代码里“值
#         相同的常量”合并成了同一个对象（小整数还会被缓存）。换成运行时才算出来的
#         大整数，id 立刻就变，第 6 节细讲。
x = [1, 2, 3]
y = z = x                        # 三个名字指向同一个对象，这就是“别名 alias”
print(f"x = {x} | y = {y} | z = {z}")
print(f"三个名字是同一个对象？{x is y is z}   id = {id(x)}, {id(y)}, {id(z)}")
print(f"sys.getrefcount(x) = {sys.getrefcount(x)}   # 3 个名字 + 函数参数，所以 >= 4")
# ⚠️ 坑：别名是双刃剑，通过 y 修改列表，x 也会“跟着变”，第 10 节重点演示。
print("-" * 60)


# ============================================================
# 3. 变量命名规则：合法标识符与关键字
# ============================================================
# 规则（不满足就是 SyntaxError）：① 只能由字母、数字、下划线组成，不能数字开头；
# ② 不能是关键字；③ 区分大小写（age / Age / AGE 是三个名字）；④ 不能含空格、连字符。
中文名 = "能跑，但别这么写"      # Unicode 允许中文标识符，可读性和可维护性都很差
print(f"中文名 = {中文名}")
for name in ["age", "_x", "x1", "1x", "my-var", "if", "True", "你好"]:
    print(f"  {name!r:>10} 是合法标识符？{name.isidentifier()}")
# 注意：'if'、'True' 的 isidentifier() 也是 True —— 判断关键字得用 keyword 模块。
print(f"Python 关键字共 {len(keyword.kwlist)} 个：{' '.join(keyword.kwlist)}")
print(f"keyword.iskeyword('class') -> {keyword.iskeyword('class')} | "
      f"iskeyword('Class') -> {keyword.iskeyword('Class')}   # 关键字区分大小写")
# ⚠️ 坑：True / False / None 不能当变量名（SyntaxError）；而 true = 1 合法，只是极误导。
print("-" * 60)


# ============================================================
# 4. 命名风格：snake_case、UPPER_CASE 与内置名陷阱
# ============================================================
# 风格不是语法，是 PEP 8 约定：变量 / 函数用 snake_case；常量用 UPPER_CASE；类名用
# PascalCase；内部用前缀下划线。别的语言那套 camelCase 在 Python 里格格不入。
user_name, total_count, MAX_SIZE = "小明", 3, 100
print(f"snake_case: user_name = {user_name}, total_count = {total_count}")
print(f"UPPER_CASE: MAX_SIZE = {MAX_SIZE}   # 看到全大写就知道“请勿修改”")
# ⚠️ 坑：用内置名当变量名会“覆盖”内置函数，后果很严重，下面演示完立刻恢复。
list = [1, 2, 3]                # 覆盖内置类型 list
print(f"list = {list}   # list 现在是个列表，不再是内置类型了")
# print(list("abc"))            # 这行会 TypeError: 'list' object is not callable
del list                        # 删掉这个名字，内置的 list 就回来了
print(f"del list 之后 list('abc') = {list('abc')}   # 内置类型恢复可用")
str, id, type, sum = "被覆盖", 7, "也被覆盖", 1 + 1
print(f"str = {str}, id = {id}, type = {type}, sum = {sum}   # 全变成普通变量")
del str, id, type, sum          # 一次性删掉，内置函数全部回归
print(f"恢复后：id(0) = {id(0)} | type(1) = {type(1)} | sum([1, 2, 3]) = {sum([1, 2, 3])}")
# 黑名单：list str dict set int float id type sum max min len input print open。
print("-" * 60)


# ============================================================
# 5. type() 与 isinstance()：动态类型的含义
# ============================================================
# 变量本身没有类型，类型属于“对象”；名字指向谁，它就“是”什么类型。
value = 42
print(f"value = {value} | type = {type(value)} | 名字 = {type(value).__name__}")
value = "四十二"                # 同一个名字换绑到字符串，完全合法
value = [4, 2]                  # 再换绑到列表
print(f"value = {value} | type = {type(value)}   # 动态类型：类型运行时才确定")
# 对比：C / Java 是静态类型，int a = 10 之后 a 只能是 int，a = "abc" 直接编译不过；Python 更
# 灵活，但错误暴露得更晚，大项目通常靠注解 + mypy 把检查提前（见第 14 节）。
n = 7
print(f"isinstance(7, int) = {isinstance(n, int)} | isinstance(7, float) = {isinstance(n, float)}")
print(f"isinstance(7, (int, str)) = {isinstance(n, (int, str))}   # 第二个参数可以是元组")
# ⚠️ 坑：bool 是 int 的子类，isinstance(True, int) 竟然是 True！
print(f"isinstance(True, int) = {isinstance(True, int)} | type(True) == int -> {type(True) == int}")
print("-" * 60)


# ============================================================
# 6. id() 与 is：小整数缓存、字符串驻留、is 与 == 的区别
# ============================================================
# is 比较身份（是不是同一个对象），== 比较值（内容是否相等），别混用。
p, q = [1, 2, 3], [1, 2, 3]
r = p
print(f"p == q -> {p == q}   # True：内容一样")
print(f"p is q -> {p is q}   # False：两个不同对象，id = {id(p)} vs {id(q)}")
print(f"r is p -> {r is p}   # True：别名，同一个对象")
# 【小整数缓存】CPython 启动时就建好 -5 ~ 256 的整数对象反复复用；下面故意让变量参与运算
# 逼编译器把计算留到运行时，这才真的在考察缓存（否则会被“常量合并”作弊）。
base, m = 6, 100
k = 2 ** base + 36              # 运行时算出 100
print(f"k = {k}；m is k -> {m is k}   # True：命中了小整数缓存")
big1, big2 = 1000, 1 + 999 + 0 * m      # 运行时算出 1000，超出缓存范围
print(f"big2 = {big2}；big1 is big2 -> {big1 is big2}   # False：大整数不复用")
# ⚠️ 坑：big1 = 1000; big2 = 1000 这种写法常量会被合并成同一对象、结果可能是 True，不能依赖。
# 【字符串驻留】像标识符的短字符串会被自动驻留，同一份内容共用一个对象。
s1, part = "hello_world_1", "world_1"
s2 = "hello_" + part            # 运行时拼出来的字符串，通常不会被自动驻留
print(f"s1 == s2 -> {s1 == s2} | s1 is s2 -> {s1 is s2}   # 内容相同，通常不是同一对象")
s3 = sys.intern("hello_" + part)        # 手动驻留：把它放进驻留池
print(f"sys.intern 之后 s1 is s3 -> {s1 is s3}   # True")
# ⚠️ 坑：驻留是 CPython 的实现细节，换解释器或版本可能不同；比内容用 ==，比身份才用 is。
result = None
print(f"result is None -> {result is None}（推荐）| result == None -> {result == None}（不推荐）")
print("-" * 60)


# ============================================================
# 7. 多重赋值、链式赋值与交换
# ============================================================
# 多重赋值：右边先整体求值成一个对象，再按位置依次绑定左边。
a, b = 1, 2
print(f"a, b = 1, 2  ->  a = {a}, b = {b}")
c, d = "12"                     # 右边也可以是列表、字符串
print(f"c, d = \"12\"  ->  c = {c!r}, d = {d!r}   # 字符串被解包成两个字符")
a, b = b, a                     # 右边 (b, a) 先整体求值，所以不需要中间变量
print(f"a, b = b, a  ->  a = {a}, b = {b}   # 一行完成交换")
e = f = 0                       # 链式赋值：两个名字指向同一个对象
print(f"e = f = 0  ->  e = {e}, f = {f}, e is f -> {e is f}")
# ⚠️ 坑：可变对象千万别用链式赋值，多个名字会共享同一个对象：
list_a = list_b = []
list_a.append(1)
print(f"list_a = {list_a}, list_b = {list_b}   # 改了 a，b 也变了 <- 经典翻车现场")
list_c, list_d = [], []         # 要各自独立，就必须分开写
list_c.append(1)
print(f"list_c = {list_c}, list_d = {list_d}   # 这次互不影响")
print("-" * 60)


# ============================================================
# 8. 星号解包：a, *rest = ...
# ============================================================
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first, *middle, last = [1..5]  ->  {first}, {middle}, {last}")
*init, tail = [10, 20, 30]
print(f"*init, tail = [10, 20, 30]  ->  init = {init}, tail = {tail}")
head, *rest = "abcdef"
print(f"head, *rest = \"abcdef\"  ->  head = {head!r}, rest = {rest!r}")
# 带 * 的名字永远得到 list（哪怕只剩一个元素，也是 [x] 而非 x）；同一行只允许一个 * 名字。
try:
    g, h = [1, 2, 3]
except ValueError as err:
    print(f"g, h = [1, 2, 3]  ->  {type(err).__name__}: {err}")
try:
    g, h, i = [1, 2]
except ValueError as err:
    print(f"g, h, i = [1, 2]  ->  {type(err).__name__}: {err}")
# ⚠️ 坑：解包失败时整个语句原子失败，左边的名字不会被“部分赋值”。
print("-" * 60)


# ============================================================
# 9. 可变对象与不可变对象
# ============================================================
# 不可变：int / float / bool / str / tuple / frozenset / None；可变：list / dict / set / bytearray。
# “不可变”指的是“对象自己不能被改”，你只能换一个对象；变量本身随便重新绑定。
s = "abc"
print(f"s = {s!r} | id = {id(s)}")
s += "def"                      # str 的 += 是新建一个字符串，再把名字 s 指过去
print(f"s = {s!r} | id = {id(s)}   # id 变了：新对象，原来的 abc 没被改动")
nums = [1, 2]
print(f"nums = {nums} | id = {id(nums)}")
nums += [3]                     # list 的 += 等价于原地 extend，不换对象
print(f"nums = {nums} | id = {id(nums)}   # id 没变：原地修改，同一个对象")
nums = nums + [4]               # 而 nums = nums + [...] 是拼出新列表再重新绑定
print(f"nums = {nums} | id = {id(nums)}   # id 又变了：这是新建的列表")
try:
    (1, 2)[0] = 9               # tuple 不可变，这行会抛 TypeError
except TypeError as err:
    print(f"元组元素赋值 -> {type(err).__name__}: {err}")
print(f"于是只能重建：(1, 2) + (3,) = {(1, 2) + (3,)}   # 这是新元组，不是原地修改")
print("-" * 60)


# ============================================================
# 10. 别名陷阱：浅拷贝与深拷贝
# ============================================================
original = [1, [2, 3], 4]
alias = original                # 只是多贴一张标签，并不是复制
alias[0] = 999
print(f"改 alias[0] 之后 original = {original}   # 原列表也被改了！")
# ⚠️ 坑：b = a 不是“复制一份”，而是给同一个对象起了第二个名字。
shallow = original.copy()       # 等价于 copy.copy(original)，只复制最外层
shallow[0] = -1                 # 顶层元素是独立副本，改它不影响 original
print(f"浅拷贝后改 shallow[0]：shallow = {shallow}")
shallow[1].append(99)           # 但嵌套的那个列表还是同一个对象！
print(f"再改 shallow[1].append(99)：original = {original}   # 也跟着变了 <- 浅拷贝的坑")
deep = copy.deepcopy(original)  # 深拷贝：递归复制整棵树
deep[1].append(777)
print(f"深拷贝后改 deep[1]：deep = {deep}")
print(f"                    original = {original}   # 完全不受影响")
# 记忆：浅拷贝只复制一层、深拷贝复制整棵树；嵌套可变对象又要彻底独立就用 deepcopy。
print(f"切片 original[:] 是新对象吗？-> {original is original[:]}   # False，切片是浅拷贝")
print("-" * 60)


# ============================================================
# 11. del 语句：删名字，不删对象
# ============================================================
temp = [1, 2, 3]
backup = temp                   # 两个名字指向同一个列表对象
print(f"temp = {temp} | id = {id(temp)}")
del temp                        # 只删掉 temp 这个绑定，对象本身还在
print(f"del temp 之后 backup = {backup} | id = {id(backup)}   # 对象还活着")
try:
    print(temp)
except NameError as err:
    print(f"再用 temp -> {type(err).__name__}: {err}")
# ⚠️ 坑：del 不是“销毁数据”，而是“撕掉标签”；只要还有别的名字指向它，数据就还在。
bag = {"a": 1, "b": 2}
del bag["a"]                    # 删除字典里的键：改的是可变对象的内容
nums2 = [1, 2, 3, 4]
del nums2[1:3]                  # 删除切片范围内的元素
print(f"del bag['a'] -> {bag} | del nums2[1:3] -> {nums2}")
g1, g2 = "x", "y"; del g1, g2   # 一条 del 也能删多个名字，之后再用就是 NameError
print("-" * 60)


# ============================================================
# 12. 常量：Python 没有真正的常量
# ============================================================
# 语法层面没有 const，全靠全大写约定：“这是常量，请勿修改”。
PI, MAX_CONNECTIONS, DEFAULT_TIMEOUT = 3.14159, 100, 30
print(f"PI = {PI}, MAX_CONNECTIONS = {MAX_CONNECTIONS}, DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")
MAX_CONNECTIONS = 200           # 语法上完全合法，只是代码审查时会被同事骂
print(f"改成 {MAX_CONNECTIONS} 也不报错 —— 这就是“约定”两个字的含义")
# 想让类型检查器帮忙拦截，可以用 typing.Final 标注：
from typing import Final
SECONDS_PER_MINUTE: Final[int] = 60
print(f"SECONDS_PER_MINUTE: Final[int] = {SECONDS_PER_MINUTE}   # mypy 会拦，python 不拦")
frozen = frozenset([1, 2, 3])   # 真需要“不可修改的容器”，用 frozenset / tuple
print(f"frozen = {frozen}；调用 frozen.add(4) 会抛 AttributeError")
print("-" * 60)


# ============================================================
# 13. 变量作用域初体验（细节留给函数章）
# ============================================================
outer_x = "外面的 x"
def demo_scope():
    inner_x = "函数里的 x"      # 局部变量，函数一结束就没了
    return inner_x
print(f"函数里返回：{demo_scope()} | 函数外依然：outer_x = {outer_x}")
try:                            # 本章变量都在模块顶层；函数内部是另一个世界，第 05 章细讲
    print(inner_x)
except NameError as err:
    print(f"函数里定义的 inner_x 在外面用 -> {type(err).__name__}: {err}")
print("-" * 60)


# ============================================================
# 14. 类型注解：写给人看的，不是给解释器强制执行的
# ============================================================
# 语法：变量名: 类型 = 值；函数：def f(参数: 类型) -> 返回类型
age: int = 18
name: str = "小明"
scores: list[int] = [90, 85, 77]
mapping: dict[str, float] = {"语文": 95.5, "数学": 88.0}
print(f"age = {age}, name = {name!r}, scores = {scores}, mapping = {mapping}")
def add(a: int, b: int) -> int:
    """返回两数之和；注解只是文档 + 类型检查器的输入。"""
    return a + b
print(f"add(1, 2) = {add(1, 2)}   # 按预期工作")
print(f"add('1', '2') = {add('1', '2')!r}   # ⚠️ 传字符串照样跑，返回 '12'")
age = "十九"                     # 注解写的是 int，赋字符串也没人拦
print(f"age = {age!r} | type = {type(age)}   # 注解与实际类型可以完全不符")
print(f"add.__annotations__ = {add.__annotations__}")
# 那注解有什么用？① IDE 智能提示与标红；② mypy / pyright 在写代码阶段查错；③ 让人一眼看懂
# 意图。它是“文档 + 工具输入”，不是运行时约束。
print("-" * 60)


# ============================================================
# 15. 常见坑汇总
# ============================================================
# 坑 1：浮点数误差 —— 这是 IEEE 754 的通病，不是 Python 的锅。
print(f"0.1 + 0.2 = {0.1 + 0.2} | 0.1 + 0.2 == 0.3 -> {0.1 + 0.2 == 0.3}   # 竟然是 False")
from decimal import Decimal
print(f"Decimal('0.1') + Decimal('0.2') == Decimal('0.3') -> "
      f"{Decimal('0.1') + Decimal('0.2') == Decimal('0.3')}   # 金额请用 Decimal 或整数分")
print(f"容忍误差的写法 abs(差) < 1e-9 -> {abs((0.1 + 0.2) - 0.3) < 1e-9}")
# 坑 2：字符串“改不了”（word[0] = "H" 会 TypeError），但可以重新绑定。
word = "hello"
word = "H" + word[1:]
print(f"想改首字母 -> word = {word!r}   # 拼出新字符串，而不是原地修改")
# 坑 3：同一个变量前后装不同类型，可读性崩坏（合法，但非常危险）。
data = 10; data = "十"; data = [10]
print(f"data 一路从 int 变成 str 再变成 {type(data).__name__}")
# 坑 4：a = b = [] 让两个名字共享同一个列表。
shared_a = shared_b = []; shared_a.append("x")
print(f"shared_a = {shared_a}, shared_b = {shared_b}   # 它们是同一个列表")
# 坑 5：变量名打错一个字母不会报“拼写错误”，只会在使用时 NameError。
user_nmae = "小明"; print(f"user_nmae = {user_nmae}   # 报 NameError 时，先回看赋值那一行的拼写")
print("=" * 60)
print("本章结束：变量是名字，对象是值，is 看身份，== 看内容。")
print("=" * 60)


# ============================================================
# 动手练习
# ============================================================
# 把每题的代码敲在文件末尾（或新建临时文件）自己跑一遍，做完再对答案。
# 【1】city = "北京"、population = 2189，用一条 f-string 打印出：城市：北京 | 人口：2189万 | 类型：str/int。
# 【2】用 id() 验证“同一个整数赋给两个名字是不是同一个对象”，再对比字面量 1000 与运行时算出的 1000。
# 【3】判断 _count / 2price / my-var / class / 单价 / totalPrice / pass 哪些合法，用 .isidentifier() 与 keyword.iskeyword() 验证并说明理由。
# 【4】用一行多重赋值把 1、2、3 分别赋给 low、mid、high，再用一行把它们倒过来（变成 3、2、1）。
# 【5】nums = [1, 2, 3, 4, 5, 6]，用星号解包取出第一个、最后一个和中间所有元素，说明中间那个是 list 还是 tuple。
# 【6】a = b = [1, 2] 后执行 b.append(3)，此时 a 是什么？再改成 b = a.copy() 后 append(3)，a 又是什么？解释原因。
# 【7】grid = [[1, 2], [3, 4]]，用 copy.copy() 与 copy.deepcopy() 各复制一份，修改副本“内层”列表的元素，观察原数据是否被波及。
# 【8】先猜再跑 0.1 + 0.2 == 0.3 与 Decimal("0.1") + Decimal("0.2") == Decimal("0.3")，再解释金额为什么不能用浮点 == 比较。
# 【9】定义 calc(a: int, b: int) -> int 返回 a * b，故意传两个字符串进去，观察结果并解释类型注解是否被强制执行。
# 【10】综合题：记录学生姓名(str)、三门课成绩(list[int])、平均分(float)、是否及格(bool)，用 sum()/len() 求平均分并打印全部信息，最后 del 掉成绩列表并捕获 NameError。变量用 snake_case，及格线 60 用全大写常量。


# ============================================================
# 参考答案（下面只是一段文本，不会被执行，所以不影响运行）
# ============================================================
"""
# 1
city, population = "北京", 2189
print(f"城市：{city} | 人口：{population}万 | 类型：{type(city).__name__}/{type(population).__name__}")
# 2
x = 100; y = x; print(x is y)                  # True：同一个对象
m = 1000; n = 1 + 999 + 0 * x; print(m is n)   # False：两个不同对象
# 字面量可能在编译期被合并成同一个常量对象，小整数还会命中缓存，所以 is 比较整数不可靠。
# 3
import keyword
names = ["_count", "2price", "my-var", "class", "单价", "totalPrice", "pass"]
print([(n, n.isidentifier(), keyword.iskeyword(n)) for n in names])
# 2price 数字开头；my-var 含连字符；class / pass 是关键字；单价与 totalPrice 合法，
# 但单价不推荐、totalPrice 按 PEP 8 应写成 total_price。
# 4
low, mid, high = 1, 2, 3
low, mid, high = high, mid, low     # 右侧先整体求值，所以不需要中间变量；结果 3 2 1
# 5
head, *middle, tail = [1, 2, 3, 4, 5, 6]
print(head, middle, tail, type(middle).__name__)   # 1 [2, 3, 4, 5] 6 list（带 * 永远得到 list）
# 6
a = b = [1, 2]; b.append(3); print(a)              # [1, 2, 3]：a、b 是同一个列表
a = [1, 2]; b = a.copy(); b.append(3); print(a)    # [1, 2]：copy() 造了新列表，互不影响
# 7
import copy; grid = [[1, 2], [3, 4]]
copy.copy(grid)[1][0] = 999; print(grid)           # 浅拷贝内层共享 -> [[1, 2], [999, 4]]
copy.deepcopy(grid)[1][0] = -1; print(grid)        # 深拷贝所有层级 -> 完全没变
# 8
from decimal import Decimal
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)                       # 0.30000000000000004 False
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) # True
# 0.1 / 0.2 / 0.3 在二进制浮点里都不精确，相加有微小误差；金额要用 Decimal 或整数“分”。
# 9
def calc(a: int, b: int) -> int: return a * b
print(calc(3, 4), calc("3", "4"))   # 12 '33'：字符串乘法是“重复拼接”，居然能跑
# 类型注解在运行时不做任何强制检查，它只服务于 IDE 提示和 mypy / pyright 静态检查。
# 10
student_name, course_scores, PASS_LINE = "李雷", [88, 92, 79], 60
average = sum(course_scores) / len(course_scores)
is_pass = average >= PASS_LINE
print(f"姓名：{student_name} | 成绩：{course_scores}（共 {len(course_scores)} 门）")
print(f"平均分：{average:.2f} | 是否及格：{is_pass}（及格线 {PASS_LINE}）")
print(f"成绩类型：{type(course_scores).__name__} | 平均分类型：{type(average).__name__}")
del course_scores                    # del 删的是名字绑定，不是数据本身
try:
    print(course_scores)
except NameError as err:
    print(f"删除后再访问 -> {type(err).__name__}: {err}")
"""
