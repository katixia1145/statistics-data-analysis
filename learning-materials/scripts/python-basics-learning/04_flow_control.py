# -*- coding: utf-8 -*-
"""
============================================================
第 4 章：流程控制（if / while / for / break / match-case）
============================================================

【本章学什么】
  1. 缩进与代码块：Python 用缩进划分块，Tab 和空格不能混用。
  2. if / elif / else：分支顺序为什么重要、嵌套 if 怎么拍平。
  3. while 与 while...else：计数器循环、条件循环、while True + break。
  4. for 遍历 list / tuple / str / dict / set / range / zip / enumerate 与 for...else。
  5. break / continue / pass 的分工，以及两层循环怎么一次跳出去。
  6. match-case 结构模式匹配（需 Python 3.10+，见第 14 节）。

【怎么运行】VS Code 里按 Ctrl+F5 整体跑，或选中一段按 Shift+Enter 逐段跑；
  也可以直接执行：python 04_flow_control.py
【会看到什么】每节以分隔线开头，先给可运行代码，再用中文注释讲解，节末打印
  关键结果。全文不用 input()，输入都用预设数据模拟，不会卡住你。
============================================================
"""
# ============================================================
# 1. 代码块与缩进：Python 用缩进划分代码块
# ============================================================
# 别的语言用 { } 括块，Python 用缩进：冒号 : 表示"下面开始一个块"，块内缩进
# 必须完全一致，标准是 4 个空格（PEP 8 建议）。
# ⚠️ 坑：Tab 和空格混用 → IndentationError。VS Code 默认按 Tab 插 4 空格，但
#    从别处复制代码可能混进真 Tab；右下角可 "Convert Indentation to Spaces"。
# ⚠️ 坑：缩进只错一层有时不报错但逻辑跑偏——某行多缩进就变成上一层 if 的内部语句。
print("=" * 60)
print("【第 1 节】缩进 = 代码块：4 个空格一层，退回去就是块结束")
if True:
    print("  → 我在 if 块里（缩进一层）")
print("  → 我回到最外层，与 if 是否成立无关")   # 缩进退回 → 块结束
# ============================================================
# 2. if / elif / else：分支写法、elif 顺序、嵌套拍平
# ============================================================
print("=" * 60)
print("【第 2 节】if / elif / else")
score = 85
# elif 是 "else if"：从上往下逐个判断，命中一个就跳过后面全部。
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"  分数 {score} → 等级 {grade}")
# ⚠️ 坑：elif 是短路的。宽条件写前面，后面的分支就永远走不到（死代码）。
bad_score = 95
if bad_score >= 60:
    bad_grade = "及格"          # 95 也满足 >=60，直接命中
elif bad_score >= 90:
    bad_grade = "优秀"          # ← 永远轮不到它
print(f"  反例：{bad_score} 分判成「{bad_grade}」→ 正确做法是从严到宽排列")

# 嵌套 if 层数一多可读性就差；内层 else 与外层行为相同时一定要拍平。
user_role, logged_in = "admin", True
if user_role == "admin":
    if logged_in:
        print("  嵌套写法：管理员已登录，进入后台")
if user_role == "admin" and logged_in:        # 拍平：用 and 合并条件
    print("  拍平写法：管理员已登录，进入后台")
# ============================================================
# 3. 真值测试：哪些条件该简写、哪些绝对不能简写
# ============================================================
print("=" * 60)
print("【第 3 节】真值测试的简化写法")
# 任何对象都有真值：空容器、0、0.0、""、None 都为假。
print(f"  bool([])={bool([])}, bool('')={bool('')}, bool(0)={bool(0)}")
# 好习惯：判容器非空直接写 if 容器，比 if len(lst) > 0: 更 Pythonic。
print(f"  if 容器 → {'非空' if [1] else '空'}（不必写 len(lst) > 0）")
# ⚠️ 坑：0 是"合法值"时，if x: 会把有效数据判成假，这是真 bug。
temperature = 0
print(f"  if {temperature}: → 判成假，但 0℃ 是有效数据，这就是 bug")
if temperature is not None:
    print(f"  if x is not None: → 正确识别出 {temperature}℃ 有效")
