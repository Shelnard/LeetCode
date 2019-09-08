#给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
def integer_reverse(self, num):
    sign = 1
    if num < 0:
        sign = -1
    num = abs(num)
    result = 0
    while num:
        result = result*10 + num%10
        num = int(num/10)

    result = result * sign

    return result
