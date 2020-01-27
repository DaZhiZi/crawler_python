from utils import log
from utils import ensure
from utils import isEquals

"""
js  == py ==
js === py is
"""

"""
  n 是 int 类型
  width 是 int 类型

  把 n 的位数变成 width 这么长，并在右对齐，不足部分用 0 补足并返回
  具体请看测试, 注意, 返回的是 string 类型

  返回 string 类型
"""


def zfill(n, width):
    s = str(n)
    i = 0
    zero = ''
    zero_len = width - len(s)
    while i < zero_len:
        zero += '0'
        i += 1
    return zero + s


def test_zfill():
    msg = 'test_zfill'
    isEquals(zfill(1, 4), '0001', msg)


"""
s 是 string
width 是 int
fillchar 是 长度为 1 的字符串, 默认为空格 ' '

如果 s 长度小于 width, 则在末尾用 fillchar 填充并返回
否则, 原样返回, 不做额外处理

返回 string 类型
"""


def ljust(s, width, fillchar=' '):
    s = str(s)
    s = str(s)
    zero_len = width - len(s)
    z = zero(zero_len, fillchar)
    log('z + s', z + s)
    return z + s


def test_ljust():
    msg = 'test_ljust'
    isEquals(ljust('gua', 6, 'y'), 'yyygua', msg)


"""
 s 是 string
 width 是 int
 fillchar 是 长度为 1 的字符串, 默认为空格 ' '

 如果 s 长度小于 width, 则在开头用 fillchar 填充并返回

 返回 string 类型
"""


def zero(num, fillchar):
    i = 0
    zero = ''
    while i < num:
        zero += fillchar
        i += 1
    return zero


def rjust(s, width, fillchar=' '):
    s = str(s)
    zero_len = width - len(s)
    z = zero(zero_len, fillchar)
    log('s + z', s + z)
    return s + z


def test_rjust():
    msg = 'test_rjust'
    isEquals(rjust('gua', 6, 'y'), 'guayyy', msg)


"""
 s 是 string
   width 是 int
   fillchar 是 长度为 1 的字符串, 默认为空格 ' '

   如果 s 长度小于 width, 则在两边用 fillchar 填充并返回
   如果 s.length 和 width 互为奇偶, 则无法平均分配两边的 fillchar
   这种情况下, 让左边的 fillchar 数量小于右边

   返回 string 类型
   width > len(s)
"""


def center(s, width, fillchar=' '):
    s = str(s)
    z = width - len(s)
    if z % 2 == 0:
        left_len = z / 2 + len(s)
        l = ljust(s, left_len, fillchar)
        s = rjust(l, width, fillchar)
    else:
        left_len = (z + 1) / 2 + len(s)
        l = ljust(s, left_len, fillchar)
        s = rjust(l, width, fillchar)
    log('s', s)
    return s


def test_center():
    msg = 'test_center'
    isEquals(center('gua', 6, 'y'), 'yyguay', msg)


"""
  s 是 string
检查 s 中是否只包含空格

   返回 bool, 如果 s 中包含的只有空格则返回 true, 否则返回 false
"""


def is_space(str):
    r = True
    for i in range(len(str)):
        if str[i] != ' ':
            r = False
            break
    log('r', r)
    log('type(r)', type(r))
    return r


def test_is_space():
    msg = 'test_is_space'
    isEquals(is_space('  '), True, msg)
    isEquals(is_space('gu a'), False, msg)


"""
  s 是字符串
   检查 s 中是否只包含数字
   返回: bool,
    如果 s 中包含的只有数字则返回 true, 否则返回 false
"""


def is_digit(str):
    num = '0123456789'
    for i in range(len(str)):
        if str[i] not in num:
            return False
    return True


def test_is_digit():
    msg = 'is_digit'
    isEquals(is_digit('123423424'), True, msg)
    isEquals(is_digit('gu a'), False, msg)
    isEquals(is_digit('1341gu a123242'), False, msg)
    pass


"""
 s 是 string
    返回一个「删除了字符串开始的所有空格」的字符串

    返回 string
"""


def strip_left(str):
    if is_space(str):  # 全部为空格
        return ''
    space = ' '
    if str[0] != space:
        return str
    index = 0  # 默认为 0  空格的索引
    for i in range(len(str)):
        if str[i] == space:
            index = i
            continue
        else:
            break
    index += 1
    r = str[index::]
    log('r', r)
    return r


def test_strip_left():
    msg = 'strip_left'
    isEquals(strip_left('  gua'), 'gua', msg)
    isEquals(strip_left('gua  gua'), 'gua  gua', msg)
    isEquals(strip_left(' gua  gua'), 'gua  gua', msg)


def strip_right(str):
    if is_space(str):  # 全部为空格
        return ''
    space = ' '
    if str[len(str) - 1] != space:
        return str
    index = 0  # 默认为 0  空格的索引
    for i in range(len(str)):
        i = len(str) - 1 - i
        if str[i] == space:
            index = i
            continue
        else:
            break
    r = str[:index:]
    log('r', r)
    return r


def test_strip_right():
    msg = 'strip_right'
    isEquals(strip_right('gua  '), 'gua', msg)
    isEquals(strip_right('gua  gua'), 'gua  gua', msg)
    isEquals(strip_right('gua  gua  '), 'gua  gua', msg)


"""
 s 是 string
    返回一个「删除了字符串首尾的所有空格」的字符串

    返回 string
"""


def strip(str):
    return strip_left(strip_right(str))


def test_strip():
    msg = 'strip'
    isEquals(strip('  gua  '), 'gua', msg)
    isEquals(strip(' gua  gua'), 'gua  gua', msg)
    isEquals(strip('gua  '), 'gua', msg)
    isEquals(strip('gua  gua'), 'gua  gua', msg)
    isEquals(strip('gua  gua  '), 'gua  gua', msg)


def main():
    test_zfill()
    test_ljust()
    test_rjust()
    test_center()
    test_is_space()
    test_is_digit()
    test_strip_left()
    test_strip_right()
    test_strip()


if __name__ == '__main__':
    main()
