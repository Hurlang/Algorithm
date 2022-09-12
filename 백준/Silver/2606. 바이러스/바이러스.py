def dfs(v):
    global cnt
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)
            cnt += 1

T = int(input()) # 컴퓨터의 수
N = int(input())
visited = [0] * (T+1)
adj_list = [[] for _ in range(T+1)]
for i in range(N):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
# print(adj_list)
cnt = 0
dfs(1)

print(cnt)