# -*- coding: utf-8 -*-
"""
第五章：函数（Python 基础语法）

【本章学什么】
1. 为什么要有函数：复用、抽象、可测试，以及 DRY 原则。
2. def 定义与调用；函数名也是变量；函数是"一等对象"（可赋值、可进列表、可当参数、可当返回值）。
3. 参数：位置实参、关键字实参、默认值参数；*args / **kwargs；调用时拆包；仅关键字 / 仅位置参数。
4. 返回值语义（没 return 就是 None，返回多个值其实是 tuple）；用卫语句提前 return。
5. docstring 与函数属性、类型注解、作用域 LEGB、global / nonlocal、闭包。
6. 递归与记忆化、装饰器入门、map / filter / reduce / sorted / functools.partial。

【怎么运行】VS Code 里点右上角运行按钮或按 Ctrl+F5 整体运行；也可选中某一小节，右键 →
"在 Python 终端中运行所选内容"逐段看结果。全程没有 input()，不会卡住等输入，没有文件
读写、没有网络、没有死循环；递归爆栈那段用 try/except RecursionError 接住了，不会崩。

【会看到什么】每节用 print("=" * 60) 开头、print("-" * 60) 结尾；大量 f-string 直接打印
结果，注释解释"为什么是这个结果"；带 "# ⚠️ 坑：" 的行是最容易踩的坑；末尾 8 道动手练习，
参考答案放在最后一个字符串里，不影响运行。建议把关键行改一改再跑一遍。
"""

import functools
import itertools
import math
import sys
import time
from functools import partial, reduce
from typing import List, Optional, Union

# ============================================================
# 1. 为什么要有函数：复用 / 抽象 / 可测试
# ============================================================
print("=" * 60, "1. 为什么要有函数", sep="\n")
# 圆面积要算三次，复制粘贴三遍？公式一改就得改三处，漏改一处就是隐藏 bug。
# DRY（Don't Repeat Yourself）= 同一份知识只写一遍。函数还带来"抽象"（调用方只管给
# 输入、拿输出）和"可测试"（输入输出确定，就能单独写测试验证它对不对）。
def circle_area(radius):
    """返回圆面积。"""
    return math.pi * radius ** 2
print(f"  circle_area(1) = {circle_area(1):.2f}，circle_area(2) = {circle_area(2):.2f}")
print(f"关键结果：多次调用共用一份逻辑，改公式只需改函数体一处")
print("-" * 60)

# ============================================================
# 2. def 与调用：函数名也是变量，函数是"一等对象"
# ============================================================
print("=" * 60, "2. def 与调用：函数是一等对象", sep="\n")
def greet(name):
    """返回一句问候。"""
    return f"你好，{name}！"
def apply_twice(func, value):          # ② 函数能当参数传（接收函数的函数叫高阶函数）
    return func(func(value))
def make_adder(n):                     # ③ 函数能当返回值（闭包与装饰器的地基）
    return lambda x: x + n
print(f"  greet('小明') = {greet('小明')}；type(greet) = {type(greet).__name__}")
sayer = greet                          # 函数名就是变量，赋给新名字（写括号就成了"调用"）
ops = [greet, str.upper, len]          # ① 函数能放进列表
print(f"  ①列表 {ops[0]('小刚')} / {ops[1]('abc')} / {ops[2]('abcd')}；greet is sayer → {greet is sayer}")
print(f"  ②当参数 {apply_twice(str.strip, '  hi  ')!r}；③当返回值 {make_adder(10)(5)}")
print(f"关键结果：函数不是特殊语法，它是一堆能被赋值、传递的普通对象")
print("-" * 60)

# ============================================================
# 3. 参数四种形态：位置实参 / 关键字实参 / 默认值
# ============================================================
print("=" * 60, "3. 位置实参 / 关键字实参 / 默认值", sep="\n")
def order(dish, size="中杯", sugar="正常糖"):
    """点单：菜品必填，杯型和糖度有默认值。"""
    return f"{size}{dish}（{sugar}）"
def power(base, exp=2):
    return base ** exp
