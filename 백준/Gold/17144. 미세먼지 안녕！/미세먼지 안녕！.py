di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def diffuse(i, j):
    cnt = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
            cnt += 1
            narr[ni][nj] += arr[i][j] // 5
    narr[i][j] += arr[i][j] - cnt * (arr[i][j] // 5)


rd = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상, 우, 하, 좌
ld = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 하, 우, 상, 좌
def move(r, c, d):
    if not d:       # 시계 방향이면
        k = 0
        pr, pc = r, c
        while k != 4:
            nr, nc = pr + rd[k][0], pc + rd[k][1]
            while 0 <= nr < r+1 and 0 <= nc < C and arr[nr][nc] != -1:
                if arr[pr][pc] != -1:
                    narr[pr][pc] = narr[nr][nc]
                pr, pc = nr, nc
                nr, nc = pr + rd[k][0], pc + rd[k][1]
            k += 1
        narr[pr][pc] = 0
    else:           # 반시계 방향이면
        k = 0
        pr, pc = r, c
        while k != 4:
            nr, nc = pr + ld[k][0], pc + ld[k][1]
            while r <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                if arr[pr][pc] != -1:
                    narr[pr][pc] = narr[nr][nc]
                pr, pc = nr, nc
                nr, nc = pr + ld[k][0], pc + ld[k][1]
            k += 1
        narr[pr][pc] = 0
R, C, T = map(int, input().split()) # R: 세로, C: 가로, T: 시간
arr = [list(map(int, input().split())) for _ in range(R)]
purifiers = {}


for t in range(T):                          # T 회
    narr = [[0] * C for _ in range(R)]
    for i in range(R):                      # 미세먼지 확산
        for j in range(C):
            if arr[i][j] == -1:
                purifiers[i, j] = [i, j]
                narr[i][j] = -1
            elif arr[i][j]:
                diffuse(i, j)

    # for item in narr:
    #     print(*item)
    # print()

    # print(purifiers.values())                       # 공기청정기 작동
    d_changer = 0                                   # 시계 <-> 반시계
    for purifier in purifiers.values():
        r, c = purifier
        move(r, c, d_changer)
        d_changer = (d_changer + 1) % 2

    arr = narr[:]

s = 0
for item in narr:
    # print(*item)
    for i in item:
        if i != -1:
            s += i
print(s)