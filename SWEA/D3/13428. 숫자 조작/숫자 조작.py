#import sys; sys.stdin = open('숫자조작.txt')
T = int(input())
for tc in range(1, T+1):
    N = list(input())
    numbers = []
    for i in range(len(N)):
        for j in range(len(N)):
            arr = N[:]
            arr[i], arr[j] = arr[j], arr[i]
            num = int(''.join(arr))
            if len(N) == len(str(num)):
                numbers.append(num)

    min_value = 999999999
    max_value = 0
    for i in range(len(numbers)):
        if max_value < numbers[i]:
            max_value = numbers[i]
        if min_value > numbers[i]:
            min_value = numbers[i]

    print(f'#{tc} {min_value} {max_value}')