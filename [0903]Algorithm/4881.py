for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    N = len(arr)

def perm(k, cur_sum):
    global ans
    if ans <= cur_sum: return
    if k == N:
       ans = min(ans, cur_sum)
         

    else :
        for i in range(k,N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k+1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(1, int(input()+1)):
    N = int (input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0,0)
    print(ans)