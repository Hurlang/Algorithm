#import sys; sys.stdin = open('오목판정.txt')
def f():
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    return 'YES'
                cnt = 0
        if cnt >= 5:
            return 'YES'

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    return 'YES'
                cnt = 0
        if cnt >= 5:
            return 'YES'

    # 대각선
    diag1 = {}
    diag2 = {}
    for i in range(N):
        for j in range(N):
            if diag1.get(i+j):
                diag1[i+j].append(arr[i][j])
            else:
                diag1[i+j] = [arr[i][j]]

            if diag2.get(i-j):
                diag2[i-j].append(arr[i][j])
            else:
                diag2[i-j] = [arr[i][j]]
    
    # 159
    for row in diag1.values():
        cnt = 0
        for item in row:
            if item == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    return 'YES'
                cnt = 0
        if cnt >= 5:
            return 'YES'

    # 357
    for row in diag2.values():
        cnt = 0
        for item in row:
            if item == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    return 'YES'
                cnt = 0
        if cnt >= 5:
            return 'YES'

    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc} {f()}')
