# -*- coding: utf-8 -*-
"""Python 基础语法 · 第六章：综合练习（共 26 题）
====================================================================
【用途】前五章综合练习：01 变量 / 02 运算符 / 03 表达式（字符串·列表·字典·推导式）
/ 04 流程控制（if·for·while·break·else）/ 05 函数（参数·递归·闭包·装饰器）。
每题都配一个可直接运行的参考实现，函数名形如 ex01_xxx。

【怎么用】先只看题干注释、遮住函数体自己写一遍，写完再对照参考实现。
难度 ★★★ 的题（第 20 题菱形）若卡住，看文件末尾「参考答案」的思路拆解。

【怎么运行】VS Code 右上角 ▶ 运行，或终端执行：python 06_exercises.py
无参数、无交互、无文件读写。本文件不使用 input()，所有"输入"都以参数给出，
方便你改参数反复验证；调试某题时把光标放进去按 F10 单步即可。
====================================================================
"""
import functools
import math


# ===== 第一部分：变量与运算符（对应 01、02 章）=====
# ------------------------------------------------------------
# 【题 1】圆面积与周长计算                          [难度：★☆☆]
# 要求：给定半径，用 math.pi 算面积与周长，结果保留两位小数。练点：变量赋值、** 幂运算、math 模块调用、round 格式化。
# ------------------------------------------------------------
def ex01_circle(radius):
    """你的实现写在这里"""
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return f"半径 {radius:.2f}：面积 {round(area, 2)}，周长 {round(perimeter, 2)}"

# ------------------------------------------------------------
# 【题 2】秒数转"时分秒"                            [难度：★☆☆]
# 要求：用 // 和 % 把秒数拆成 h/m/s，注意边界 0 秒与 3661 秒。练点：整除 //、取余 %，以及"先取整再取余"的拆位思路。
# ------------------------------------------------------------
def ex02_hms(seconds):
    """你的实现写在这里"""
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    return f"{seconds} 秒 = {h} 时 {m} 分 {s} 秒"

# ------------------------------------------------------------
# 【题 3】交换两个变量                              [难度：★☆☆]
# 要求：不借助第三个变量，用多重赋值交换 a、b 并打印前后结果。练点：Python 特有的元组解包赋值 a, b = b, a。
# ------------------------------------------------------------
def ex03_swap(a, b):
    """你的实现写在这里"""
    print(f"  交换前：a = {a}, b = {b}")
    a, b = b, a
    return f"交换后：a = {a}, b = {b}"

# ------------------------------------------------------------
# 【题 4】判断闰年                                  [难度：★☆☆]
# 要求：能被 4 整除且不能被 100 整除，或能被 400 整除；同时用链式比较校验年份范围。练点：and / or 优先级、链式比较 1 <= year <= 9999。
# ------------------------------------------------------------
def ex04_is_leap(year):
    """你的实现写在这里"""
    if not 1 <= year <= 9999:  # 链式比较等价于 year >= 1 and year <= 9999
        return False
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# ------------------------------------------------------------
# 【题 5】位运算小练习                              [难度：★☆☆]
# 要求：判断 n 是否为 2 的幂：n > 0 and (n & (n - 1)) == 0，并打印 n 与 n-1 的二进制，直观看到"抹掉最低位 1"的效果。练点：位与 &、bin()、位运算的巧用。
# ------------------------------------------------------------
def ex05_power_of_two(n):
    """你的实现写在这里"""
    is_pow = n > 0 and (n & (n - 1)) == 0
    return (f"n = {n:>3}  bin = {bin(n):>8}  n-1 bin = {bin(n - 1):>8}"
            f"  是 2 的幂：{is_pow}")


