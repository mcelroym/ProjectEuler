def sum_of_squares(n):
    sum = n * (n+1) * (2*n + 1) / 6
    return sum

def square_of_sum(n):
    sum = n * (n+1) / 2
    sum = sum ** 2
    return sum

print square_of_sum(10)
print sum_of_squares(10)

print square_of_sum(100) - sum_of_squares(100)