from utils import log
from utils import ensure
from utils import isEquals
"""
seq[ind] 获得下标为Ind的元素

seq[ind1:ind2] 获得下标从ind1到ind2间的元素集合

seq * expr 序列重复expr次

seq1 + seq2 连接序列seq1和seq2

obj in seq 判断obj元素是否包含在seq中  *******

obj not in seq 判断obj元素是否不包含在seq中 

list(iter) 把可迭代对象转换为列表

str(obj) 把obj对象转换为字符串

tuple(iter) 把一个可迭代对象转换成一个元祖对象  
"""
def test_01():
    num = enumerate([1, 2, 3, 4, 6, 5])
    obj = dict(num)
    log('obj', obj)
    pass


def test_02():
    pass


def main():
    test_01()
    test_02()


if __name__ == '__main__':
    main()