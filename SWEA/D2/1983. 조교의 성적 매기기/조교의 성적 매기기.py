T = int(input())
scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    
    for i in range(N):
        a, b, c = map(int, input().split())
        arr.append(a * 0.35 + b * 0.45 + c * 0.2)
    
    K_score = arr[K-1]
    
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    for i in range(len(arr)):
        if arr[i] == K_score:
            break
    
    print(f'#{tc} {scores[i // (N // 10)]}')