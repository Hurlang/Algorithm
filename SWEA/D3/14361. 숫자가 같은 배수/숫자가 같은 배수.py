#import sys;sys.stdin=open('숫자가 같은 배수.txt')
T = int(input())
for tc in range(1, T+1):
    N = input()
    N_list = sorted(list(map(int,N)))

    multiple =[]
    length = len(N)

    ans = 'impossible'
    for i in range(2, 10):
        if len(str(int(N)*i)) == length and sorted(list(map(int, str(int(N)*i)))) == N_list:
            ans = 'possible'
            break
    print(f'#{tc} {ans}')