print(f"  全用默认值 {order('奶茶')}；位置实参 {order('奶茶', '大杯')}")
print(f"  关键字跳过中间 {order('奶茶', sugar='少糖')}；顺序随意 {order(size='小杯', dish='咖啡')}")
print(f"  power(3) = {power(3)}，power(3, 4) = {power(3, 4)}")
# ⚠️ 坑：混用时位置实参必须写在关键字实参前面，否则 SyntaxError：
#   order(size='小杯', '咖啡')  → positional argument follows keyword argument
# ⚠️ 坑：默认值在"函数定义时"求值一次，不是每次调用都重算——对数字没事，
#         对 list / dict 就是灾难（第 14 节专讲）。
print(f"关键结果：默认值让常用调用更短，关键字实参让意图更清楚")
print("-" * 60)

# ============================================================
# 4. *args 与 **kwargs：数量不定的参数
# ============================================================
print("=" * 60, "4. *args 与 **kwargs", sep="\n")
def total(*args):
    """收任意多个位置实参：args 是 tuple。"""
    print(f"  args 类型 = {type(args).__name__}，值 = {args}")
    return sum(args)
def profile(name, **kwargs):
    """收任意多个关键字实参：kwargs 是 dict。"""
    print(f"  kwargs 类型 = {type(kwargs).__name__}，值 = {kwargs}")
    return f"{name}: " + "，".join(f"{k}={v}" for k, v in kwargs.items())
def everything(a, b=2, *args, **kwargs):
    return f"a={a}, b={b}, args={args}, kwargs={kwargs}"
print(f"  total(1, 2, 3) = {total(1, 2, 3)}，一个都不传 total() = {total()}")
print(f"  {profile('小明', age=18, city='北京')}；{profile('小红')}")
print(f"  everything(1, 3, 5, 7, x=9) = {everything(1, 3, 5, 7, x=9)}")
# 参数定义的顺序规则（从左到右）：
#   位置参数 → *args → 默认值参数 → 仅关键字参数 → **kwargs
# ⚠️ 坑：*args 会把"多余的"位置实参全吃掉，所以写在它后面的参数没法再用位置传，
#         只能变成"仅关键字参数"（见第 6 节）。
print(f"关键结果：*args 收成 tuple，**kwargs 收成 dict")
print("-" * 60)

# ============================================================
# 5. 调用时拆包：f(*lst) 与 f(**dic) 为什么要用
# ============================================================
print("=" * 60, "5. 调用时拆包：f(*lst) 与 f(**dic)", sep="\n")
def box(x, y, z):
    """拼三位数：box(1, 2, 3) → 123。"""
    return x * 100 + y * 10 + z
nums = [1, 2, 3]
info = {"x": 4, "y": 5, "z": 6}
print(f"  box(*nums) = {box(*nums)}（等价 box(1, 2, 3)）；box(**info) = {box(**info)}（等价 box(x=4,y=5,z=6)）")
# 为什么需要：参数常常已经装在容器里（从别处算好的一行数据）。不拆包就得手写
# box(nums[0], nums[1], nums[2])，容器长度一变就得改代码。它也是"参数转发"的标准写法：
# 装饰器里的 wrapper(*args, **kwargs) 就是把收到的参数原样传下去。
# ⚠️ 坑：**dic 的键必须是字符串，且要和形参名一一对应，否则 TypeError。
print("  用 * 把列表摊平成多个参数：", end="")
print(*nums, sep=" -> ")
print(f"关键结果：拆包让你不必关心容器里到底有几个元素")
print("-" * 60)

# ============================================================
# 6. 仅关键字参数（*）与仅位置参数（/）
# ============================================================
print("=" * 60, "6. 仅关键字参数（*）与仅位置参数（/）", sep="\n")
def power_kw(base, *, exp=2):
    """exp 写在 * 之后 → 只能靠关键字传。"""
    return base ** exp
def tag(name, /, text):
    """name 写在 / 之前 → 只能靠位置传；text 两种都行。"""
    return f"<{name}>{text}</{name}>"
