def solution(s):
    answer = []
    #주어진 문자열을 2차원 배열로 변환
    s = s[:-2].replace('{','').replace(',',' ').split('}')

    for i,v in enumerate(s):
            s[i] = v.split()
    
    #2차원 배열을 원소의 길이를 기준으로 오름차순 정렬 
    s.sort(key=len)
    # #반복문을 이용하여 최종 결과 구하기
    for t in s:
        for i in answer:
            t.remove(i)
        answer.append(t[0])
    
    answer = [int(i) for i in answer]
    
    return answer