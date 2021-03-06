import math
import time

num = 600851475143
max_prime_factor = 1

# what is the largest prime number that evenly divides num?

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

n = 2
val = num

print "Running..."
t = time.clock()

while n <= val:
    if val % n == 0:
        if is_prime(n):
            max_prime_factor = n

        val = val / n

    else:
        n += 1

print "Finished"
print "Runtime: ", time.clock() - t

print max_prime_factor