# ⚠️ 坑：if x == True: 是坏味道，它会把 1 也当成 True，还掩盖类型问题。
print(f"  (1 == True) = {1 == True} → 说明 == True 会误纳 1")
# ⚠️ 坑：if a = 1: 是语法错误（= 是赋值）。要"边赋值边判断"用海象 := 且必须括号。
value = 7
if (n := value * 2) > 10:
    print(f"  海象运算符：先算出 n = {n}，再用它比较")
# ============================================================
# 4. 条件表达式：什么时候用一行搞定
# ============================================================
print("=" * 60)
print("【第 4 节】条件表达式（三元）与 if 语句的取舍")
age = 20
print(f"  条件表达式：{age} 岁 → {'成年' if age >= 18 else '未成年'}")
if age >= 18:                       # 等价的 if/else 写法
    label = "成年"
else:
    label = "未成年"
print(f"  等价 if 语句：{age} 岁 → {label}")
# 取舍：二选一且结果短 → 用条件表达式；分支更多、要嵌套三元 → 用 if/elif/else。
# ⚠️ 坑：a if c1 else b if c2 else d 这种嵌套三元极难读，别写。
# ============================================================
# 5. while ... else：正常结束才走 else
# ============================================================
print("=" * 60)
print("【第 5 节】while ... else")
i = 1
while i <= 3:
    i += 1                          # ⚠️ 忘了自增就是死循环
else:
    print(f"  A：正常结束 {i - 1} 次 → 执行了 else")
i = 1
while i <= 5:
    if i == 2:
        break
    i += 1
else:
    # ⚠️ 关键语义：else 只在"条件变假而正常结束"时执行，被 break 打断则不执行。
    print("  B：这行不会打印（循环被 break 打断了）")
print("  B：循环结束，继续往下走")
queue, target, pos = [3, 7, 11, 15], 11, 0      # C：找不到就交给 else 兜底
while pos < len(queue):
    if queue[pos] == target:
        print(f"  C：在索引 {pos} 找到 {target}")
        break
    pos += 1
else:
    print(f"  C：队列里没有 {target}")
# ============================================================
# 6. for 循环：遍历一切可迭代对象
# ============================================================
print("=" * 60)
print("【第 6 节】for 遍历各类容器")
# for 从可迭代对象里逐个取元素，取完自然结束，不用手动维护下标，比 while 安全。
for fruit in ["苹果", "香蕉"]:            # list
    print(f"  list   : {fruit}")
print(f"  tuple  : {list((1, 2, 3))}")
print(f"  str    : {'-'.join('Python')}   # 字符串按字符遍历")
person = {"name": "小明", "age": 18}
for k in person:                          # dict 默认遍历"键"
    print(f"  dict 键 : {k}")
print(f"  值/项   : {list(person.values())} / {list(person.items())}")
print(f"  set    : {', '.join({'A', 'B', 'C'})}   # 无序，别依赖顺序")
# 生成器表达式：边算边给、不占内存，适合数据多但只顺序处理一次的场景。
print(f"  生成器  : {list(x * x for x in range(5))}")
# ============================================================
# 7. range 三参数：左闭右开，支持负步长
# ============================================================
print("=" * 60)
print("【第 7 节】range(stop) / range(start, stop) / range(start, stop, step)")
# range 是"左闭右开"：含 start、不含 stop。返回惰性对象，看内容要 list()。
print(f"  range(5)        = {list(range(5))}        # 0~4，共 5 个")
print(f"  range(2, 6)     = {list(range(2, 6))}        # 2~5，共 4 个")
print(f"  range(0, 10, 3) = {list(range(0, 10, 3))}       # 步长 3，到 9 停")
print(f"  range(5, 0, -1) = {list(range(5, 0, -1))}       # 负步长倒数，到 1 停")
# ⚠️ 坑：想"包含 10"必须写 range(11)，stop 本身取不到——最常见的差一错误。
print(f"  1~10 和：range(1, 11)={sum(range(1, 11))}，写 range(1, 10) 少算 10={sum(range(1, 10))}")
# ⚠️ 坑：步长为 0 抛 ValueError；方向写反得到空区间（不报错，但结果是空的）。
print(f"  range(0, 5, -1) = {list(range(0, 5, -1))}   # 方向反了，静默给空列表")
total = 0
for _ in range(3):                        # 只关心次数时用 _ 占位
    total += 10
