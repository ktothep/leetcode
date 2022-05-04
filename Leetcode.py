class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Constructed Binary Tree
a=Node("1")
b=Node("2")
c=Node("3")
d=Node("4")


a.left=b
a.right=c
b.right=d
ans=[]
def parserTree(node,res):
    if not node.left and not node.right:
        res.append(node.value)
        print(res)
        ans.append(res.copy())
        return
    res.append(node.value)
    if node.left :
        parserTree(node.left,res)
        res.pop()
    if node.right :
        parserTree(node.right,res)
        res.pop()
parserTree(a,[])
print(ans)
