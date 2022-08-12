#import sys; sys.stdin = open('GNS_test_input.txt')

def a_to_sorted_a(arr):

    # 문자열 -> 숫자로 변경하기 위한 딕셔너리
    GNS_dict = {
        "ZRO" : 0 ,
        "ONE" : 1 ,
        "TWO" : 2 ,
        "THR" : 3 ,
        "FOR" : 4 ,
        "FIV" : 5 ,
        "SIX" : 6 ,
        "SVN" : 7 ,
        "EGT" : 8 ,
        "NIN" : 9 ,
    }

    N = len(arr) # 리스트의 길이
    num_arr = [0] * N

    # 문자를 숫자로 변경
    for i in range(N):
        num_arr[i] = GNS_dict[arr[i]]

    # 카운팅 정렬
    cnt = [0] * 10 # 0 ~ 9 카운팅

    for num in num_arr:
        cnt[num] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    sorted_arr = [0] * N
    for i in range(N):
        cnt[num_arr[i]] -= 1
        sorted_arr[cnt[num_arr[i]]] = arr[i]

    return sorted_arr

T = int(input())
for tc in range(1, T+1):
    t, length = input().split()
    arr = list(input().split())

    print(f'{t}')
    print(f'{" ".join(a_to_sorted_a(arr))}')