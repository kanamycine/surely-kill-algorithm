import sys
def preorder_traverse(T):
    if T:
        print("%d" % T, end =' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])


templ = list(map(int,input().split()))

for i in range(len(templ) // 2):
    parent, child = templ[i*2], templ[i*2*1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child


    
