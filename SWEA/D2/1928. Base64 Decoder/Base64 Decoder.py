#import sys; sys.stdin = open('Base64 Decoder.txt')
def s_to_dec(string):
    N = ord(string)
    if 65 <= N <= 90:
        return N - 65
    elif 97 <= N <= 122:
        return N - 71
    elif 48 <= N <= 57:
        return N + 4
    elif string == '+':
        return 62
    else:
        return 63

def dec_to_bin(num):
    if num == 1:
        return [1]
    return dec_to_bin(num//2) + [num%2]

def six_bit_maker(arr):
    while len(arr) != 6:
        arr = [0] + arr
    return ''.join(map(str, arr))

def bin_to_dec(bin):
    bin_arr = list(map(int, bin))
    total = 0
    
    for i in range(len(bin_arr)-1,-1,-1):
        total += bin_arr[7-i] * (1<<i)
    
    return total

def dec_to_s(dec):
    return chr(dec)



T = int(input())
for tc in range(1, T+1):
    arr = list(input())

    # 숫자를 6자리 2진수로 변환
    bits = ''
    for i in range(len(arr)):
        bits += six_bit_maker(dec_to_bin(s_to_dec(arr[i])))

    # 비트를 8개씩 끊어서 숫자로, 다시 숫자를 문자로 변환
    text = ''
    for i in range(len(bits)//8):
        text += dec_to_s(bin_to_dec(bits[8*i:8*i+8]))

    print(f'#{tc} {text}')
