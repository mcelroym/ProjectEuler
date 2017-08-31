num = 2 ** 1000

digit_list = list(str(num))
digit_list = [int(i) for i in digit_list]

print sum(digit_list)