# ===== 第二部分：表达式与字符串（对应 03 章）=====
# ------------------------------------------------------------
# 【题 6】格式化输出成绩单                          [难度：★☆☆]
# 要求：姓名左对齐宽 6，数字右对齐宽 6，平均分保留 1 位，得分率用 .1% 输出成 90.8% 这种形式。练点：f-string 的填充对齐 < >、浮点精度 .1f、百分比 .1%。
# ------------------------------------------------------------
def ex06_score_table(records):
    """你的实现写在这里"""
    lines = [f"{'姓名':<6}{'语文':>6}{'数学':>6}{'平均分':>8}{'得分率':>9}"]
    for name, chinese, math_score in records:
        avg = (chinese + math_score) / 2
        lines.append(f"{name:<6}{chinese:>6}{math_score:>6}{avg:>8.1f}{avg / 100:>9.1%}")
    return "\n".join(lines)

# ------------------------------------------------------------
# 【题 7】字符串反转与回文判断                     [难度：★☆☆]
# 要求：两种写法各实现一遍——(1) 切片 s[::-1] 反转后直接比较；(2) 双指针从两端向中间比对，不等立即返回 False。练点：切片步长、while 循环与双指针、函数提前返回。
# ------------------------------------------------------------
def ex07_palindrome_slice(s):
    """你的实现写在这里（切片法）"""
    return s == s[::-1]


def ex07_palindrome_two_pointers(s):
    """你的实现写在这里（双指针法）"""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# ------------------------------------------------------------
# 【题 8】统计单词出现次数                          [难度：★☆☆]
# 要求：按空白切分句子，去掉首尾标点、统一小写后统计词频，按"次数降序 + 字母升序"输出前 top_n 个单词。练点：字典累加 counts.get(k, 0) + 1、sorted 的 key 与 lambda。
# ------------------------------------------------------------
def ex08_word_count(text, top_n=5):
    """你的实现写在这里"""
    counts = {}
    for word in text.split():
        word = word.strip(".,!?;:").lower()
        if word:  # 真值测试：空字符串为假，跳过
            counts[word] = counts.get(word, 0) + 1
    top = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top_n]
    return "，".join(f"{w}×{c}" for w, c in top)

# ------------------------------------------------------------
# 【题 9】统计元音、数字、空格数量                  [难度：★☆☆]
# 要求：分别统计英文字母中的元音个数、数字字符个数、空格个数。练点：生成器表达式求和、成员运算符 in、字符串方法。
# ------------------------------------------------------------
def ex09_count_chars(s):
    """你的实现写在这里"""
    vowels = sum(1 for ch in s if ch.lower() in "aeiou")
    digits = sum(1 for ch in s if ch in "0123456789")
    spaces = sum(1 for ch in s if ch == " ")
    return f"元音 {vowels} 个，数字 {digits} 个，空格 {spaces} 个"

# ------------------------------------------------------------
# 【题 10】列表推导式生成平方表                     [难度：★☆☆]
# 要求：用列表推导式生成 1~100 的平方列表；再用带 if 过滤的推导式取出其中"偶数的平方"。练点：列表推导式 [表达式 for 变量 in 可迭代 if 条件]。
# ------------------------------------------------------------
def ex10_squares():
    """你的实现写在这里"""
    squares = [i ** 2 for i in range(1, 101)]
    even_squares = [i ** 2 for i in range(1, 101) if i % 2 == 0]
    return (f"1~100 的平方共 {len(squares)} 个，最大值 {squares[-1]}；"
            f"偶数平方共 {len(even_squares)} 个，前 5 个 {even_squares[:5]}")

# ------------------------------------------------------------
# 【题 11】列表去重且保持原顺序                     [难度：★☆☆]
# 要求：两种写法——(1) dict.fromkeys(items)：字典键唯一且保序；(2) 遍历 + set 记录已见：seen 判重、result 保序追加。练点：字典保序特性、set 的 O(1) 成员判断、not in。
# ------------------------------------------------------------
def ex11_dedupe_dict(items):
    """你的实现写在这里（dict.fromkeys 法）"""
    return list(dict.fromkeys(items))


def ex11_dedupe_set(items):
    """你的实现写在这里（set 记录法）"""
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

