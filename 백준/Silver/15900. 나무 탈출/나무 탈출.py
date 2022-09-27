# def dfs(v, n): # v: 방문지점, n: 루트노드와 거리
#     global cnt
#
#     visited[v] = 1
#     flag = True
#     for w in adj_list[v]:
#         if visited[w] == 0:
#             flag = False
#             dfs(w, n+1)
#     if flag:
#         cnt += 1
#
#
# N = int(input())
# adj_list = list([] for _ in range(N+1))
# visited = [0] * (N+1)
# for i in range(N-1):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#     adj_list[b].append(a)
#
# cnt = 0
# dfs(1, 0)
#
# if cnt % 2 == 0:
#     print('No')
# else:
#     print('Yes')

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        w = q.pop()
        flag = True
        for ww in adj_list[w]:
            if visited[ww] == 0: # 방문안했으면
                flag = False
                q.append(ww)
                visited[ww] = visited[w] + 1
        if flag:
            leaf[w] = 1


N = int(input())
adj_list = list([] for _ in range(N+1))
visited = [0] * (N+1)
leaf = [0] * (N+1)
for i in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

bfs(1)

total = 0
for i in range(N+1):
    if leaf[i]:
        total += visited[i] - 1

if total % 2 == 0:
    print('No')
else:
    print('Yes')