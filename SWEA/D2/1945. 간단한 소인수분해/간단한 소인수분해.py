# 간단한 소인수 분해

arr = [2, 3, 5, 7, 11]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    cnt = [0] * 5
    idx = 0
    
    while N > 0:
        if idx ==5:
            break
        
        if N % arr[idx] == 0:
            cnt[idx] += 1
            N = N // arr[idx]
        else:
            idx += 1

    print(f'#{tc} {" ".join(map(str, cnt))}')