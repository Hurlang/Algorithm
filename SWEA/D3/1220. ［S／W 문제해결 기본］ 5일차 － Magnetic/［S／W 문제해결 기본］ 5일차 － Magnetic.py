#import sys; sys.stdin = open('Magnetic.txt')
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if stack:
                if arr[j][i] != stack[-1] and arr[j][i] != 0:
                    stack.append(arr[j][i])
            else:
                if arr[j][i] == 1:
                    stack.append(1)
        cnt += len(stack) // 2

    print(f'#{tc} {cnt}')