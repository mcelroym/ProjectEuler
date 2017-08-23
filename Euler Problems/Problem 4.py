def is_palindrome(n):
    arr = list(str(n))
    index1 = 0
    index2 = len(arr) - 1

    while index1 < index2:
        if arr[index1] != arr[index2]:
            return False

        index1, index2 = index1 + 1, index2 - 1

    return True

max_palindrome = 0
for n1 in range(100, 1000):
    for n2 in range(n1, 1000):
        if n1 * n2 > max_palindrome and is_palindrome(n1 * n2):
            max_palindrome = n1 * n2

print max_palindrome