#import sys; sys.stdin = open('암호생성기.txt')
for t in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    flag = True
    while flag:
        for i in range(1, 6):
            poped = arr.pop(0) - i
            if poped <= 0:
                arr.append(0)
                flag = False
                break
            else:
                arr.append(poped)

    print(f'#{tc}', end= ' ')
    for i in range(8):
        print(arr[i], end = ' ')
    print()