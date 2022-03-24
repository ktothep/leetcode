n = 5
k = 73
chars = ['a'] * n

for i in range(n - 1, -1, -1):

    val = k - (i)

    if val >= 26:
        chars[i] = 'z'
        k -= 26
    else:
        chars[i] = chr(ord('a') + val - 1)
        k -= val

print(''.join(chars))