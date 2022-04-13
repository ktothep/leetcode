s = "Let's take LeetCode contest"
res = ""
s = s.split(" ")
for x in range(len(s)):
    res += s[x][::-1]
    if x != len(s) - 1:
        res += " "

print(res)