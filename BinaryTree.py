from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Constructed Binary Tree
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g

rev=[]
#Breadth First Traversal
def breadthfirst(root):
    q=[root]
    while q:
        x=q.pop(0)
        print(x.value)
        if x.left:
            q.append(x.left)
        if x.right:
            q.append(x.right)
#Breadth First Traversal Reverse
def breadthfirst_reverse(root):
    q=deque()
    q.append(root)
    while q:
        x=q.popleft()
        rev.append(x.value)
        if x.right:
            q.append(x.right)
        if x.left:
            q.append(x.left)
    while rev:
        print(rev.pop())

def average(root):
    q=deque()
    q.append(root)
    res=[]
    while q:
        level=len(q)
        sum=0
        for _ in range((level)):
            y=q.popleft()
            sum+=y.value
            if y.left:
                q.append(y.left)
            if y.right:
                q.append(y.right)
        avg=sum/level
        res.append(avg)
    print(res)

def mindepth(root):
    q=deque()
    q.append(root)
    depth=0
    while q:
        depth+=1
        level=len(q)
        for _ in range(level):
            x=q.popleft()
            if not x.left and not x.right:
                return depth
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)

def levelorder(root,key):
    q = deque()
    q.append(root)
    flag=0
    while q:
        level = len(q)
        for _ in range(level):
            x = q.popleft()
            if flag==1:
                return x.value
            if x.value==key:
                flag=1
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)

def rightview(root):
    q=deque()
    q.append(root)
    res=[]
    while q:
        level=len(q)
        for i in range(level):
            x=q.popleft()
            if i==level-1:
                res.append(x.value)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
    print(res)

#breadthfirst(a)
#breadthfirst_reverse(a)
#average(a)
#print(mindepth(a))
#print(levelorder(a,3))
rightview(a)

