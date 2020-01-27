from utils import log
from utils import ensure
from utils import isEquals

"""
    3 个参数 s old new 都是字符串
    返回一个「将 s 中的 old 字符串替换为 new 字符串」的字符串
    假设 old 存在并且只出现一次
    返回 string
"""


def replace(str, old_str, new_str):
    str_len = len(str)
    old_len = len(old_str)
    left = ''
    right = ''
    for i in range(str_len):
        s = str[i: i + old_len]
        if s == old_str:
            left = str[0: i:]
            right = str[i + old_len::]
            break
    if left == '' and right == '':
        return str
    else:
        log('result', left + new_str + right)
        return left + new_str + right


def test_replace():
    msg = 'repalce'
    isEquals(replace('guayy', 'yy', 'gua'), 'guagua', msg)


"""
   s1 是一个字符串
   s2 是一个字符串
   检查 s1 是否以 s2 开头, 返回 true 或者 false
"""


def start_with(s1, s2):
    s2_len = len(s2)
    # log('s1[0: s2_len]', s1[0: s2_len])
    if s1[0: s2_len] == s2:
        return True
    else:
        return False


def test_start_with():
    msg = 'start_with'
    isEquals(start_with('guagua', 'gua'), True, msg)
    isEquals(start_with('guagua', 'ggua'), False, msg)


"""
    s1 是一个字符串
  s2 是一个长度为 1 的字符串
  返回参数 s2 在 s1 中第一次出现的下标
  如果 s2 没有在 s1 中出现, 返回 -1
"""


def find_in(s1, s2):
    index = -1
    for i in range(len(s1)):
        s = s1[i]
        if s == s2:
            index = i
            break
    log('index', index)
    return index


def test_find_in():
    msg = 'find_in'
    isEquals(find_in('guagua', 'a'), 2, msg)
    isEquals(find_in('guagua', 'g'), 0, msg)


"""
   s1 是一个字符串
   s2 是一个长度为 1 的字符串
   返回参数 s2 在 s1 中出现的所有下标组成的 array
   如果 s2 没有在 s1 中出现, 返回空数组 []
"""


def find_all_in(s1, s2):
    list = []
    for i in range(len(s1)):
        s = s1[i]
        if s == s2:
            list.append(i)
    log('list', list)
    return list


def test_find_all_in():
    msg = 'find_all_in'
    isEquals(find_all_in('guagua', 'a'), [2, 5], msg)
    isEquals(find_all_in('guagua', 'g'), [0, 3], msg)


"""
   s1 是一个字符串
   s2 是一个字符串, 长度未知, 不一定为 1
   返回参数 s2 在 s1 中出现的下标组成的 array
   如果 s2 没有在 s1 中出现, 返回 []
"""


def find_all_string(s1, s2):
    list = []
    s2_len = len(s2)
    for i in range(len(s1)):
        s = s1[i: i + s2_len]
        if s == s2:
            list.append(i)
    log('list', list)
    return list


def test_find_all_string():
    msg = 'find_all_string'
    isEquals(find_all_string('guagua', 'a'), [2, 5], msg)
    isEquals(find_all_string('guagua', 'g'), [0, 3], msg)
    isEquals(find_all_string('guagua', 'gua'), [0, 3], msg)


"""
s1 是一个字符串
s2 是一个字符串
检查 s1 是否以 s2 结尾, 返回 true 或者 false
"""


def end_with(s1, s2):
    result = True
    index = len(s1) - len(s2)
    end = s1[index:]
    if end != s2:
        result = False
    log('result', result)
    return result


def test_end_with():
    msg = 'end_with'
    isEquals(end_with('guagua', 'a'), True, msg)
    isEquals(end_with('guagua', 'gua'), True, msg)
    isEquals(end_with('guagua', 'Guagua'), False, msg)


"""
students 是 array
里面的每个元素都是如下格式的 object
{
    'name': 'gua',
    'sex': '男',
    'score': 127,
}
返回 score 最高的那个元素(object)
"""


