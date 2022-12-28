N, L = map(int, input().split())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()

s = 0 # 널빤지 시작
e = 0 # 널빤지 끝
board_cnt = 0 # 널빤지 개수
board_sum = 0 # 널빤지 누적 개수
for i in range(N):
    s = max(s, arr[i][0])
    e = max(e, arr[i][1])

    if (e-s) % L:
        board_cnt = (e-s) // L + 1
    else:
        board_cnt = (e - s) // L

    board_sum += board_cnt
    e = s + board_cnt * L

    s = e

print(board_sum)