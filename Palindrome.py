#判断一个数是否是回文数
from Integer_Reverse import *
def palindrome(int_num):
    b = integer_reverse(int_num)

    if b == int_num:
        return True
    else:
        return False