from utils import log
from utils import ensure
from utils import isEquals


# 求数组的和
def sum(arr):
    result = 0
    for n in arr:
        result += n
    # log('result', result)
    return result


# 求 array 的乘积
def product(arr):
    result = 1
    for n in arr:
        result *= n
    log('result', result)
    return result


# 返回一个数的绝对值
def abs(num):
    if num < 0:
        return -num
    else:
        return num


# 求 array 中所有数字的平均数
def average(arr):
    l = len(arr)
    return sum(arr) / l


def min(arr):
    m = arr[0]
    for a in arr:
        if m > a:
            m = a
    return m


def sum1(num):
    s = 1
    i = 2
    while i <= num:
        if i % 2 != 0:
            s -= i
        else:
            s += i
        i += 1
    log('s', s)
    return s


def sum2(num):
    n = num
    s = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            s -= i
        else:
            s += i
        i += 1
    return s


# 不用递归
def fac(num):
    n = num
    i = 1
    s = 1
    while i <= num:
        s *= i
        i += 1
    return s


""""
注意 下面几题中的参数 op 是 operator(操作符) 的缩写
op 是 string 类型, 值是 '+' '-' '*' '/' 其中之一
a b 分别是 2 个数字
根据 op 对 a b 运算并返回结果(加减乘除)
"""


def apply(operator, a, b):
    op = operator
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


"""
op 是 '+' '-' '*' '/' 其中之一
oprands 是一个只包含数字的 array
根据 op 对 oprands 中的元素进行运算并返回结果
例如, 下面的调用返回 -4
var n = applyList('-', [3, 4, 2, 1])
log(n)
// 结果是 -4, 用第一个数字减去所有的数字
"""


def applyList(op, oprands):
    result = oprands[0]
    i = 1
    while i < len(oprands):
        result = apply(op, result, oprands[i])
        # log('result', i, result)
        i += 1
    return result


"""
 实现 applyCompare 函数
参数如下
expression 是一个 array(数组), 包含了 3 个元素
第一个元素是 op, 值是 '>' '<' '==' 其中之一
剩下两个元素分别是 2 个数字
根据 op 对数字运算并返回结果(结果是 true 或者 false)
"""


def applyCompare(expression):
    op = expression[0]
    a = expression[1]
    b = expression[2]
    if op == '>':
        return a > b
    elif op == '<':
        return a < b
    elif op == '==':
        return a == b


"""
参数如下
expression 是一个 array
expression 中第一个元素是上面几题的 op, 剩下的元素是和 op 对应的值
根据 expression 运算并返回结果
"""


def apply_ops(expression):
    op = expression[0]
    if op in '+-*/':
        oprands = expression[1: len(expression)]
        return applyList(op, oprands)
    else:
        return applyCompare(expression)


def test_01():
    arr = [1, 2, 3]
    ensure(sum(arr) == 6, 'test_01')


def test_02():
    arr = [1, 2, 3, 6]
    ensure(product(arr) == 36, 'test_02')


def test_03():
    ensure(abs(-1) == 1, 'test_03   1')
    ensure(abs(1) == 1, 'test_03   2')
    ensure(abs(0) == 0, 'test_03   3')


def test_04():
    arr = [4, 2, 6, 8]
    ensure(average(arr) == 5, 'test_04')


def test_05():
    arr = [23, 456, 647, 2, 4, 5]
    ensure(min(arr) == 2, 'test_05')


def test_06():
    ensure(sum1(3) == 0, 'test_06')


def test_07():
    ensure(sum2(3) == 2, 'test_07')


def test_08():
    ensure(fac(3) == 6, 'test_08')


def test_09():
    ensure(apply('+', 1, 5) == 6, 'test_09  +')
    ensure(apply('-', 1, 5) == -4, 'test_09  -')
    ensure(apply('*', 5, 5) == 25, 'test_09  *')
    ensure(apply('/', 5, 5) == 1, 'test_09  /')


def test_10():
    ensure(applyList('+', [1, 3, 2]) == 6, 'test_10  +')
    ensure(applyList('-', [1, 3, 2]) == -4, 'test_10  -')
    ensure(applyList('*', [1, 3, 2]) == 6, 'test_10  *')
    ensure(applyList('/', [6, 3, 2]) == 1, 'test_10  /')


def test_11():
    ensure(applyCompare(['>', 2, 1]) == True, 'test_11  >')


def test_12():
    arr = ['+', 1, 2, 3]
    ensure(apply_ops(['>', 2, 1]) == True, 'test_12  >')
    ensure(apply_ops(arr) == 6, 'test_12  +')


def main():
    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()
    test_07()
    test_08()
    test_09()
    test_10()
    test_11()
    test_12()


if __name__ == '__main__':
    main()
