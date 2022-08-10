T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        cnt_x = 0

        for j in range(M):
            if arr[i][j]:
                cnt_x += 1
                if max_cnt < cnt_x:
                    max_cnt = cnt_x
            else:
                cnt_x = 0

    for i in range(M):
        cnt_y = 0
        for j in range(N):
            if arr[j][i]:
                cnt_y += 1
                if max_cnt < cnt_y:
                    max_cnt = cnt_y
            else:
                cnt_y = 0

    print(f'#{tc} {max_cnt}')