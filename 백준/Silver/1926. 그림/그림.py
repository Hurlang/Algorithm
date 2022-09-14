n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j):
    global max_v
    v = 0
    q.append([i, j])

    while q:
        t = q.pop(0)
        i = t[0]
        j = t[1]
        v += 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 1:
                q.append([ni, nj])
                arr[ni][nj] += 1

    if max_v < v :
        max_v = v


max_v = 0
cnt = 0

q = []
visited = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            arr[i][j] += 1
            bfs(i, j)

print(cnt)
print(max_v)