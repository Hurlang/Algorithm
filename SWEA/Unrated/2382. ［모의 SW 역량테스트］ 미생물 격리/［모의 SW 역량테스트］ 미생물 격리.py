#import sys; sys.stdin = open('msm.txt')

d = [0, [-1, 0], [1, 0], [0, -1], [0, 1]]


def change_direction(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n == 3:
        return 4
    else:
        return 3


T = int(input())
for tc in range(1, T + 1):
    # setting
    N, M, K = map(int, input().split())
    arr = [list([] for __ in range(N)) for _ in range(N)]
    order = 0 # 움직인 군집과 아직 안움직인 군집을 비교하기위함
    for _ in range(K):
        i, j, num, direction = map(int, input().split())
        arr[i][j].append([num, direction, order])

    # ################
    # for item in arr:
    #     print(*item)
    # ################

    #  격리

    for _ in range(M):
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    for item in arr[i][j]: # arr[i][j] = [num, direction, order]
                        if item[2] == order:
                            ni = i + d[item[1]][0]
                            nj = j + d[item[1]][1]
                            item[2] = (item[2] + 1) % 2 # order = (order + 1) % 2 해주기

                            if ni == 0 or ni == N-1 or nj == 0 or nj == N-1: # 만약 테두리이면 (1)군집수 감소, (2)방향 바꾸기
                                item[0] //= 2
                                item[1] = change_direction(item[1])

                            if item[0] != 0: # 만약 소멸하지 않았다면
                                arr[ni][nj].append([item[0], item[1], item[2]])
                            arr[i][j].pop(0)

        # 이동 완료 후
        for i in range(N):
            for j in range(N):
                if arr[i][j]: # 겹친 군집 정리
                    total_num = 0
                    max_num = 0
                    strong_direction = 0
                    for item in arr[i][j]: # arr[i][j] = [num, direction, order]
                        total_num += item[0] # 개체수 더하기

                        if item[0] > max_num: # 방향설정
                            max_num = item[0]
                            strong_direction = item[1]


                    arr[i][j] = [[total_num, strong_direction, (order+1)%2]]
        order = (order + 1) % 2

    # 격리 종료 후
    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for item in arr[i][j]: # arr[i][j] = [num, direction, order]
                    total += item[0]

    print(f'#{tc} {total}')