# ------------------------------------------------------------
# 【题 12】温度换算表                               [难度：★☆☆]
# 要求：用推导式生成 -40 到 100 华氏度的摄氏换算表（步长 20），华氏右对齐，摄氏保留 1 位小数。摄氏 = (华氏 - 32) * 5 / 9。练点：range(start, stop, step)、推导式内嵌格式化。
# ------------------------------------------------------------
def ex12_fahrenheit_table(start=-40, end=100, step=20):
    """你的实现写在这里"""
    rows = [f"{f:>6} 华氏 = {(f - 32) * 5 / 9:>7.1f} 摄氏"
            for f in range(start, end + 1, step)]
    return "\n".join(rows)


# ===== 第三部分：流程控制（对应 04 章）=====
# ------------------------------------------------------------
# 【题 13】成绩等级判定                             [难度：★☆☆]
# 要求：90/80/70/60 四个边界分别对应 A/B/C/D，其余 E；分数不在 0~100 时返回"分数不合法"。练点：if/elif 的短路顺序——先兜底非法值，再自上而下写边界，顺序写反（比如先判 60）结果就全错了。
# ------------------------------------------------------------
def ex13_grade(score):
    """你的实现写在这里"""
    if not 0 <= score <= 100:
        return "分数不合法"
    if score >= 90:
        return "A 优秀"
    elif score >= 80:
        return "B 良好"
    elif score >= 70:
        return "C 中等"
    elif score >= 60:
        return "D 及格"
    else:
        return "E 不及格"

# ------------------------------------------------------------
# 【题 14】九九乘法表                               [难度：★☆☆]
# 要求：嵌套循环输出下三角形状的九九乘法表，行末不留多余空格。练点：外层 i 控行、内层 j 控列（j <= i）、join + rstrip 收尾。
# ------------------------------------------------------------
def ex14_multiplication_table():
    """你的实现写在这里"""
    lines = []
    for i in range(1, 10):
        row = "".join(f"{j}×{i}={i * j:<4}" for j in range(1, i + 1))
        lines.append(row.rstrip())
    return "\n".join(lines)

# ------------------------------------------------------------
# 【题 15】猜数字游戏（预设猜测序列）               [难度：★☆☆]
# 要求：给定答案 target 与猜测序列 guesses（不用 input()），用 while True + break 逐次判断太大/太小，猜中或猜完即停。练点：while True 死循环 + break 跳出、索引自增、边界判断。
# ------------------------------------------------------------
def ex15_guess_number(target, guesses):
    """你的实现写在这里"""
    log = []
    i = 0
    while True:
        if i >= len(guesses):  # 猜测用完必须退出，否则死循环
            log.append(f"猜测次数已用完，答案是 {target}")
            break
        g = guesses[i]
        i += 1
        if g < target:
            log.append(f"第 {i} 次猜 {g}：太小")
        elif g > target:
            log.append(f"第 {i} 次猜 {g}：太大")
        else:
            log.append(f"第 {i} 次猜 {g}：猜对了！共 {i} 次")
            break
    return "\n".join(log)

# ------------------------------------------------------------
# 【题 16】判断素数（for-else 写法）                [难度：★☆☆]
# 要求：用 for-else 判断 n 是否为素数（n < 2 直接排除）。练点：for...else 的执行时机——循环被 break 打断则不执行 else，这里"找到因子就 break"，所以能走到 else 的一定是素数。
# ------------------------------------------------------------
def ex16_is_prime(n):
    """你的实现写在这里"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 只需试除到平方根
        if n % i == 0:
            break  # 找到因子，不是素数
    else:
        return True  # 循环完整跑完、没被 break -> 素数
    return False

# ------------------------------------------------------------
# 【题 17】打印 100 以内所有素数                    [难度：★☆☆]
# 要求：两种实现——(1) 试除法：对每个 n 试除到 sqrt(n)，配合 for-else；(2) 埃拉托斯特尼筛法：布尔表标记合数，从 i*i 起划掉倍数。练点：嵌套循环、布尔列表、以及"用空间换时间"的算法直觉。
# ------------------------------------------------------------
def ex17_primes_by_trial(limit=100):
    """你的实现写在这里（试除法）"""
    result = []
    for n in range(2, limit + 1):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            result.append(n)
    return result


def ex17_primes_by_sieve(limit=100):
    """你的实现写在这里（筛法）"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):  # 从 i*i 起划掉倍数
                is_prime[j] = False
    return [n for n in range(2, limit + 1) if is_prime[n]]

