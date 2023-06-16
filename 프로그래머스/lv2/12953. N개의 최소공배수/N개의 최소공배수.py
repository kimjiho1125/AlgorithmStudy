def solution(arr):
    arr.sort()
    bigNum = arr[len(arr)-1]
    i = 1
    lenArr = len(arr)
    while True:
        currentNum = bigNum * i
        temp = 0
        for num in arr:
            if currentNum % num == 0:
                temp += 1
            else:
                break
        #종료 조건 체크
        if temp == lenArr:
            return currentNum
        i += 1
        