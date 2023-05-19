def solution(survey, choices):
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }
    answer = ""
    # 설문 결과에 따른 각 성격 유형별 점수 구하기
    for types, choice in zip(survey, choices):
        notAgree = types[0]
        agree = types[1]
        if choice == 1:
            scores[notAgree] += 3
        elif choice == 2:
            scores[notAgree] += 2
        elif choice == 3:
            scores[notAgree] += 1
        elif choice == 5:
            scores[agree] += 1
        elif choice == 6:
            scores[agree] += 2
        elif choice == 7:
            scores[agree] += 3
    #1번 지표 성격 유형 구하기
    if scores['R'] > scores['T']:
        answer += 'R'
    elif scores['R'] < scores['T']:
        answer += 'T'
    elif scores['R'] == scores['T']:
        answer += 'R'
    #2번 지표 성격 유형 구하기
    if scores['C'] >= scores['F']:
        answer += 'C'
    elif scores['C'] < scores['F']:
        answer += 'F'
    #3번 지표 성격 유형 구하기
    if scores['J'] >= scores['M']:
        answer += 'J'
    elif scores['J'] < scores['M']:
        answer += 'M'
    #4번 지표 성격 유형 구하기
    if scores['A'] >= scores['N']:
        answer += 'A'
    elif scores['A'] < scores['N']:
        answer += 'N'
    #정답 반환
    return answer