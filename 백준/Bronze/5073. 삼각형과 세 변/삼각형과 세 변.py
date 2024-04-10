from collections import Counter

while True:
    cases = list(map(int, input().split()))

    #종료 조건 체크
    if cases[0] == 0 and cases[1] == 0 and cases[2] == 0:
        break

    #삼각형 조건 체크
    cases.sort(reverse=True)
    if cases[0] >= cases[1] + cases[2]:
        print('Invalid')
        continue
    
    #count 채우기
    number_of_count = len(Counter(cases))
    if number_of_count == 1:
        print('Equilateral')
    elif number_of_count == 2:
        print('Isosceles')
    elif number_of_count == 3:
        print('Scalene')


