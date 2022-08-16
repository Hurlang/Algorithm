#import sys; sys.stdin=open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(input()))

    ans = 'possible'
    same = ''
    diff = ''
    for i in range(N):
        flag = False
        for j in range(M):
            if arr[i][j] == '#' or arr[i][j] == '.':
                if i%2 == j%2:
                    same = arr[i][j]
                else:
                    diff = arr[i][j]

    if same:
        diff = '.' if same == '#' else '#'
    elif diff:
        same = '.' if diff == '#' else '#'

    for i in range(N):
        for j in range(M):
            if i%2 == j%2 and arr[i][j] == diff:
                ans = 'impossible'
            elif i%2 != j%2 and arr[i][j] == same:
                ans = 'impossible'

    print(f'#{tc} {ans}')