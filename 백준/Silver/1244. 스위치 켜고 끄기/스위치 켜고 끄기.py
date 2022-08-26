N = int(input())
arr = list(map(int, input().split()))
student = int(input())
for i in range(student):
    gender, number = map(int, input().split())

    if gender == 1: # 남자이면
        for j in range(N):
            if (j+1) % number == 0:
                if arr[j]: arr[j] = 0   # 0 -> 1
                else: arr[j] = 1        # 1 -> 0

    else: # 여자이면
        if arr[number-1]: arr[number-1] = 0
        else: arr[number-1] = 1

        j = 1
        while True:
            if 0<=number-1-j<N and 0<=number-1+j<N and arr[number-1-j] == arr[number-1+j]:

                if arr[number-1-j]:
                    arr[number-1-j] = 0
                    arr[number-1+j] = 0
                else:
                    arr[number-1-j] = 1
                    arr[number-1+j] = 1

                j += 1
            else:
                break
for i in range(len(arr)):
    print(arr[i], end=' ')
    if (i+1)%20 == 0:
        print()
