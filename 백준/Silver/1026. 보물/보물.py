from collections import deque
N = int(input())                                    # 배열의 길이
A = deque(sorted(list(map(int, input().split()))))  # 배열 A
B = list(map(int, input().split()))                 # 배열 B

A2 = [-1] * N                                       # 재배열한 A : 초기값: [-1, -1, -1, ... ]
for i in range(N):                                  # A2의 원소를 N번 바꿔줘야함
    max_idx = 0                                         # B 배열에서 최대값 idx를 저장하기 위한 변수
    max_value = 0                                       # B 배열에서 최대값을 저장하기 위한 변수
    for j in range(N):                                  # B 배열 순회
        if B[j] >= max_value and A2[j] == -1:               # B의 j번째 인덱스 값이 max_value보다 크고, A2에 할당되지 않은 상태라면
            max_value = B[j]                                    # 최대값 저장
            max_idx = j                                         # 최대값 idx 저장

    A2[max_idx] = A.popleft()                           # B배열의 최대값 위치에 A배열의 최소값을 할당

s = 0                                               # 합
for i in range(N):
    s += A2[i] * B[i]

print(s)
