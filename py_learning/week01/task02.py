from utils import log
from utils import ensure
from utils import isEquals

"""
    s1 s2 都是 string
    但 s2 的长度是 1

    返回 s2 在 s1 中的下标, 从 0 开始, 如果不存在则返回 -1
"""


def find(s1, s2):
    index = -1
    for i in range(len(s1)):
        if s1[i] == s2:
            index = i
            break
    # log('index', index)
    return index


def test_find():
    msg = 'find'
    isEquals(find('gua', 'a'), 2, msg)


"""
下面给出一个例子作为后面作业的参考
返回字符串的小写形式的函数
注意, 这里假设了 s 字符串全是大写字母

"""


def lower_case(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        u = lower[find(upper, s)]
        result += u
    log('result', result)
    return result


def test_lower_case():
    msg = 'lower_case'
    isEquals(lower_case('GUA'), 'gua', msg)


"""
定义一个函数
参数是一个字符串 s
返回大写后的字符串
注意, 假设 s 字符串全是小写字母

注意, 自行实现测试函数, 之后的题目都要求自行实现测试函数
"""


def upper_case(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        u = upper[find(lower, s)]
        result += u
    log('result', result)
    return result


def test_upper_case():
    msg = 'upper_case'
    isEquals(upper_case('gua'), 'GUA', msg)


"""
实现 lowercase1
它能正确处理带 小写字母 的字符串
"""


def lower_case1(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        if s in upper:
            u = lower[find(upper, s)]
            result += u
        else:
            result += s
    # log('result', result)
    return result


def test_lower_case1():
    msg = 'lower_case1'
    isEquals(lower_case1('xiao-gUA'), 'xiao-gua', msg)


"""
实现 uppercase1
它能正确处理带 大写字母 的字符串
"""


def upper_case1(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        if s in lower:
            u = upper[find(lower, s)]
            result += u
        else:
            result += s
    log('result', result)
    return result


def test_upper_case1():
    msg = 'upper_case1'
    isEquals(upper_case1('xiao-gUA'), 'XIAo-GUA', msg)


"""
实现一个叫 凯撒加密 的加密算法, 描述如下
对于一个字符串, 整体移位, 就是加密
以右移 1 位为例
原始信息 'afz' 会被加密为 'bga'
实现 encode1 函数, 把明文加密成密码并返回
右移 1 位
"""


#  (char, n)
#  char  可以为  单字母 （大写小写） 或者其它  不移位
def shift_char(char, n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char in lower:  # 小写
        index = find(lower, char)
        new_index = (index + n + 26) % 26
        return lower[new_index]
    elif char in upper:  # 大写
        index = find(upper, char)
        new_index = (index + n + 26) % 26
        return upper[new_index]
    else:
        return char


# r  result
def encode1(str):
    r = ''
    for i in range(len(str)):
        char = str[i]
        r += shift_char(char, +1)
    log('r', r)
    return r


def test_encode1():
    msg = 'test_encode1'
    isEquals(encode1('abc'), 'bcd', msg)


# 实现 decode1 函数, 把加密的密码解密为明文并返回
def decode1(str):
    r = ''
    for i in range(len(str)):
        char = str[i]
        r += shift_char(char, -1)
    log('r', r)
    return r


def test_decode1():
    msg = 'test_decode1'
    isEquals(decode1('bcd'), 'abc', msg)


"""
实现 encode2
多了一个参数 shift 表示移的位数
"""


# r  result
def encode2(str, shift):
    r = ''
    for i in range(len(str)):
        char = str[i]
        r += shift_char(char, shift)
    log('r', r)
    return r


def test_encode2():
    msg = 'test_encode2'
    isEquals(encode2('abc', 2), 'cde', msg)


"""
实现 decode2
多了一个参数 shift 表示移的位数
"""


def decode2(str, shift):
    r = ''
    for i in range(len(str)):
        char = str[i]
        r += shift_char(char, shift)
    log('r', r)
    return r


def test_decode2():
    msg = 'test_decode2'
    isEquals(decode2('cde', -2), 'abc', msg)


"""
知乎有一个求助题, 破译密码的
链接在此
https://www.zhihu.com/question/28324597
这一看就是凯撒加密...
如果没思路, 可看本文件最后的提示
我把密码放在下面, 请解出原文
"""


def decode3(str):
    list = []
    s = lower_case1(str)
    for i in range(26):
        ele = decode2(s, i)
        log('ele', i, ele)
        list.append(ele)
    return list


# 2019/12/29 17:07:21 ele 23 sometimes i want to chat with you,but i have no reason to chat with you
def test_decode3():
    log('test_decode3')
    str = 'VRPHWLPHV L ZDQW WR FKDW ZLWK BRX,EXW L KDYH QR UHDVRQ WR FKDW ZLWK BRX'
    arr = decode3(str)
    log('arr', arr)
    pass


def main():
    test_find()
    test_lower_case()
    test_upper_case()
    test_lower_case1()
    test_upper_case1()
    test_encode1()
    test_decode1()
    test_decode2()
    test_decode3()


if __name__ == '__main__':
    main()
