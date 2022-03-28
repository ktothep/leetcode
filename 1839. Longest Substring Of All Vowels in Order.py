word = "aeeeiiiioooauuuaeiou"
charmap={}
maxlen=0
for window_end in range(len(word)):
    if word[window_end]=='a' and window_end!=len(word)-1:
        if word[window_end+1] == 'a' or word[window_end+1]=='e' :
            if word[window_end] in charmap:
                charmap[word[window_end]]+=1
            else:
                charmap[word[window_end]] = 1
        else:

            charmap.clear()
    if word[window_end] == 'e' and window_end!=len(word)-1:
        if word[window_end + 1] == 'e' or word[window_end + 1] == 'i':
            if word[window_end] in charmap:
                charmap[word[window_end]] += 1
            else:
                charmap[word[window_end]] = 1
        else:

            charmap.clear()
    if word[window_end] == 'i' and window_end!=len(word)-1:
        if word[window_end + 1] == 'i' or word[window_end + 1] == 'o':
            if word[window_end] in charmap:
                charmap[word[window_end]] += 1
            else:
                charmap[word[window_end]] = 1
        else:

            charmap.clear()
    if word[window_end] == 'o' and window_end!=len(word)-1:
        if word[window_end + 1] == 'o' or word[window_end + 1] == 'u':
            if word[window_end] in charmap:
                charmap[word[window_end]] += 1
            else:
                charmap[word[window_end]] = 1
        else:

            charmap.clear()
    if word[window_end] == 'u' and window_end!=len(word)-1:
        if word[window_end + 1] == 'u':
            if word[window_end] in charmap:
                charmap[word[window_end]] += 1
            else:
                charmap[word[window_end]] = 1
        else:
            maxlen=max(maxlen,sum(list(charmap.values())))
            charmap.clear()

print(maxlen+1)