# ------------------------------------------------------------
# 【题 18】斐波那契数列前 n 项                      [难度：★☆☆]
# 要求：两版实现——(1) while 循环版：a, b = b, a + b 滚动前进；(2) 生成器函数版：yield 每次产出下一项，用 next() 取值。练点：多重赋值滚动、生成器 yield 的惰性求值、next()。
# ------------------------------------------------------------
def ex18_fib_while(n):
    """你的实现写在这里（while 版）"""
    seq = []
    a, b = 0, 1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq


def ex18_fib_generator(n):
    """你的实现写在这里（生成器版）"""
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    gen = fib()
    return [next(gen) for _ in range(n)]

# ------------------------------------------------------------
# 【题 19】辗转相除法求最大公约数与最小公倍数       [难度：★☆☆]
# 要求：用 while 实现欧几里得算法，并据此求最小公倍数。公式：反复做 a, b = b, a % b 直到 b 为 0，此时 a 即 gcd；lcm = |a * b| // gcd。练点：while 的多重赋值、abs、以及"先算 gcd 再复用求 lcm"。
# ------------------------------------------------------------
def ex19_gcd_lcm(a, b):
    """你的实现写在这里"""
    x, y = abs(a), abs(b)
    while y:  # y 为 0 时退出，此时 x 就是最大公约数
        x, y = y, x % y
    gcd = x
    lcm = 0 if gcd == 0 else abs(a * b) // gcd
    return f"gcd({a}, {b}) = {gcd}，lcm({a}, {b}) = {lcm}"

# ------------------------------------------------------------
# 【题 20】打印菱形图案                             [难度：★★★]
# 要求：给定半高 n，用嵌套循环打印上下对称的菱形（本题 n = 4）：
#           *        第1行 3空格1星    ***       第2行 2空格3星
#         *****      第3行 1空格5星   *******    第4行 0空格7星（中间最长行）
#           *        第7行与第1行对称，第5、6行同第3、2行
# 提示：空格数 = n - i，星号数 = 2 * i - 1（奇数序列）；
#       下半部分把 i 从 n-1 递减到 1，公式完全一样。
# 练的是：嵌套循环、空格与星号的数量关系、range 倒序遍历。
# ------------------------------------------------------------
def ex20_diamond(n=4):
    """你的实现写在这里"""
    lines = []
    for i in range(1, n + 1):  # 上半部分（含中间最长行）
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):  # 下半部分，行序倒过来
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    return "\n".join(lines)


# ===== 第四部分：函数（对应 05 章）=====
# ------------------------------------------------------------
# 【题 21】任意数量参数统计                         [难度：★★☆]
# 要求：用 *args 接收任意个数字，返回个数、总和、最大值、最小值；不传参数时给出友好提示。练点：可变位置参数 *args（打包成元组）、空元组的真值判断。
# ------------------------------------------------------------
def ex21_stats(*args):
    """你的实现写在这里"""
    if not args:  # 空元组为假
        return "没有传入任何参数"
    return (f"个数 = {len(args)}，和 = {sum(args)}，"
            f"最大值 = {max(args)}，最小值 = {min(args)}")

