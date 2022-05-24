text1 = "psnw"
text2="vozsh"

ptr1=0
ptr2=0
if len(text1) < len(text2):
    text1, text2 = text2, text1

while ptr1<len(text1):
    if text1[ptr1]==text2[ptr2]:
        ptr2+=1
    ptr1 += 1
print(ptr2)