from collections import deque
T = 10
for tc in range(1, T+1):
    def bfs(s):
        q = deque()
        q.append(s)
        visited[s] = 1
        while q:
            t = q.popleft()
            for i in contact_arr[t]:
                if not visited[i]:
                    q.append(i) # [7, 15]
                    visited[i] = visited[t] + 1
 
    n, start = map(int ,input().split())
    arr = list(map(int, input().split()))
    contact_arr = [[] for _ in range(101)] # [[], [17, 8, 7], [7, 15], [22], [10, 2], [], [2], [1], [], [], [], [6], [], [], [], [4], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for i in range(0, len(arr), 2): # 0 2 4 6 8 10 12 ... 22
        contact_arr[arr[i]].append(arr[i+1])
    visited = [0] * 101
    
    
    bfs(start)


    Max = 0
    for i in range(len(visited)):
        if visited[i] >= max(visited):
            Max = i
    print(f'#{tc} {Max}')