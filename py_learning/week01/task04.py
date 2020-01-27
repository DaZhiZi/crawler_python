from utils import log
from utils import ensure
from utils import isEquals

from task03 import words
from task02 import find, lower_case1, decode3


def word_num(answer):  # answer 有几个单词在 words 中
    times = 0
    list = answer.split(' ')
    for word in list:
        if word in words:
            times += 1
    log('出现的次数', times)
    return times


def best_times(answers):  # 最优解的 索引
    index = 0  # 默认第一个是最优解的索引  及出现单词 在 words 最多
    max_times = word_num(answers[index])
    for i, answer in enumerate(answers):
        num = word_num(answer)
        if num > max_times:
            index = i
            max_times = num
    return index


def best_answer(possible_answers):
    index = best_times(possible_answers)
    r = possible_answers[index]
    return r


def decode_line(code):
    log('decode_line')
    decodes = decode3(code)  # 得到的 所有可能的结果 26 种
    c = best_answer(decodes)  # 选择最优解
    log('c', c)
    return c


def decode_random(codes):
    arr = []
    for code in codes:
        c = lower_case1(code)  # 大写转换小写
        new_code = decode_line(c)  # 解码
        arr.append(new_code)
    return arr


def load_codes():
    path = "code.txt"
    list = []
    with open(path) as all:
        for line in all:
            list.append(line)
    return list


def main():
    """
     本题将对一段凯撒加密后的密文进行解密。
     该段密文有多行内容，每一行在加密时都采用了不同（或相同）的位移数 shift 。
     但每行加密时的位移数未知。
     请求出该段密文的明文。
    """
    r = ''
    # codes = [
    #     'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ',
    #     'JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW',
    #     'BPM YCQKS JZWEV NWF RCUXA WDMZ BPM TIHG LWO',
    # ]
    codes = load_codes()
    r = decode_random(codes)
    log('r', r)
    return r
    pass


if __name__ == '__main__':
    main()
