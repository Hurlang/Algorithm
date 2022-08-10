T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    max_continue = 0
    cont = 0
    for i in range(N):
        if arr[i] :
            cont += 1
            if max_continue < cont:
                max_continue = cont
        else:
            cont = 0
    print(f'#{tc} {max_continue}')