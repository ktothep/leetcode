N=2
ans=[]
def bracket(res,opening_bracket,closing_bracket,i):
    if i==2*N:
        print(res)
        return
    if opening_bracket<N:
        bracket(res+'(',opening_bracket+1,closing_bracket,i+1)
    if closing_bracket<opening_bracket:
        bracket(res+')',opening_bracket,closing_bracket+1,i+1)


bracket("",0,0,0)
