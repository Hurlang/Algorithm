def comb(n, r, k, s):
    global p
    if k == r:
        cnt = 0
        for char in p:
            if char in vowels:
                cnt += 1
        if 1 <= cnt < r-1:
            print(p)

    else:
        for i in range(s, n-r+1+k):
            p += arr[i]
            comb(n, r, k+1, i+1)
            p = p[:-1]


L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
vowels = 'aeiou'
p = ''
ans = []
comb(C, L, 0, 0)