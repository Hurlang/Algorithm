def dfs(x, y, k, num):
    if k == 6:
        t.add(num)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, k+1, num * 10 + arr[nx][ny])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, arr[i][j])

    print(f'#{tc} {len(t)}')