print(f"  power_kw(3, exp=3) = {power_kw(3, exp=3)}；tag('b', '粗体') = {tag('b', '粗体')}；tag('b', text='也行') = {tag('b', text='也行')}")
print(f"  len([1, 2, 3]) = {len([1, 2, 3])}，sorted([2, 1]) = {sorted([2, 1])}")
# ⚠️ 坑：power_kw(3, 3) 和 tag(name='b', text='x') 都会 TypeError。
#   为什么这样设计：sorted(..., key=, reverse=) 这类"选项"参数写成关键字后，读代码的人
#   一眼知道谁是谁；而内置 len(obj)、sorted(iterable) 的内部参数名属于实现细节，官方故意
#   不让你用关键字传，将来改内部名字也不会破坏你的代码。
print(f"关键结果：* 之后只能关键字传，/ 之前只能位置传")
print("-" * 60)

# ============================================================
# 7. 返回值：return 的语义与"返回多个值"的真相
# ============================================================
print("=" * 60, "7. 返回值：没 return 就是 None", sep="\n")
def no_return(x):
    x + 1                              # 算了个寂寞：没写 return，结果就丢了
def min_max(nums):
    """看着像"返回两个值"。"""
    return min(nums), max(nums)
def check(x):
    if x < 0:
        return "负数"                   # 提前结束，后面的语句不跑
    return "非负"
packed = min_max([3, 1, 4, 1, 5])
low, high = min_max([3, 1, 4, 1, 5])   # 元组解包接收
print(f"  忘了写 return，拿到的是 {no_return(1)!r}；check(-1)={check(-1)}，check(0)={check(0)}")
print(f"  packed = {packed}，type = {type(packed).__name__}  ← 其实是一个 tuple！解包后 low={low}, high={high}")
# ⚠️ 坑：return 之后的语句是死代码；只写 return（或不写值）等于 return None。
print(f"关键结果：没写 return 得到 None；多个返回值本质是一个元组")
print("-" * 60)

# ============================================================
# 8. 提前 return（卫语句）：把深层嵌套压平
# ============================================================
print("=" * 60, "8. 提前 return（卫语句）压平嵌套", sep="\n")
def price_bad(user, coupon, stock):
    """反面教材：一层套一层，缩进越来越深。"""
    if user is None:
        return -4
    else:
        if not user.get("vip"):
            return -3
        else:
            if coupon is None:
                return -2
            else:
                return 80 if stock > 0 else -1
def price_good(user, coupon, stock):
    """卫语句：先把各种不合格挡在门口，主逻辑留在最后，只缩进一层。"""
    if user is None:
        return -4
    if not user.get("vip"):
        return -3
    if coupon is None:
        return -2
    if stock <= 0:
        return -1
    return 80
vip = {"vip": True}
print(f"  两种写法结果一致：{price_bad(vip, 'C1', 5)} == {price_good(vip, 'C1', 5)}")
print(f"  无货 {price_good(vip, 'C1', 0)}；非会员 {price_good({'vip': False}, 'C1', 5)}；无用户 {price_good(None, 'C1', 5)}")
print(f"关键结果：卫语句把异常分支前置，主流程不再被 if 埋住")
print("-" * 60)

# ============================================================
# 9. 文档字符串 docstring 与函数属性
# ============================================================
print("=" * 60, "9. docstring 与函数属性", sep="\n")
def div(a, b):
    """做除法并返回浮点结果。

    参数: a 是被除数，b 是除数（不能为 0）。
    返回: a / b 的结果。
    抛错: b 为 0 时抛 ZeroDivisionError。
    """
    return a / b
def with_default(a, b=10):
    """带默认值的函数。"""
    return a + b
print(f"  div.__doc__ 第一行 = {div.__doc__.strip().splitlines()[0]}")
print(f"  div.__name__ = {div.__name__!r}，div.__defaults__ = {div.__defaults__}")
print(f"  with_default.__defaults__ = {with_default.__defaults__}；__annotations__ = {with_default.__annotations__}")
# 在 VS Code 里取消注释单独运行下面这行，会打印排版好的完整文档：help(with_default)
# ⚠️ 坑：docstring 必须紧跟在 def 那一行下面、中间不夹别的语句，
#         否则它只是一段被丢弃的字符串，__doc__ 会是 None。
print(f"关键结果：__doc__ / __name__ / __defaults__ 都是能读到的真实属性")
print("-" * 60)

