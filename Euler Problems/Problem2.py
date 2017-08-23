fib = [1, 2]
result = 2

while fib[-1] < 4000000:
    curr_term = fib[-1] + fib[-2]
    fib.append(curr_term)
    if curr_term % 2 == 0:
        result += curr_term

print result
