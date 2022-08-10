
T = int(input())

for tc in range(T):
    N = int(input())
    cnt = [0] * 101
    arr = list(map(int, input().split()))

    for num in arr:
        cnt[num] += 1


    max_idx = 0
    for i in range(len(cnt)):
        if cnt[i] >= cnt[max_idx] :
            max_idx = i

    print(f'#{N} {max_idx}')
