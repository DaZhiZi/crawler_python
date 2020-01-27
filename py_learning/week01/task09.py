from utils import log
from utils import ensure
from utils import isEquals


# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10
def rule_1(char):
    r = False
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = lower + upper
    if char in letter:
        r = True
    log('rule_1', r)
    return r


def rule_2(char):
    r = False
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    underline = "_"
    valid_str = lower + upper + num + underline
    if char in valid_str:
        r = True
    log('rule_2', r)
    return r


def rule_3(char):
    r = False
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = lower + upper
    num = '0123456789'
    valid_str = letter + num
    if char in valid_str:
        r = True
    log('rule_3', r)
    return r


def valid_password(pwd):
    # 默认为 True
    r = True
    # 1，第一位是字母
    if rule_1(pwd[0]) is not True:
        return False
    # 2，只能包含字母、数字、下划线
    for char in pwd:
        if rule_2(char) is not True:
            return False
    # 3，只能字母或数字结尾
    if rule_3(pwd[-1]) is not True:
        return False
    # 4，最小长度2
    # 5，最大长度10
    if len(pwd) < 2 or len(pwd) > 10:
        return False
    return r


def test_valid_password():
    msg = 'valid_password '
    isEquals(valid_password('gua123'), True, msg)
    isEquals(valid_password('gua123[p'), False, msg)


"""
num  
yes  return True
no   reutrn False

被自己 或者 1 整除 (2除外)

for i in range(start, end):
    log('i', i)
    
"""


def is_prime(num):
    r = True
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    # log('prime', r)
    return r


# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用
def prime_numbers(num):
    list = []
    for i in range(2, num):
        if is_prime(i):
            list.append(i)
    log('list', list)
    return list


def test_prime_numbers():
    msg = 'prime_numbers '
    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    isEquals(prime_numbers(100), list, msg)


# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
"""
 str = "hello"
 
 obj = {
    'h': 1,
    'e': 1,
    'l': 2,
    'o': 1,
 }
 
 tuple_h = ('h', 1)
 
 arr = [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
 
 
 掏粪方法：
    python 对象是否含有某个属性
    hasattr(obj, pro)
"""

"""
def letter_obj(str):
    obj = {}
    for i in str:
        log('i', i, hasattr(obj, i))
        if hasattr(obj, i):
            obj[i] += 1
        else:
            obj[i] = 1
    log('obj', obj)
    return obj
"""
def letter_obj(str):
    obj = {}
    for s in str:
        if s in obj:  # 这里为什么用  in 一个套路吗
            obj[s] += 1
        else:
            obj[s] = 1
    log('obj', obj)
    return obj


def letter_count(str):
    obj = letter_obj(str)
    arr = [(k, v) for k, v in obj.items()]
    log(arr, arr)
    return arr


def test_letter_count():
    msg = 'letter_count'
    arr = [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
    isEquals(letter_count('hello'), arr, msg)


def main():
    # str = 'gua'
    # log('s', str[0])
    test_valid_password()
    test_prime_numbers()
    test_letter_count()
    pass


if __name__ == '__main__':
    main()
