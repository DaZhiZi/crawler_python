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
    log('index', index)
    return index


def test_find():
    msg = 'find'
    isEquals(find('gua', 'a'), 2, msg)


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
    log('result', result)
    return result


def test_lower_case1():
    msg = 'lower_case1'
    isEquals(lower_case1('xiao-gUA'), 'xiao-gua', msg)



# 给定一个英文句子（一个只有字母的字符串），
# 将句中所有单词变为有且只有首字母大写的形式
"""
str = 'gua gua  gua guagua  '
 
str = 'Gua gua gua guagua  '
"""
def title(str):
    s = str
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    u = upper[find(lower, s[0])]
    result = u + str[1::]
    log('result', result)
    return result

def cap_string(str):
    s = lower_case1(str)
    return title(s)


def test_cap_string():
    msg = 'cap_string'
    isEquals(cap_string('gua gua  gua Guagua  '), 'Gua gua  gua guagua  ', msg)


def main():
    test_cap_string()
    pass


if __name__ == '__main__':
    main()
