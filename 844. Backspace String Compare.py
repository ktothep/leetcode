import itertools



def Build(S):
       ans=[]
       flag=0
       for c in reversed(range(len(S))):
           if S[c]=="#":
               flag+=1
           elif flag!=0:
               flag-=1
           else:
               ans.append(S[c])
       return ''.join(ans)



print(Build("ab#c")==Build("ad#c"))