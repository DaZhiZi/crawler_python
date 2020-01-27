"""
先近先出
    element  -----  e

    enqueue (e)  入队
    dequeue()   出队 并 返回
    front()     队伍中最前面的那位大哥
    isEmpty()   是否 为空
    size()      数量
    print()     打印
"""
class Queue():
    def __init__(self):
        self.list = []

    def enqueue(self, element):
        self.list.append(element)

    def dequeue(self):
        # js shift()
        return self.list.pop(0)


    def front(self):
        return self.list[0]

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def log(self):
        print(self.list)


def test():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    q.log()

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    test()