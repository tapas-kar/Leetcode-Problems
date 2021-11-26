def getSum(a, b):

    while b != 0:
        temp = (a & b) << 1
        a = a ^ b
        b = temp

    return a


a = 1
b = 2

getSum(a, b)