from collections import deque
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(i, j):
    global max_distance
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > max_distance:
                    max_distance = visited[nx][ny]


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_distance = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            bfs(i, j)
print(max_distance - 1)