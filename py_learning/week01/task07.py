# 作者：鸡啊
# 链接：https://zhuanlan.zhihu.com/p/39538294
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# _*_ coding: utf-8 _*_
__author__ = 'qianzeng'
__date__ = '2018/7/11 19:23'


# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10
def valid_password(pwd):
    if len(pwd) < 2 or len(pwd) > 10:
        return False
    if not pwd[0].isalpha() or not pwd[-1].isalnum():
        return False
    for w in pwd:
        if not w.isalnum() and w != '_':
            return False
    return True


# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用
def prime_numbers():
    list = []
    for i in range(2, 101):
        a = i
        if i > 50: a = 50
        for x in range(1, a):
            if i % x == 0 and i != x and x != 1:
                a = 0
                break
        if a:
            list.append(i)
    return list


# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
def letter_count(str):
    d, l = {}, []
    for s in str:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    for k in d:
        l.append((k, d[k]))
    return l


# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式
def cap_string(str):
    return str.lower().title()


# 题 5
# 写一个 Queue 类，它有两个方法，用法如下
class Queue():
    def __init__(self):
        self.n = []

    def enqueue(self, n):
        self.n.append(n)

    def dequeue(self):
        return self.n.pop(0)


# 题 1
# print(valid_password('qwe123_qwe'))
# print(valid_password('123_qwe'))
# print(valid_password('qwe123_'))
# print(valid_password('qwe123+qwe'))

# 题 2
# print(prime_numbers())

# 题 3
# print(letter_count('hello'))

# 题 4
# print(cap_string('AklF'))

# 题 5
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue()) # 1
# print(q.dequeue()) # 2
# print(q.dequeue()) # 3