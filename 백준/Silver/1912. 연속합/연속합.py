N = int(input()) # 숫자의 갯수
arr = list(map(int, input().split())) # 배열
max_value = max(arr)

shorten = []
s = 0
sign = 1
for i in range(N):
    if s == 0:
        if arr[i] > 0:
            sign = 1
        elif arr[i] < 0:
            sign = -1

    if (sign == 1 and arr[i] > 0) or (sign == -1 and arr[i] < 0):
        s += arr[i]
    elif (sign == -1 and arr[i] > 0) or (sign == 1 and arr[i] < 0):
        shorten.append(s)
        s = arr[i]
        sign *= -1
shorten.append(s)


N2 = len(shorten)
for i in range(N2-2):
    if shorten[i] > 0 and shorten[i+2] < shorten[i] + shorten[i+1] + shorten[i+2]:
        shorten[i+2] = shorten[i] + shorten[i+1] + shorten[i+2]
max_value = max(max_value, max(shorten))
print(max_value)
