def collatz_sequence_length(n):
    count = 1

    while n != 1:
        count += 1

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

    return count


i = 1
max_length = 0
max_start_val = 0

while i < 1000000:

    if i % 10000 == 0:
        print i

    curr_length = collatz_sequence_length(i)

    if curr_length > max_length:
        max_length = curr_length
        max_start_val = i

    i += 1


print max_start_val, max_length