# ------------------------------------------------------------
# 【题 22】字典形式的个人信息输出                   [难度：★★☆]
# 要求：用 **kwargs 接收任意键值对，按指定顺序优先输出，未列出的键追加在后面，每个字段缩进两空格。练点：可变关键字参数 **kwargs（打包成字典）、字典的 in 判断。
# ------------------------------------------------------------
def ex22_profile(**kwargs):
    """你的实现写在这里"""
    order = ["姓名", "年龄", "城市", "职业"]
    ordered_keys = [k for k in order if k in kwargs]
    ordered_keys += [k for k in kwargs if k not in order]
    body = "\n".join(f"  {k}：{kwargs[k]}" for k in ordered_keys)
    return "个人信息卡片：\n" + body

# ------------------------------------------------------------
# 【题 23】递归实现阶乘与列表求和                   [难度：★★☆]
# 要求：两版递归——(1) factorial(n)：n <= 1 返回 1，否则 n * factorial(n - 1)；(2) sum_list(items)：空列表返回 0，否则首元素 + 剩余部分递归。练点：递归的"基准情形 + 递归情形"缺一不可，否则栈溢出。
# ------------------------------------------------------------
def ex23_factorial(n):
    """你的实现写在这里"""
    if n < 0:
        raise ValueError("阶乘的入参不能为负数")
    if n <= 1:  # 基准情形（终止条件）
        return 1
    return n * ex23_factorial(n - 1)


def ex23_sum_list(items):
    """你的实现写在这里"""
    if not items:  # 基准情形：空列表和为 0
        return 0
    return items[0] + ex23_sum_list(items[1:])

# ------------------------------------------------------------
# 【题 24】带默认参数与仅关键字参数的打招呼函数      [难度：★★☆]
# 要求：写 greet(name, *, greeting="你好", punctuation="！")，调用时用关键字覆盖 greeting 与 punctuation。练点：默认参数的求值时机、用 * 分隔出的"仅关键字参数"。
# ------------------------------------------------------------
def ex24_greet(name, *, greeting="你好", punctuation="！"):
    """你的实现写在这里"""
    return f"{greeting}，{name}{punctuation}"

# ------------------------------------------------------------
# 【题 25】闭包计数器                               [难度：★★☆]
# 要求：make_counter() 返回一个计数器函数，每次调用自增 1 并返回新值；两个计数器互不干扰，各自持有独立的 count 变量。练点：闭包捕获外层变量、nonlocal 声明"我要改的是外层变量"。
# ------------------------------------------------------------
def ex25_make_counter(start=0):
    """你的实现写在这里"""
    count = start

    def counter():
        nonlocal count  # 不加这行会报 UnboundLocalError
        count += 1
        return count

    return counter

