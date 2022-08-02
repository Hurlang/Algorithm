def direction(N):
    if N == 1:
        return [1]
    arr = [N]
    for i in range(N-1,0,-1):
        arr += [i, i]
    return arr

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0 for i in range(N)] for j in range(N)]
    direct = direction(N)
    i = 0
    j = -1
    k = 0
    for idx, steps in enumerate(direct):
        if idx % 4 == 0:
            for step in range(steps):
                j += 1
                k += 1
                arr[i][j] = k
                
            
        elif idx % 4 == 1:
            for step in range(steps):
                i += 1
                k += 1
                arr[i][j] = k
            
        elif idx % 4 == 2:
            for step in range(steps):
                j -= 1
                k += 1
                arr[i][j] = k
                
            
        else:
            for step in range(steps):
                i -= 1
                k += 1
                arr[i][j] = k
                
            
    print(f'#{test_case}')
    
    for row in arr:
        print(' '.join(list(map(str,row))))