print(f"  for _ in range(3) 累加 10 → {total}")
# ============================================================
# 8. enumerate 与 zip：拿下标、并行遍历
# ============================================================
print("=" * 60)
print("【第 8 节】enumerate（带序号）与 zip（并行遍历）")
# enumerate 同时给出"序号 + 元素"；默认从 0 开始，start 可改起始编号。
for rank, name in enumerate(["张三", "李四", "王五"], start=1):
    print(f"  enumerate：第 {rank} 名 → {name}")
for subject, score in zip(["语文", "数学"], [88, 95]):   # 拉链式配对
    print(f"  zip 配对：{subject} {score} 分")
# ⚠️ 坑：zip 有"木桶效应"——长度不等按最短截断，多出来的静默丢弃、不报错。
print(f"  zip 长度不等：{list(zip([1, 2, 3], ['a', 'b']))} → 3 被悄悄丢掉")
# zip(*matrix) 转置：* 把每行拆成独立参数，zip 再把同列元素聚到一起。
matrix = [[1, 2, 3], [4, 5, 6]]
print(f"  原矩阵 {matrix} → 转置 {[list(r) for r in zip(*matrix)]}")
# ============================================================
# 9. for ... else：省掉标志位变量的利器
# ============================================================
print("=" * 60)
print("【第 9 节】for ... else")
def is_prime(n):
    """判断素数：用 for-else 省掉标志位变量。"""
    if n < 2:
        return False
    # 只需试到平方根：若 n = a*b，则 a、b 必有一个 <= sqrt(n)。
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False        # 找到因数 → 不是素数
    else:
        return True             # 循环没被打断 → 无因数 → 是素数

print(f"  2~29 的素数：{[n for n in range(2, 30) if is_prime(n)]}")
# 不用 for-else 就得声明 found 并在循环里置 True + break，多一处易忘改的地方。
for search in ("药水", "弓"):                 # 在列表里找元素
    for item in ["剑", "盾", "药水", "地图"]:
        if item == search:
            print(f"  找到：{search}")
            break
    else:
        print(f"  库存里没有 {search}（else 兜底，没写标志位）")
# ============================================================
# 10. break / continue / pass：三个关键字的分工
# ============================================================
print("=" * 60)
print("【第 10 节】break / continue / pass")
# break：立刻终止整个循环；continue：跳过本轮剩余语句、直接进下一轮。
kept = []
for n in range(1, 8):
    if n == 4:
        break                       # 碰到 4 整体停止，4 和它后面都不再处理
    kept.append(n)
print(f"  break 结果    ：{kept}")
print(f"  continue 结果 ：{[n for n in range(1, 9) if n % 2]}")
# ⚠️ 坑：while 里用 continue 时，要确保自增语句不被跳过，否则死循环。
i = count = 0
while i < 5:
    i += 1                          # 先自增，continue 才不会卡住循环
    if i == 3:
        continue
    count += 1
print(f"  while + continue：自增放前面才安全，count = {count}")

def todo_later():
    pass                            # pass 占位：语法要求有语句，但暂不写实现

