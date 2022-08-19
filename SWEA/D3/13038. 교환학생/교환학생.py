T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    li = []
    for i in range(7):
        day = cnt = 0
        while N != cnt:
            cnt += arr[i]
            i = (i + 1) % 7
            day += 1
        li.append(day)

    print(f'#{tc} {min(li)}')