#import sys; sys.stdin = open('팔씨름.txt')
T = int(input())
for tc in range(1, T+1):
    ox = input()
    played = len(ox)

    win = 0
    for result in ox:
        if result == 'o':
            win += 1

    ans = 'YES' if 15 - played + win >= 8 else 'NO'

    print(f'#{tc} {ans}')