# ------------------------------------------------------------
# 【题 26】调用日志装饰器                           [难度：★★☆]
# 要求：实现 log_calls 装饰器，被装饰函数每次调用时打印函数名与参数，并打印返回值；用 functools.wraps 保留原函数元信息。练点：装饰器 = 接收函数、返回函数；*args/**kwargs 透传；忘了 return result，返回值就会变成 None。
# ------------------------------------------------------------
def log_calls(func):
    """你的实现写在这里"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [log_calls] 调用 {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"  [log_calls] {func.__name__} 返回 {result!r}")
        return result

    return wrapper


@log_calls
def ex26_add_all(*numbers):
    """被装饰的函数：任意个数字求和。"""
    return sum(numbers)


# ===== 参考答案（折叠查看）=====
"""【参考答案：关键思路 / 另一种写法】
题 1  面积 πr²、周长 2πr；round(x, 2) 返回数值本身，f-string 的 .2f 才是显示层控制。
题 2  总秒数 // 3600 得小时，余数 // 60 得分钟，最后 % 60 得秒；0 秒也要正常输出。
题 3  a, b = b, a 先把右侧打包成元组再解包，所以不需要临时变量。
题 4  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0；and 优先级高于 or，建议加括号。
题 5  2 的幂二进制只有一个 1，n & (n-1) 会抹掉最低位的 1，结果 0 且 n > 0 即可。
题 6  {值:填充符对齐符宽度}，如 {name:<6}、{x:>8.1f}，百分比用 {x:.1%}；中文占 2 个字符宽度，列宽要放宽。
题 7  切片法 O(n) 但复制整个字符串；双指针法遇到第一个不同即返回，长文本更省内存。
题 8  counts.get(word, 0) + 1 是字典计数通用套路；等价写法 collections.Counter().most_common()。
题 9  三个计数写成生成器表达式求和最简洁；元音判断 in "aeiou" 配合 .lower() 兼容大小写。
题 10 [i ** 2 for i in range(1, 101) if i % 2 == 0] 等价于 [i ** 2 for i in range(2, 101, 2)]。
题 11 dict.fromkeys(items) 利用"字典 3.7+ 保序 + 键唯一"一行搞定；set 版可读性更好。
题 12 range(-40, 101, 20) 上界要 +1 才含 100；-40 华氏正好等于 -40 摄氏，可当校验点。
题 13 elif 自上而下短路，边界必须从高到低写；先用 not 0 <= score <= 100 兜底非法输入。
题 14 外层 i 是行号、内层 j 只到 i，所以是下三角；"".join 拼一行比 print(end=...) 干净。
题 15 while True + break 是"至少执行一次"的标准写法；务必在"猜测耗尽"分支里 break，否则死循环。
题 16 for...else 的 else 只在循环正常结束时执行；试除上界到 int(sqrt(n)) 即可，因子成对出现。
题 17 筛法：先假设全为素数，从 2 起把 i 的倍数（从 i*i 开始）标记为合数，最后留下仍为 True 的下标，复杂度 O(n log log n)。
题 18 while 版用 a, b = b, a + b 滚动；生成器是惰性的：调用 fib() 并不执行，next() 才推进一次，取前 n 项更省内存。
题 19 辗转相除法：while y: x, y = y, x % y，结束时 x 即 gcd；lcm = |a*b| // gcd，先除后乘可避免大数。
题 20（★★★ 思路拆解）
      ① 把图形按中间最长那行切成上下两半，先只画上半部分。
      ② 找规律（n = 4）：第 1 行 3 空格 1 星，第 2 行 2 空格 3 星，第 3 行 1 空格 5 星，第 4 行 0 空格 7 星；
         归纳得第 i 行：空格 = n - i，星号 = 2 * i - 1（星号是 1,3,5,7 的奇数序列）。
      ③ 上半 for i in range(1, n+1) 输出 " " * (n-i) + "*" * (2*i-1)；下半复用同一公式、行序倒过来。
      ④ 左右不对称时先怀疑空格公式写反（常见错误：i-1、n-2i、忘乘 2）；也可先算好每行的空格/星号数再统一打印。