# ============================================================
# 10. 类型注解：写给人和工具看的，运行时不做强制
# ============================================================
print("=" * 60, "10. 类型注解不做运行时检查", sep="\n")
def average(nums: List[float]) -> float:
    """求平均值。nums 应当是数字列表。"""
    return sum(nums) / len(nums)
def find(name: str, table: dict) -> Optional[str]:
    """查表；查不到返回 None，所以返回类型是 Optional[str]（= Union[str, None]）。"""
    return table.get(name)
def fmt(value: Union[int, str]) -> str:
    """Union 示例：只接受 int 或 str。"""
    return f"<{value}>"
def scale(value: float, factor: float) -> float:
    """按倍数放大：注解说了只收数字。"""
    return value * factor
print(f"  average([1, 2, 3]) = {average([1, 2, 3])}")
print(f"  average.__annotations__ = {average.__annotations__}")
print(f"  find('a', ...) = {find('a', {'a': 'A'})}，find('z', ...) = {find('z', {})}；fmt(1) = {fmt(1)}")
# ⚠️ 坑：注解在运行时"完全不做检查"：下面传了字符串，Python 照样跑出结果，还"看起来
#         没错"——这类错误只有 mypy / pyright 这类静态检查工具能抓。
print(f"  传字符串也不报错：scale('ab', 3) = {scale('ab', 3)!r}")
print(f"关键结果：类型注解 = 文档 + 编辑器提示 + 静态检查，不是运行时校验")
print("-" * 60)

# ============================================================
# 11. 作用域 LEGB：Local → Enclosing → Global → Builtins
# ============================================================
print("=" * 60, "11. 作用域 LEGB", sep="\n")
name = "全局 name"
length = 3
def outer():
    name = "Enclosing（外层函数）name"
    def inner():
        return f"inner 看到的是：{name}"     # Local 没有 → 去 Enclosing 找
    return inner()
def use_builtin():
    # Local 没有 len，Enclosing / Global 也没有，最后在 Builtins 里找到内置 len
    return len("hello")
def shadow_builtin():
    # ⚠️ 坑：函数里给 list 赋值，list 就成了局部名，内置 list 被遮蔽：
    # print(list(range(3)))          # UnboundLocalError: cannot access local variable 'list'
    list = [1, 2, 3]
    return list
def shadow_global():
    # ⚠️ 坑：同理，函数里给 length 赋值后，读 length 也只能读局部那个：
    # print(length)                  # UnboundLocalError: cannot access local variable
    length = 100                     # 这一行让 length 被判为局部名
    return length
print(f"  outer() → {outer()}；模块级 name = {name}（模块顶层就是 Global）；use_builtin() = {use_builtin()}")
print(f"  shadow_builtin() = {shadow_builtin()}，函数外 list 仍可用：{list('ab')}")
print(f"  shadow_global() = {shadow_global()}，函数外的 length 仍是 {length}")
# 记忆点：Python 在编译期就决定名字是局部还是全局——只要函数体里出现过赋值，它就是
# 局部的，跟全局那个同名变量再无关系。UnboundLocalError 就是这么来的。
print(f"关键结果：查找顺序 L → E → G → B；有赋值就是局部名")
print("-" * 60)

# ============================================================
# 12. global 与 nonlocal：能不用就不用
# ============================================================
print("=" * 60, "12. global 与 nonlocal", sep="\n")
counter_global = 0
def bump_global():
    """global 声明：我要改的是模块级那个 counter_global。"""
    global counter_global
    counter_global += 1
def make_counter_basic():
    count = 0
    def step():
        nonlocal count                # 声明：改的是外层函数的 count，不是新建一个
        count += 1
        return count
    return step
