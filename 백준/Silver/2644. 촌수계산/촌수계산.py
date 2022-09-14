def bfs(v):
    visited[v] = 0
    q = []
    q.append(v)

    while len(q) != 0:
        t = q.pop(0)
        for w in adj_list[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1

    if visited[E] == 0:
        return -1
    return visited[E]


N = int(input())
S, E = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
R = int(input())
for i in range(R):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
visited = [0] * (N+1)
print(bfs(S))

