import math

def is_prime(n):
    i = 2

    if n >= 10:
        if n % 10 == 0: return False
        if n % 10 == 2: return False
        if n % 10 == 4: return False
        if n % 10 == 5: return False
        if n % 10 == 6: return False
        if n % 10 == 8: return False

    if n == 2: return True

    while i <= int(math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
        i += 1

    return True


def get_nth_prime(k):
    count = 0
    num_to_test = 2

    while count < k:
        if is_prime(num_to_test):
            count += 1

        num_to_test += 1

    return num_to_test - 1

print get_nth_prime(10001)