题 21 函数内 args 是元组，空元组为假，用 if not args 兜底；也可写成 def f(name, *args) 混用固定参数。
题 22 kwargs 是字典；输出顺序可用 order 列表控制。调用侧键名不能数字开头，如 profile(姓名="小明")。
题 23 递归两要素：基准情形（n <= 1 / 空列表）与向基准收敛的调用（n-1 / items[1:]），缺一即 RecursionError。
题 24 * 之后的参数只能用关键字传，能防止位置写错；默认参数只求值一次，别用 [] 这类可变对象。
题 25 nonlocal count 声明要改的是外层变量，否则会抛 UnboundLocalError；每次 make_counter() 都新建一份 count，两个计数器互不干扰。
题 26 wrapper 用 *args/**kwargs 原样透传，且必须 return result；@functools.wraps 复制 __name__/__doc__，否则会变成 "wrapper"。
"""


# ===== 主程序：集中调用并打印结果 =====
if __name__ == "__main__":
    print("=" * 60); print("第一部分：变量与运算符（对应 01、02 章）"); print("=" * 60)
    print(f"【题1】{ex01_circle(2)}")
    print(f"【题2】{ex02_hms(0)} ｜ {ex02_hms(3661)}")
    print(f"【题3】{ex03_swap(1, 2)}")
    print(f"【题4】2000->{ex04_is_leap(2000)}，1900->{ex04_is_leap(1900)}，2024->{ex04_is_leap(2024)}")
    print(f"【题5】{ex05_power_of_two(64)}")
    print(f"【题5】{ex05_power_of_two(48)}")
    print("-" * 60); print("第二部分：表达式与字符串（对应 03 章）"); print("-" * 60)
    print("【题6】成绩单")
    print(ex06_score_table([("小明", 88, 93.5), ("小红", 95, 89), ("阿强", 59, 66.5)]))
    print(f"【题7】level 切片{ex07_palindrome_slice('level')}/双指针{ex07_palindrome_two_pointers('level')}；"
          f"python 切片{ex07_palindrome_slice('python')}/双指针{ex07_palindrome_two_pointers('python')}")
    print(f"【题8】词频 Top5：{ex08_word_count('the quick brown fox jumps over the lazy dog the fox')}")
    print(f"【题9】{ex09_count_chars('Hello Python 2026, ok!')}")
    print(f"【题10】{ex10_squares()}")
    data = [3, 1, 2, 3, 5, 1, 4, 2, 6]
    print(f"【题11】原列表 {data} -> dict法 {ex11_dedupe_dict(data)}，set法 {ex11_dedupe_set(data)}")
    print("【题12】华氏 -> 摄氏换算表（-40 ~ 100，步长 20）")
    print(ex12_fahrenheit_table())
    print("=" * 60); print("第三部分：流程控制（对应 04 章）"); print("=" * 60)
    print("【题13】成绩等级：" + "，".join(f"{s}分->{ex13_grade(s)}" for s in (95, 90, 85, 72, 60, 59, 120)))
    print("【题14】九九乘法表\n" + ex14_multiplication_table())
    print("【题15】猜数字（答案 42，序列 [50, 25, 42]）")
    print(ex15_guess_number(42, [50, 25, 42]))
    print("【题15】猜数字（答案 42，序列 [10, 20]，猜不完）")
    print(ex15_guess_number(42, [10, 20]))
    print(f"【题16】17 素数{ex16_is_prime(17)}，91 素数{ex16_is_prime(91)}，1 素数{ex16_is_prime(1)}")
    print(f"【题17】试除法 {ex17_primes_by_trial(100)}")
    print(f"【题17】筛  法 {ex17_primes_by_sieve(100)}")
    print(f"【题17】两种实现结果一致：{ex17_primes_by_trial(100) == ex17_primes_by_sieve(100)}")
    print(f"【题18】while 版前 10 项 {ex18_fib_while(10)}")
    print(f"【题18】生成器版前 10 项 {ex18_fib_generator(10)}")
    print(f"【题19】{ex19_gcd_lcm(48, 18)}；{ex19_gcd_lcm(17, 5)}")
    print("【题20】菱形图案（半高 4）\n" + ex20_diamond(4))
    print("-" * 60); print("第四部分：函数（对应 05 章）"); print("-" * 60)
    print(f"【题21】{ex21_stats(3, 1, 4, 1, 5, 9, 2, 6)}")
    print(f"【题21】{ex21_stats()}")
    print("【题22】" + ex22_profile(姓名="小明", 年龄=18, 城市="杭州", 职业="学生", 爱好="编程"))
    print(f"【题23】5! = {ex23_factorial(5)}，[1,2,3,4,5] 求和 = {ex23_sum_list([1, 2, 3, 4, 5])}")
    print(f"【题24】{ex24_greet('小明')} ｜ {ex24_greet('Bob', greeting='Hi', punctuation='!')}")
    c1, c2 = ex25_make_counter(), ex25_make_counter(start=100)
    print(f"【题25】c1：{c1()}, {c1()}, {c1()} ｜ c2：{c2()}, {c2()}（互不干扰）")
    print("【题26】调用被 @log_calls 装饰的函数：")
    print(f"【题26】返回值 = {ex26_add_all(1, 2, 3, 4)}，函数名 = {ex26_add_all.__name__}")
    print("=" * 60); print("全部 26 题运行结束，无异常。"); print("=" * 60)
