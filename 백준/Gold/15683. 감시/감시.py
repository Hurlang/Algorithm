d1 = [[[1, 0]], [[0, 1]], [[-1, 0]], [[0, -1]]]                                                                         # 상, 우, 하, 좌 (4)
d2 = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]]                                                                             # 가로, 세로 (2)
d3 = [[[1, 0], [0, 1]], [[0, 1], [-1, 0]], [[-1, 0], [0, -1]], [[0, -1], [1, 0]]]                                       # 상우, 우하, 하좌, 좌상 (4)
d4 = [[[1, 0], [0, 1], [-1, 0]], [[0, 1], [-1, 0], [0, -1]], [[-1, 0], [0, -1], [1, 0]], [[0, -1], [1, 0], [0, 1]]]     # 상우하, 우하좌, 하좌상, 좌상우 (4)
d5 = [[[1, 0], [0, 1], [-1, 0], [0, -1]]]                                                                               # 상우하좌 (1)
d = [0, d1, d2, d3, d4, d5]


def dfs(n, r):
    global max_cnt, cnt
    if n == r:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    k = len(d[cctvs[r][0]])
    l = len(d[cctvs[r][0]][0])
    for i in range(k):
        for j in range(l):
            ni, nj = cctvs[r][1] + d[cctvs[r][0]][i][j][0], cctvs[r][2] + d[cctvs[r][0]][i][j][1]   # 방문
            while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = -1 * (r + 1)
                    cnt += 1
                ni += d[cctvs[r][0]][i][j][0]
                nj += d[cctvs[r][0]][i][j][1]

        dfs(n, r+1)

        for j in range(l):                                                                          # 방문 해제
            ni, nj = cctvs[r][1] + d[cctvs[r][0]][i][j][0], cctvs[r][2] + d[cctvs[r][0]][i][j][1]
            while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                if arr[ni][nj] == -1 * (r + 1):
                    arr[ni][nj] = 0
                    cnt -= 1
                ni += d[cctvs[r][0]][i][j][0]
                nj += d[cctvs[r][0]][i][j][1]


N, M = map(int, input().split())                            # N: 세로, M: 가로
arr = [list(map(int, input().split())) for _ in range(N)]   # 입력 배열
max_cnt = 0
cnt = 0                                                     # 차지 공간: 카메라, 벽, 감시영역의 개수 (사각지대 제외)
cctvs = []                                                  # cctv의 종류와 좌표를 담는 배열
for i in range(N):                                          # 방을 순회하면서
    for j in range(M):
        if 0 < arr[i][j] <= 6:                              # 빈공간이 아니라면
            if arr[i][j] != 6:                              # (그리고 카메라라면)
                cctvs.append([arr[i][j], i, j])             # (cctvs 배열에 [카메라의 종류, 좌표]를 append)
            cnt += 1                                        # 차지 공간 +1
cctvs.sort(reverse=True)                                    # 카메라의 번호가 높은 순서대로 정렬

n = len(cctvs)
dfs(n, 0)

# for item in arr:
#     print(*item)
# print()

print(N * M - max_cnt)