print(f"  pass 只是占位符，不影响运行：todo_later() 返回 {todo_later()}")
# ============================================================
# 11. 嵌套循环：九九乘法表与"只跳出内层"
# ============================================================
print("=" * 60)
print("【第 11 节】嵌套循环")
# 写法一：双重 for，j <= i 只打下三角。
for i in range(1, 10):
    row = []
    for j in range(1, i + 1):
        row.append(f"{j}x{i}={i * j:2d}")
    print("    " + " ".join(row))
# 写法二：同一结果，用生成器 + join 拼行，代码更短（这里只示范第 3 行）。
i = 3
print("    " + " ".join(f"{j}x{i}={i * j:2d}" for j in range(1, i + 1)))  # 其余行同理
# ⚠️ 坑：内层 break 只跳出内层，外层照常继续（容易误以为整个循环都停了）。
for i in range(1, 3):
    hits = []
    for j in range(1, 5):
        if j == 3:
            break                   # 只结束内层
        hits.append(j)
    print(f"    外层 i={i}，内层收集到 {hits}（每次都到 2 就断）")

def find_first(matrix_data, target):
    """逃离方式 ③：封成函数用 return，一次退出所有层——最推荐。"""
    for row in matrix_data:
        for value in row:
            if value == target:
                return value
    return None

outer_done, found = False, None          # ① 标志位
for row in [[1, 2], [3, 4], [5, 6]]:
    if outer_done:
        break
    for value in row:
        if value == 4:
            found, outer_done = value, True
            break
for row in [[1, 2], [3, 4], [5, 6]]:     # ② for-else 反用
    for value in row:
        if value == 4:
            break
    else:
        continue                         # 内层没 break → 继续找下一行
    break                                # 内层 break 了 → 跳出外层
print(f"  一次跳出两层：① 标志位={found}  ② for-else 命中 4  "
      f"③ return={find_first([[1, 2], [3, 4], [5, 6]], 5)}")
# ============================================================
# 12. 综合小实战（全部用预设数据，不需要 input）
# ============================================================
print("=" * 60)
print("【第 12 节】综合小实战")
# 实战 1：while 模拟猜数字，猜测序列就是"预设的用户输入"。
secret, guesses, attempt = 42, [10, 75, 42, 99], 0
while attempt < len(guesses):
    guess = guesses[attempt]
    attempt += 1                    # 先自增，保证循环一定前进
    if guess == secret:
        print(f"  实战 1：第 {attempt} 次猜 {guess} → 命中！共 {attempt} 次")
        break
    print(f"  实战 1：第 {attempt} 次猜 {guess} → {'小了' if guess < secret else '大了'}")
else:
    print(f"  实战 1：{len(guesses)} 次都没猜中，游戏失败")
# 实战 2/3：计数用 dict.get(键, 默认值)，省掉 if 判断。
char_count = {}
for ch in "abracadabra":
    char_count[ch] = char_count.get(ch, 0) + 1
print(f"  实战 2：字符计数 → {sorted(char_count.items(), key=lambda kv: -kv[1])}")
word_count = {}
for word in "the quick fox jumps over the lazy dog the fox".split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"  实战 3：重复的词 → { {w: c for w, c in word_count.items() if c > 1} }")

def gcd(a, b):
    """实战 4：辗转相除法求最大公约数（while 的经典用法）。"""
    while b != 0:
        a, b = b, a % b             # 元组打包赋值，等价于同时更新 a、b
    return a

print(f"  实战 4：gcd(48,18)={gcd(48, 18)}, gcd(100,75)={gcd(100, 75)}, gcd(17,5)={gcd(17, 5)}")
# ============================================================
# 13. 常见坑集中演示
# ============================================================
print("=" * 60)
print("【第 13 节】常见坑集中演示")
# 坑 1：一边遍历一边删除 → 后面元素向前补位，导致漏删/漏项。
nums = [1, 2, 2, 3, 2, 4]
for n in nums:
    if n == 2:
        nums.remove(n)              # ⚠️ 边遍历边改长度，索引错位
