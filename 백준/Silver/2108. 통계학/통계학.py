import sys
N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for i in range(N)]

arr.sort()

#산술평균
print(round(sum(arr)/len(arr)))

#중앙값
print(arr[len(arr)//2])

#최빈값
cnt = [0] * 8001
for num in arr:
    cnt[num+4000] += 1

max_freq = max(cnt)
max_freq_idx_lst = []
if cnt.count(max_freq) > 1:
    for idx, num in enumerate(cnt):
        if num == max_freq:
            max_freq_idx_lst.append(idx)
        if len(max_freq_idx_lst) == 2:
            print(max_freq_idx_lst[-1]-4000)
            break
    
else:
    print(cnt.index(max_freq)-4000)

#범위
print(arr[-1]-arr[0])