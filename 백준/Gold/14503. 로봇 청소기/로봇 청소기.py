N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 0
p = 2
while True:
    # 현재 위치를 청소한다. (이미 청소되어있는 칸이라면 skip)
    if arr[r][c] < 2:
        arr[r][c] = p
        cnt += 1
        p += 1

    # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향을 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    # b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    flag = False
    for k in range(4):
        ni = r + di[(d + (3 * (k + 1))) % 4]
        nj = c + dj[(d + (3 * (k + 1))) % 4]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            r, c = ni, nj
            d = (d + (3 * (k + 1))) % 4
            flag = True
            break

    if flag:
        continue


    # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진할 수 없는 경우에는 작동을 멈춘다.
    ni = r + di[(d + 2) % 4]
    nj = c + dj[(d + 2) % 4]
    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
        break

    r, c = ni, nj

print(cnt)

# for item in arr:
#     for i in item:
#         print(i, end="      ")
#     print()
