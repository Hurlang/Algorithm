# #import sys;sys.stdin=open('숫자가 같은 배수.txt')
# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     N_list = sorted(list(map(int,N)))
#
#     multiple =[]
#     length = len(N)
#
#     ans = 'impossible'
#     for i in range(2, 10):
#         if len(str(int(N)*i)) == length and sorted(list(map(int, str(int(N)*i)))) == N_list:
#             ans = 'possible'
#             break
#     print(f'#{tc} {ans}')

#import sys;sys.stdin=open('숫자가 같은 배수.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    length = len(str(N))
    cnt = [0] * 10

    for num in list(map(int,str(N))):
        cnt[num] += 1

    ans = 'impossible'
    i = 2
    while len(str(N*i)) == length:
        cnt2 = [0] * 10
        for num in list(map(int,str(N*i))):
            cnt2[num] += 1
        if cnt == cnt2:
            ans = 'possible'
            break
        i += 1

    print(f'#{tc} {ans}')