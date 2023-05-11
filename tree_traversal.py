def inorder(x, key, left, right):
    if left[x] != -1:
        inorder(left[x], key, left, right)
    
    print(key, end=" ")
    
    if right[x] != -1:
        inorder(right[x], key, left, right)
    return

def preorder(x, key, left, right):
    print(key, end=" ")
    if left[x] != -1:
        preorder(left[x], key, left, right)
    if right[x] != -1:
        preorder(right[x], key, left, right)
    return

def postorder(x, key, left, right):
    if left[x] != -1:
        postorder(left[x], key, left, right)
    if right[x] != -1:
        postorder(right[x], key, left, right)
    print(key, end=" ")
    return

n = int(input())
key, left, right = [], [], []

for i in range(n):
    k, l, r = list(map(int, input().split()))
    key.append(k)
    left.append(l)
    right.append(r)

inorder(0, key, left, right)