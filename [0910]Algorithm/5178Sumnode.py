def dfs(idx):
    
    if idx > N + 1: return 0
    if Tree[idx]: return Tree[idx]
    left = idx*2
    right = left+1
    Tree[idx] = dfs(left) + dfs(right)
    return Tree[idx]
 
 
for t in range(int(input())):
    N, M, L = map(int, input().split())
    Tree = [0 for _ in range(N+2)]
    for i in range(M):
        node, value = map(int, input().split())
        Tree[node] = value
    result = dfs(L)
    print('#{} {}'.format(t+1, result))