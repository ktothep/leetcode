chars = ["a", "a", "a", "a", "a", "b"]
p1, p2 = 0, 1
count = 1
curr = chars[0]
while p2 < len(chars):
    if chars[p2] == curr:
        count += 1
    else:
        chars[p1] = curr
        p1 += 1
        if count > 1:
            for c in str(count):
                chars[p1] = c
                p1 += 1
        count = 1
        curr = chars[p2]
    p2 += 1
chars[p1] = curr
if count == 1:
     print(p1 + 1)
else:
    p1 += 1
    for c in str(count):
        chars[p1] = c
        p1 += 1

