#import sys; sys.stdin=open('파리퇴치.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for row in range(N):
        arr.append(list(map(int, input().split())))

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M):
                for l in range(M):
                    kill += arr[i+k][j+l]

            if kill > max_kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')