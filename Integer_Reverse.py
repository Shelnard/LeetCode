#给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
def integer_reverse(num):
    num_bits = []
    sign = 1

    if num < 0:
        sign = -1

    num = abs(num)

    while num != 0:
        num_bits.append(num / 10)
        num = num % 10

    num_reverse_bits = num_bits.reverse()
    result = 0

    for i in num_reverse_bits:
        result = result * 10 + i

    result = result * sign

    return result
