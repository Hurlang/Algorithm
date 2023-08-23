def solution(arr):
    answer = []
    num = -1
    for i in range(len(arr)):
        if arr[i] != num:
            answer.append(arr[i])
            num = arr[i]
    return answer