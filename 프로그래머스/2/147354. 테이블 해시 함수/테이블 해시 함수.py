def solution(data, col, row_begin, row_end):
    answer = 0
    s = []
    #col번째 칼럼을 기준으로 오름차순으로 정렬, 값이 동일하다면 첫 번째 컬럼을 기준으로 내림차순으로 정렬
    data.sort(key=lambda x:(x[col-1],-x[0]))
    #각각의 S_i구하기
    for i in range(row_begin,row_end+1):
        sumN = 0
        for j in range(len(data[0])):
            sumN += (data[i-1][j] % i)
        s.append(sumN)
    #모든 S_i를 누적하여 bitwiseXOR 연산진행
    for i in range(len(s)):
        if i == 0:
            answer = s[i]
        else:
            answer ^= s[i]
    return answer