bump_global()
bump_global()
c = make_counter_basic()
print(f"  bump_global 调 2 次后 counter_global = {counter_global}；nonlocal 计数器：{c()} → {c()} → {c()}")
# ⚠️ 坑：global / nonlocal 让"到底是谁改了状态"难以追踪，测试也难写，多线程更危险。
#         能用参数传入、返回值传出，就别去改外部变量。
# ⚠️ 坑：nonlocal 找不到外层同名变量时直接 SyntaxError；global 只在"赋值"时必要，
#         只读全局变量时加不加都行。
print(f"关键结果：global 改模块级，nonlocal 改外层函数级，都是共享状态的信号")
print("-" * 60)

# ============================================================
# 13. 闭包：函数记住了它出生时的环境
# ============================================================
print("=" * 60, "13. 闭包：函数记住了外部变量", sep="\n")
def counter_factory(start=0):
    """计数器工厂：每调用一次，返回一个独立的计数器函数。"""
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
c1 = counter_factory()
c2 = counter_factory(100)
print(f"  c1：{c1()}，{c1()}，{c1()}；c2：{c2()}，{c2()}  ← 两个计数器互不干扰")
print(f"  c1.__closure__ = {c1.__closure__}")
print(f"  里面那个 cell 现在装的值 = {c1.__closure__[0].cell_contents}")
callbacks = [lambda: i for i in range(3)]
callbacks_fixed = [lambda i=i: i for i in range(3)]    # 用默认值"当场拍照"
# ⚠️ 坑：闭包记住的是"变量本身"而不是当时的值，所以循环里创建闭包会"晚绑定"。
print(f"  晚绑定：{[f() for f in callbacks]}  ← 全是 2，不是 0 1 2；修好后：{[f() for f in callbacks_fixed]}")
print(f"关键结果：闭包 = 函数 + 它捕获的外部变量；变量是共享的，不是快照")
print("-" * 60)

# ============================================================
# 14. 大坑：可变默认参数只在定义时求值一次
# ============================================================
print("=" * 60, "14. 可变默认参数的大坑", sep="\n")
def add_item_wrong(item, basket=[]):
    """错误示范：默认值是空列表。"""
    basket.append(item)
    return basket
def add_item_ok(item, basket=None):
    """正确写法：用 None 当哨兵，进函数后再新建列表。"""
    if basket is None:
        basket = []
    basket.append(item)
    return basket
print(f"  第一次调用：{add_item_wrong('苹果')}；第二次调用：{add_item_wrong('香蕉')}  ← 上次的苹果还在！！")
# 原因：默认值对象在 def 执行的那一刻只创建一次，之后每次调用都复用同一个列表。
print(f"  证据：add_item_wrong.__defaults__ = {add_item_wrong.__defaults__}")
print(f"  用 None 哨兵后：{add_item_ok('苹果')}、{add_item_ok('香蕉')}  ← 干净了")
# ⚠️ 坑：不可变默认值（数字、字符串、元组、None）没这个问题，
#         只有 list / dict / set 这种可变对象才会"越攒越多"。
print(f"关键结果：可变默认参数一律改成 None 哨兵，这是最经典的 Python 坑")
print("-" * 60)

# ============================================================
# 15. lambda：只写一个表达式的匿名函数
# ============================================================
print("=" * 60, "15. lambda 与 def 的取舍", sep="\n")
square = lambda x: x * x
pairs = [("苹果", 5), ("香蕉", 2), ("橙子", 8)]
print(f"  square(5) = {square(5)}，__name__ = {square.__name__!r}")
print(f"  按价格排：{sorted(pairs, key=lambda p: p[1])}")
print(f"  按价格倒序：{sorted(pairs, key=lambda p: p[1], reverse=True)}")
# 什么时候用：规则很短、只用一次，尤其是"当参数塞进去"的时候。
# ⚠️ 坑：lambda 只能写一个表达式，不能写语句（不能赋值、没有 if/else 块，只有三元表达式）。
# ⚠️ 坑：给 lambda 起名字（square = lambda ...）不推荐——报错时只显示 <lambda>，没有
#         函数名，排查很痛苦；规范上这种都该写成 def。
print(f"关键结果：lambda = 一次性小规则；逻辑一复杂就该用 def")
print("-" * 60)

