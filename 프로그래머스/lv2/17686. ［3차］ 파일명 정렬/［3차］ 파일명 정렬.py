def solution(files):
    answer = []
    sp = []
    
    for idx, file in enumerate(files):
        #해당 파일의 인덱스, HEAD, NUMBER의 정보를 담을 리스트 초기화
        sp.append([idx,'',''])
        #대소문자 구분X
        file = file.lower()
        number_section = False
        number_counter = 0
        for s in file:
            
            #NUMBER의 최대길이는 5이므로 체크해준다.
            if number_counter == 5:
                break
                
            if s.isdigit():
                number_section = True
                number_counter += 1
                sp[-1][2] += s
            else:
                #숫자를 만난 이후에 숫자가 아닌게 나왔으면 break
                if number_section:
                    break
                #number를 만나기 이전이면 무조건 HEAD
                sp[-1][1] += s
        #나중에 NUMBER의 대소 비교를 위해 문자열 -> 숫자로 변경
        sp[-1][2] = int(sp[-1][2])
    
    #주어진 조건대로 HEAD, NUMBER, index순서대로 우선순위를 두어 정렬한다.
    sp = sorted(sp, key=lambda x: (x[1],x[2],x[0]),)
    
    for file in sp:
        answer.append(files[file[0]])
             
    return answer