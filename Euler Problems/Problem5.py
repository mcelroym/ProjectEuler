import math

def is_prime(n):

    if n >= 10:
        if n % 10 == 0: return False
        if n % 10 == 2: return False
        if n % 10 == 4: return False
        if n % 10 == 5: return False
        if n % 10 == 6: return False
        if n % 10 == 8: return False

    if n == 2: return True

    i = 2
    while i <= int(math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
        i += 1

    return True

######################

prime_factors_count = [0] * 21
result = 1

def prime_factors(n):
    arr = []
    i = 2

    while i <= n:
        if n % i == 0:
            arr.append(i)
            n = n / i
        else:
            i += 1

    return arr

for i in range(2, 21):
    factors_of_i = prime_factors(i)

    for j in range(2, i+1):
        temp = factors_of_i.count(j)
        if prime_factors_count[j] < temp:
            prime_factors_count[j] = temp

for i in range(2, 21):
    if prime_factors_count[i] > 0:
        result *= i ** prime_factors_count[i]

print result
print prime_factors_count