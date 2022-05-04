from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Constructed Binary Tree
a=Node(4)
b=Node(2)
c=Node(6)
d=Node(1)
e=Node(3)

a.left=b
a.right=c
b.left=d
b.right=e


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

def sumLeftLeaves(root):
    q=deque()
    q.appendleft(root)
    sum=0
    while q:
        level=len(q)
        for i in range(level):
            x=q.popleft()
            if  x.left and not x.left.left and not x.left.right:
                sum+=x.value
            if x.left:
                 q.append(x.left)
            if x.right:
                q.append(x.right)
    print(sum)

def minDistanceNode(root):
    q = deque()
    q.appendleft(root)
    mini_value = float('inf')
    while q:
        x=q.popleft()
        if x.left:
            mini_value=min(abs(x.value-x.left.value),mini_value)
            q.append(x.left)
        if x.right:
            mini_value=min(abs(x.value-x.right.value),mini_value)
            q.append(x.right)
    return mini_value

def pathSum(root,targetSum):
    q=deque()
    q.appendleft((root,root.value))
    while q:
        x, x_val = q.popleft()
        if x_val == targetSum and not x.left and not x.right:
            return True
        if x.left:
            q.append((x.left, x_val + x.left.val))
        if x.right:
            q.append((x.right, x_val + x.right.val))
#breadthfirst(a)
#breadthfirst_reverse(a)
#average(a)
#print(mindepth(a))
#print(levelorder(a,3))
#rightview(a)
#(minDistanceNode(a))
pathSum(a,9)