# ============================================================
# 16. 递归：函数自己调用自己
# ============================================================
print("=" * 60, "16. 递归与终止条件", sep="\n")
def factorial(n):
    """n 的阶乘。终止条件：n <= 1 时直接返回 1，不再往下递归。"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
def fib(n):
    """斐波那契第 n 项（朴素递归版，效率很差，第 17 节优化）。"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
def fib_iter(n):
    """迭代版：结果一样，但不堆栈。"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def no_base_case(n):
    # ⚠️ 坑：忘了写终止条件，递归永远不回头。
    return no_base_case(n + 1)
print(f"  5! = {factorial(5)}；fib(10) = {fib(10)}；迭代版 fib(30) = {fib_iter(30)}")
print(f"  sys.getrecursionlimit() = {sys.getrecursionlimit()}  ← 默认最大递归深度")
try:
    no_base_case(0)
except RecursionError as e:
    print(f"  忘记终止条件 → 捕获到 RecursionError：{e}")
print("  程序没崩，继续往下跑——这就是要用 try/except 接住它的原因。")
# 递归 vs 迭代：递归贴合数学定义、代码短，但有栈深度上限、调用开销大；累加/遍历这类
# 能用循环表达的优先用循环；树和图这种天然分叉的问题递归更清晰。
print(f"关键结果：递归必须有终止条件，否则 RecursionError")
print("-" * 60)

# ============================================================
# 17. 用 functools.lru_cache 做记忆化，把递归提速
# ============================================================
print("=" * 60, "17. lru_cache 记忆化优化递归", sep="\n")
@functools.lru_cache(maxsize=None)      # 缓存所有算过的 "参数 → 结果"
def fib_fast(n):
    """带缓存的斐波那契。"""
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)
t0 = time.perf_counter()
r_slow = fib(30)
t1 = time.perf_counter()
r_fast = fib_fast(30)
t2 = time.perf_counter()
print(f"  朴素递归 fib(30) = {r_slow}，耗时 {t1 - t0:.4f} 秒")
print(f"  记忆化 fib(30)  = {r_fast}，耗时 {t2 - t1:.6f} 秒")
print(f"  缓存统计：{fib_fast.cache_info()}")
# 原理：把"参数 → 结果"存进一张表，同样的参数第二次直接查表，不再重算。朴素递归算
# fib(30) 要调用几百万次，缓存后只算几十次，复杂度从指数级降到线性。
# ⚠️ 坑：lru_cache 要求参数可哈希（不能传 list / dict 当参数），否则 TypeError。
print(f"关键结果：记忆化 = 拿一点内存换巨大的时间，参数必须可哈希")
print("-" * 60)

# ============================================================
# 18. 装饰器入门：接收函数、返回函数
# ============================================================
print("=" * 60, "18. 装饰器入门", sep="\n")
def timeit(func):
    """计时装饰器。本质就是：接收一个函数，返回一个新的函数。"""
    @functools.wraps(func)              # 把原函数的 __name__ / __doc__ 复制到 wrapper 上
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)   # 原样转发参数，去调用原函数
        print(f"  [timeit] {func.__name__} 耗时 {(time.perf_counter() - start) * 1000:.3f} 毫秒")
        return result
    return wrapper
@timeit                                 # 这一行的意思就是：slow_sum = timeit(slow_sum)
def slow_sum(n):
    """求 0..n-1 的和。"""
    return sum(range(n))
def repeat(times):
    """带参数的装饰器：repeat(3) 先返回一个装饰器，再由它装饰函数（三层嵌套）。"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)                              # 等价于 shout = repeat(3)(shout)
def shout(word):
    """把单词喊三遍。"""
    print(f"  喊：{word.upper()}")
    return word