print(f"  坑 1：边遍历边删 → {nums}（还剩一个 2 没删掉）")
# 修复 A：列表推导式重建（最推荐，语义清晰、结果确定）。
print(f"  修复 A（列表推导式）→ {[n for n in [1, 2, 2, 3, 2, 4] if n != 2]}")
# 修复 B：倒序删除——从后往前删，前面的索引不受影响。
nums = [1, 2, 2, 3, 2, 4]
for idx in range(len(nums) - 1, -1, -1):
    if nums[idx] == 2:
        del nums[idx]
print(f"  修复 B（倒序删除）→ {nums}")
# 坑 2：range 边界写错，循环少跑一次（见第 7 节）。
print(f"  坑 2：range(1, 5) 只到 4 → {list(range(1, 5))}，想要 1~5 得写 range(1, 6)")
# 坑 3：while x = 1: 是语法错误（= 是赋值）。比较写 while x == 1:，
#       边赋值边判断写 while (x := 值) > 0:。此处只说明，不写错误代码。
# 坑 4：浮点累加不精确，循环次数可能比预期多一次。
accumulate, rounds = 0.0, 0
while accumulate < 1.0:
    accumulate += 0.1
    rounds += 1
print(f"  坑 4：0.1 累加 {rounds} 次才 >= 1.0，其实是 {accumulate!r}（并非精确 1.0）")
print("       更稳：用整数计数器 range(10) 最后除 10，或比较时留容差 - 1e-9")
# ============================================================
# 14. match-case 结构模式匹配（需 Python 3.10+）
# ============================================================
print("=" * 60)
print("【第 14 节】match-case（需 Python 3.10+，老版本会 SyntaxError）")
# 它不只是"比相等"，而是按"结构"匹配：能解包元组、匹配序列和字典、加 if 守卫；
# 而 if/elif 链只能做值比较，遇到"不同形状的数据"就得写一堆 isinstance 判断。
def handle_command(command):
    match command:
        case "quit" | "exit":                       # 多值用 | 表示"或"
            return "程序退出"
        case ("move", x, y) if x == 0 and y == 0:   # 元组解包 + if 守卫
            return "原地不动"
        case ("move", x, y):                        # 元组解包
            return f"移动到 ({x}, {y})"
        case ["go", direction]:                     # 列表模式：长度位置都要对上
            return f"向 {direction} 走"
        case {"type": "click", "x": px, "y": py}:   # 字典模式：多出的键会被忽略
            return f"在 ({px}, {py}) 处点击"
        case _:                                     # _ 通配符 = default 分支
            return "无法识别的指令"

for cmd in ["quit", ("move", 3, 5), ("move", 0, 0), ["go", "north"],
            {"type": "click", "x": 10, "y": 20}, "whatever"]:
    print(f"  {cmd!s:<40} → {handle_command(cmd)}")
