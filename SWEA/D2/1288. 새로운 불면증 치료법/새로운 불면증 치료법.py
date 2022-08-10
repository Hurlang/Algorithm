#import sys; sys.stdin = open('새로운 불면증 치료법_input.txt')
T = int(input())

for tc in range(1, T+1):
    arr = [0] * 10

    N = int(input())

    i = 1
    while True:
        KN = str(N * i)
        for num in KN:
            arr[int(num)] += 1

        mul = 1
        for j in range(len(arr)):
            mul *= arr[j]

        if mul != 0:
            break

        i += 1
    print(f'#{tc} {KN}')
