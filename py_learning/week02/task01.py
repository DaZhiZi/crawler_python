from utils import log
from utils import ensure
from utils import isEquals

"""
    delimiter 是 string
    array 是包含 string 的 array

    把 array 中的元素用 delimiter 连接成一个字符串并返回
    具体请看测试
"""
def join(delimiter, arr):
    r = arr[0]
    for i in range(1, len(arr)):
        a = arr[i]
        r += (delimiter + a)
    log('r', r)
    return r

def test_join():
    msg = 'join'
    arr1 = ['da', 'vi', 'zi']
    isEquals(join('-', arr1), 'da-vi-zi', msg)
    arr2 = ['g', 'u', 'a']
    isEquals(join('*', arr2), 'g*u*a', msg)

"""
 s 是 string
    delimiter 是 string, 默认为空格 ' '

    以 delimiter 为分隔符号, 返回一个 array
    例如
    split('1 2 3') 返回 ['1', '2', '3']
    split('a=b&c=d', '&') 返回 ['a=b', 'c=d']
    注意, 测试 array 是否相等得自己写一个函数用循环来跑

    学会拆分函数
    方法：
    0123456789
    'a=bc=def'
    [0, 1, 4, s.length]
    (0, 1)
    (1, 4)
    (4, s.length)
"""
def split(s, delimiter=' '):
    list = []
    space = len(delimiter)
    start = 0 # 起点
    for i in range(len(s)):
        tmp = s[i : i + space:]
        if tmp == delimiter:
            list.append(s[start : i :])
            start = i + space
    list.append(s[start ::])
    log('list', list)
    return list


def test_split():
    msg = 'split'
    list =  ['da', 'vi', 'zi']
    isEquals(split('da-vi-zi', '-'), list , msg)

"""
s old newString 都是 string
返回一个「将 s 中出现的所有 old 字符串替换为 new 字符串」的字符串
"""
def replace_all(s, old, new_str):
    r = join(new_str,  split(s, old))
    log('r', r)
    return r


def test_replace_all():
    msg = 'replace_all'
    isEquals(replace_all('da-vi-zi', '-', '&'), 'da&vi&zi' , msg)


"""
    start end step 都是数字

    和 range2 一样, 但是要求支持负数 step
    返回一个 array
    假设 start=1, end=5, step=1 返回数据如下
    [1, 2, 3, 4]
    假设 start=6, end=0, step=-1 返回数据如下
    [6, 5, 4, 3, 2, 1]
"""
def step_condition(start, end, step):
    if (step < 0):
        return end < start
    else:
        return end > start

def range3(start, end, step):
    list = []
    i = start
    while(step_condition(i, end, step)):
        list.append(i)
        i += step
    log('list', list)
    return list

def test_range3():
    msg = 'range3'
    isEquals(range3(1, 5, 1), [1, 2, 3, 4], msg)
    isEquals(range3(6, 0, -1), [6, 5, 4, 3, 2, 1], msg)

def main():
    test_join()
    test_split()
    test_replace_all()
    test_range3()


if __name__ == '__main__':
    main()