# 怎么选：判"值的相等/区间"→ if/elif 更自然、兼容性更好；处理"不同形状的
# 结构"（配置、指令、协议报文）→ match-case 清晰得多；兼容 3.9 只能用 if/elif。
# ============================================================
# 动手练习
# ============================================================
# 请另建临时文件写答案，别改本文件；全部用预设数据，不用 input()。
# 1. 基础：year = 2024，判断是否闰年（能被 4 整除且不能被 100 整除，或能被 400 整除）。
# 2. 基础：用 while 打印 1~20 里所有能被 3 整除的数。
# 3. 进阶：nums = [5, -3, 0, 8, -1]，用 for-else 找出第一个负数，
#    若全是非负数则打印"没有负数"，要求不使用标志位变量。
# 4. 进阶：用 range 与 for 求 1~100 的总和、偶数之和，验证两个结果能对上。
# 5. 进阶：用 enumerate(start=1) 打印 ["apple","banana","cherry"] 的编号列表。
# 6. 中等：a = [1, 2, 3, 4]、b = [10, 20, 30]，用 zip 打印配对结果，
#    并说明多出来的 4 去哪了。
# 7. 中等：把"判断 97 是否为素数"写成函数，内部用 for-else，
#    同时返回"是否素数"和"最小因数"。
# 8. 中等：用嵌套循环打印 5 行倒三角星号（第 1 行 5 个星，最后一行 1 个）。
# 9. 挑战：写函数用 zip(*matrix) 返回二维列表的转置，再手写双重 for 版本对照结果。
# 10. 挑战：模拟石头剪刀布。预设玩家出拳 ["石头","剪刀","布","石头"]、电脑出拳
#     ["布","石头","布","石头"]，用 zip 逐轮判胜负并累计比分，最后打印总比分。
# ============================================================
# 参考答案（放在三引号字符串里，保证不参与执行）
# ============================================================
ANSWERS = """
参考而已，写法不唯一。
# --- 1. 闰年 ---
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} 是闰年" if is_leap else f"{year} 不是闰年")
# 提醒：and/or 混用优先级容易出错，拿不准就加括号。
# --- 2. while 打印 1~20 内 3 的倍数 ---
i = 1
while i <= 20:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1              # ⚠️ 忘了自增就是死循环
print()
# --- 3. for-else 找第一个负数 ---
for n in [5, -3, 0, 8, -1]:
    if n < 0:
        print(f"第一个负数是 {n}")
        break
else:
    print("没有负数")   # 没 break 才走这里，等价于"没找到"，不用标志位
# --- 4. 1~100 的和 ---
total = sum(range(1, 101))
even_sum = sum(n for n in range(2, 101, 2))
print(total, even_sum, total - even_sum, (total - even_sum) + even_sum == total)
# --- 5. enumerate 编号 ---
for idx, w in enumerate(["apple", "banana", "cherry"], start=1):
    print(f"{idx}. {w}")
# --- 6. zip 木桶效应 ---
a, b = [1, 2, 3, 4], [10, 20, 30]
print(list(zip(a, b)))          # [(1, 10), (2, 20), (3, 30)]
print(f"多出来的 {a[len(b):]} 被丢弃：zip 按最短的截断，且不报错。")
# --- 7. 素数判定（返回是否素数 + 最小因数）---
def check_prime(n):
    if n < 2:
        return False, None
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False, d         # 找到最小因数
    else:
        return True, None           # 循环正常结束 → 无因数
print(check_prime(97), check_prime(91))     # (True, None) (False, 7)
# --- 8. 倒三角 ---
for i in range(5, 0, -1):           # 负步长从 5 数到 1，比手写 n -= 1 简洁
    print("*" * i)
# --- 9. 矩阵转置 ---
matrix = [[1, 2, 3], [4, 5, 6]]
by_zip = [list(row) for row in zip(*matrix)]
by_loop = [[matrix[r][c] for r in range(len(matrix))]
           for c in range(len(matrix[0]))]
print(by_zip, by_zip == by_loop)    # [[1, 4], [2, 5], [3, 6]] True
# --- 10. 石头剪刀布 ---
player, computer = ["石头", "剪刀", "布", "石头"], ["布", "石头", "布", "石头"]
beats = {("石头", "剪刀"), ("剪刀", "布"), ("布", "石头")}   # 玩家赢的组合
win = lose = draw = 0
for idx, (p, c) in enumerate(zip(player, computer), start=1):
    if p == c:
        draw, result = draw + 1, "平"
    elif (p, c) in beats:
        win, result = win + 1, "玩家胜"
    else:
        lose, result = lose + 1, "电脑胜"
    print(f"第 {idx} 轮：玩家 {p} vs 电脑 {c} → {result}")
print(f"总比分：玩家 {win} 胜 / 电脑 {lose} 胜 / {draw} 平")
"""
