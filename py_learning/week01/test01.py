# 使用点语法获取json数据
from utils import log
from collections import abc

class Data(object):
    def __init__(self, mapping):
        self._data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            return Data.build(self._data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


def main():
    s = Data({'a': {'b': 1}})
    log('s.__dict__', s.__dict__)
    log('s.a.b', s.a.b)


if __name__ == '__main__':
    main()

