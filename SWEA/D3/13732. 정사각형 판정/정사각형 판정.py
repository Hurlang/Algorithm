#import sys; sys.stdin = open('정사각형 판정.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    min_i = N
    max_i = 0
    min_j = N
    max_j = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if i < min_i : min_i = i
                if i > max_i : max_i = i
                if j < min_j : min_j = j
                if j > max_j : max_j = j

    ans = 'yes'
    for i in range(N):
        for j in range(N):
            if min_i <= i <= max_i and min_j <= j <= max_j and arr[i][j] == '.':
                ans = 'no'

    if (max_i - min_i) != (max_j - min_j):
        ans = 'no'

    print(f'#{tc} {ans}')