def top1(student_list):
    obj = student_list[0]
    top_score = obj['score']
    for index, stu in enumerate(student_list):
        score = stu['score']
        if score > top_score:
            obj = student_list[index]
            top_score = score
    log('obj', obj)
    return obj


def test_top1():
    msg = 'top1'
    student_list = [
        {
            'name': 'gua1',
            'sex': '男',
            'score': 627,
        },
        {
            'name': 'gua2',
            'sex': '男',
            'score': 99,
        },
        {
            'name': 'gua3',
            'sex': '男',
            'score': 199,
        },
        {
            'name': 'gua4',
            'sex': '男',
            'score': 299,
        },
        {
            'name': 'gua5',
            'sex': '男',
            'score': 499,
        },
    ]
    gua = {
        'name': 'gua1',
        'sex': '男',
        'score': 627,
    }
    isEquals(top1(student_list), gua, msg)


"""
day 是代表星期的数字, 从周一到周日分别是 1 2 3 4 5 6 7
返回 '星期一' '星期二' 这样的描述字符串
"""


def formated_weekday(day):
    days = ['', '一', '二', '三', '四', '五', '六', '七']
    str = '星期' + days[day]
    return str


def test_formated_weekday():
    msg = 'formated_weekday'
    isEquals(formated_weekday(5), '星期五', msg)


"""
price 是一个 int
grade 合法情况下一共 6 种取值, 还可能没有给出这个参数
    '小学生'
    '初中生'
    '高中生'
    '大学生'
    '研究生'
对应的折扣分别是 5 6 7 8 9

注意, 如果调用者没有给出 grade 参数, 没有折扣

返回折扣后的价格
"""


def discount(price, grade):
    discount = [10, 5, 6, 7, 8, 9]
    grades = [None, '小学生', '初中生', '高中生', '大学生', '研究生']
    p = price
    for i in range(len(grades)):
        g = grades[i]
        if g == grade:
            p = discount[i] * p / 10
            break
    log('price', p)
    return p


def test_discount():
    msg = 'discount'
    isEquals(discount(100, '大学生'), 80.0, msg)


"""
array 是 array 类型, 里面的元素都是字符串
按如下的格式返回这个 array
假设 array 是 ['python', 'js', 'objective-c']
那么返回的数据是一个数组, 多了首尾两个元素
[
    '+++++++++++++++',
    '+ python      +',
    '+ js          +',
    '+ objective-c +',
    '+++++++++++++++',
]  返回包含了 string 的 array

三个部分  
上 下  都是   '+++++++++++++++',  
规律 根据  '+ objective-c +', 
中间     '+ objective-c +',    规律  arr 中长度最长  左右 都含有 +
"""


def max_length_ele(arr):
    r = arr[0]
    for ele in arr:
        if len(r) < len(ele):
            r = ele
    log('max_length_ele', r)
    return r


def repeat_char(char, num):
    r = ''
    for i in range(num):
        r += char
    return r


def top_bottom_jxhc(arr):
    ele = max_length_ele(arr)
    l = len(ele) + 2 + 2
    r = repeat_char('+', l)
    return r


def center_ele(arr):
    pass


def pretty_log(arr):
    r = []
    # top and bottom
    top = top_bottom_jxhc(arr)
    r.append(top)
    # center
    for ele in arr:
        ksge_num = len(top) - 2 - 2 - len(ele)
        ksge = repeat_char(' ', ksge_num)
        center = '+ {}{} +'.format(ele, ksge)
        r.append(center)
    # bottom
    r.append(top)
    log('r', r)
    return r


def test_pretty_log():
    msg = 'pretty_log'
    arr = ['python',
           'js',
           'objective-c',
           ]
    result = [
        '+++++++++++++++',
        '+ python      +',
        '+ js          +',
        '+ objective-c +',
        '+++++++++++++++',
    ]
    isEquals(pretty_log(arr), result, msg)


def main():
    test_replace()
    test_start_with()
    test_find_in()
    test_find_all_in()
    test_find_all_string()
    test_end_with()
    test_top1()
    test_formated_weekday()
    test_discount()
    test_pretty_log()


if __name__ == '__main__':
    main()
