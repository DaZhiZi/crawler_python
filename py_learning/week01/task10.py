from utils import log
from utils import ensure
from utils import isEquals

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

def main():
    str = "hello"
    letter_obj(str)

if __name__ == '__main__':
    main()
