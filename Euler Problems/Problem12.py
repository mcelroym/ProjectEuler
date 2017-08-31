def triangle_number(n):
    return n * (n + 1) / 2

def number_of_divisors(num):
    count = 0

    for i in range(1, num / 2 + 1):
        if num % i == 0:
            count +=1

    count += 1

    return count

test_num = 1

#while number_of_divisors(test_num) <= 500:
#    test_num += 1

#print number_of_divisors(4)