print(f"  slow_sum(100000) = {slow_sum(100000)}")
print(f"  名字和文档被保住了：__name__={slow_sum.__name__!r}, __doc__={slow_sum.__doc__!r}")
# ⚠️ 坑：忘了 @functools.wraps，slow_sum.__name__ 会变成 'wrapper'，调试、日志、文档
#         全都对不上号。写装饰器请养成配 wraps 的习惯。
shout("hi")
print(f"  @repeat(3) 的返回值 = {shout('again')!r}  ← 最后一次调用的结果")
print(f"关键结果：装饰器 = 接收函数返回函数，@ 只是语法糖")
print("-" * 60)

# ============================================================
# 19. 高阶函数与 functools：map / filter / reduce / sorted / partial
# ============================================================
print("=" * 60, "19. 高阶函数与 functools", sep="\n")
def power_of(base, exp):
    """base 的 exp 次方。"""
    return base ** exp
nums = [1, 2, 3, 4, 5, 6]
words = ["banana", "apple", "cherry", "fig"]
square_of = partial(power_of, exp=2)    # 预先固定 exp=2，生成一个新函数
print(f"  map 平方：{list(map(lambda x: x * x, nums))}；filter 偶数：{list(filter(lambda x: x % 2 == 0, nums))}")
print(f"  reduce 求和：{reduce(lambda acc, x: acc + x, nums)}；带初值 100：{reduce(lambda acc, x: acc + x, nums, 100)}")
print(f"  sorted(key=len)：{sorted(words, key=len)}；sorted(key=末字母)：{sorted(words, key=lambda w: w[-1])}")
print(f"  partial 固定 exp=2：square_of(9) = {square_of(9)}；itertools.accumulate：{list(itertools.accumulate(nums))}")
# ⚠️ 坑：reduce 不给初值时就拿第一个元素当起点，空序列会 TypeError。
# ⚠️ 坑：map / filter 返回的是"迭代器"，只能消费一次。
it = map(str, nums)
print(f"  消费一次：{list(it)}；再消费一次：{list(it)}  ← 空了！迭代器被用完了")
print(f"关键结果：把小函数传来传去，是 Python 表达数据流水线的常用手法")
print("-" * 60)

# ============================================================
# 20. 常见坑汇总（对照前面各节）
# ============================================================
print("=" * 60, "20. 常见坑汇总", sep="\n")
def add_forgot_return(a, b):
    a + b                               # 忘了写 return
def push(lst, value):
    lst.append(value)                   # 直接改了传进来的那个对象
    return lst
def increment():
    # counter_global += 1               # 取消注释会 UnboundLocalError：赋值让计数器成了局部名
    return counter_global + 1
data = [1]
push(data, 2)
print(f"  坑1 忘写 return：add_forgot_return(1, 2) = {add_forgot_return(1, 2)!r}；坑2 可变默认参数见第 14 节")
print(f"  坑3 改了可变实参：调用前 data = [1]，调用后 data = {data}（形参和实参指向同一个列表对象）")
print(f"  坑4 函数内赋值 = 局部名：只读全局时 increment() = {increment()}")
print(f"  坑5 名字拼错 → NameError，不会静默地去找别的同名变量")
print(f"  坑6 位置参数超过 3~4 个，调用处就看不懂谁是谁 → 改用关键字实参或收进 dict/对象")
# 想避免坑3：函数里先写 lst = list(lst) 复制一份，或约定"我不改你的东西"（纯函数）。
print(f"  提示：VS Code 里把鼠标停在函数名上，能看到签名和 docstring。")
print("-" * 60)

