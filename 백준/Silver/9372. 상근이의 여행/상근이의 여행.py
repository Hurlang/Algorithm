#import sys; sys.stdin=open('상근이의여행.txt')
def dfs(v):
    global cnt
    if not visited[v]:
        visited[v] = 1
        cnt += 1
        if visited.count(1) == N:
            return
        for w in adj_list[v]:
            dfs(w)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    visited = [0] * (N+1)
    adj_list = [[] for _ in range(M+2)]
    cnt = -1
    for i in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    dfs(1)
    print(cnt)