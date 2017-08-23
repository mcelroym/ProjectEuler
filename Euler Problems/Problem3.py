import math
num = 600851475143
max_prime_factor = 1

# what is the largest prime number that evenly divides num?

def is_prime(n):
    i = 2

    while i <= int(math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
        i += 1

    return True

n = 2
val = int(math.ceil(math.sqrt(num)))

print "Starting"

while n <= val:
    if is_prime(n) and (num % n == 0):
        max_prime_factor = n
    n += 1

print "Finished"

print max_prime_factor