# ============================================================
# 动手练习（先自己写，再看文件末尾的参考答案）
# ============================================================
print("=" * 60, "动手练习：8 题，由易到难", sep="\n")
# 1.【易】写函数 greet(name)，返回 "你好，<name>！"，并调用打印。
# 2.【易】写函数 area(width, height=1) 返回矩形面积；只传 width 时按正方形算。
# 3.【中】写函数 stats(*nums)，返回元组 (最小值, 最大值, 平均值)；nums 为空时返回 None。
# 4.【中】写工厂函数 make_multiplier(n)，返回"乘以 n"的函数；make_multiplier(3)(7) 应为 21。
# 5.【中】用 lambda + sorted 把 [("Bob", 25), ("Amy", 30), ("Cid", 20)] 按年龄升序排。
# 6.【中】给第 3 题的函数补规范 docstring，并用它的 __doc__ 打印第一行。
# 7.【偏难】用 @functools.lru_cache 装饰递归版 fib，求 fib(50) 并打印 cache_info()。
# 8.【难】把第 8 节 price_bad 改用卫语句；并修复 add_item(item, lst=[]) 的经典 bug，
#         说明为什么第一次调用看起来是对的、Python 为什么要这样设计。
print("  写完记得用 Ctrl+F5 跑一遍验证。")
print("=" * 60)

# ============================================================
# 参考答案（放在字符串里，不影响上面的程序运行）
# ============================================================
ANSWERS = """
1) 最简函数
def greet(name):
    return f"你好，{name}！"
print(greet("小明"))                  # 你好，小明！

2) 默认值参数（默认参数必须写在非默认参数之后）
def area(width, height=1):
    return width * height
print(area(5), area(3, 4))            # 5 12

3) *args + 卫语句（返回多个值其实是 tuple，可直接解包）
def stats(*nums):
    '''返回 (最小值, 最大值, 平均值)；空输入返回 None。'''
    if not nums:
        return None                   # 卫语句：先把空的情况挡掉
    return min(nums), max(nums), sum(nums) / len(nums)
print(stats())                        # None
low, high, avg = stats(1, 2, 3, 4)
print(low, high, avg)                 # 1 4 2.5

4) 闭包工厂（每次调用都捕获一个独立的 n）
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply
print(make_multiplier(3)(7))          # 21

5) lambda + sorted（key 只负责"取出用来比较的值"）
people = [("Bob", 25), ("Amy", 30), ("Cid", 20)]
print(sorted(people, key=lambda p: p[1]))   # [('Cid',20), ('Bob',25), ('Amy',30)]

6) docstring
def stats(nums):
    '''统计一组数字。

    参数: nums 是数字序列，不能为空。
    返回: (最小值, 最大值, 平均值) 三元组。
    '''
    return min(nums), max(nums), sum(nums) / len(nums)
print(stats.__doc__.strip().splitlines()[0])      # 统计一组数字。

7) lru_cache（functools 在本文件开头已 import）
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(50))                        # 12586269025
print(fib.cache_info())               # misses=51（0..50 各算一次），hits 很多
# 没有缓存时 fib(50) 的调用次数是指数级（约 2^50 量级），普通机器上基本等于卡死。
# ⚠️ 参数必须可哈希，传 list 会 TypeError。

8) 卫语句 + 可变默认参数
def price(user, coupon, stock):
    if user is None:
        return -4
    if not user.get("vip"):
        return -3
    if coupon is None:
        return -2
    if stock <= 0:
        return -1
    return 80
# 主逻辑只缩进一层，每个异常情况一行说清；原写法最深处缩进 4 层。

def add_item(item, lst=[]):           # ✗ 坏写法
    lst.append(item)
    return lst
print(add_item("苹果"))    # ['苹果']              —— 看起来完全正确
print(add_item("香蕉"))    # ['苹果', '香蕉']       ← 出问题了！

【为什么第一次是对的】默认值 [] 在 def 执行时只创建了一次，这个列表对象被存进
add_item.__defaults__。第一次调用时它还是空的，所以结果正常；之后每次不传 lst 的调用
用的都是同一个列表对象，而 append 是原地修改，于是数据不断累积。
【为什么 Python 这样设计】默认值在"定义时"求值，而不是"每次调用时"求值。这样默认值可以
是一个在定义时就确定好的对象（常量表、已算好的结果），不必每次重建；副作用是可变对象
会被所有调用共享。

def add_item(item, lst=None):         # ✓ 修复：用 None 当哨兵
    if lst is None:
        lst = []                      # 每次调用都新建列表
    lst.append(item)
    return lst
print(add_item("苹果"), add_item("香蕉"))   # ['苹果'] ['香蕉']
"""
