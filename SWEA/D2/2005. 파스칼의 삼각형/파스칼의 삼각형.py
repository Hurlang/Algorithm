T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [1]
    print(f'#{tc}')
    print(*arr)
    for i in range(N-1):
        arr1 = [0] + arr
        arr2 = arr + [0]
        arr = arr + [0] # 개수 늘려줌
        for j in range(len(arr1)):
            arr[j] = arr1[j] + arr2[j]
        print(*arr)