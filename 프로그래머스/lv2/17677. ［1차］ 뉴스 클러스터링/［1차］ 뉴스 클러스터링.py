def solution(str1, str2):
    #대소문자를 구분하지 않으므로
    str1 = str1.lower()
    str2 = str2.lower()
    
    s1 = []
    s2 = []
    
    #알파벳을 제외한 나머지 제거 + 다중집합 생성
    for i in range(len(str1)):
        if i == len(str1)-1: break
        if str1[i].isalpha() == False or str1[i+1].isalpha()==False: continue
        else: s1.append(str1[i]+str1[i+1])
    
    for i in range(len(str2)):
        if i == len(str2)-1: break
        if str2[i].isalpha()==False or str2[i+1].isalpha()==False: continue
        else: s2.append(str2[i]+str2[i+1]) 
    
    #합집합 구하기
    s1_copy = s1.copy()
    union = s1.copy()
    for i in s2:
        union.append(i) if i not in s1_copy else s1_copy.remove(i)
    
    #교집합 구하기
    intersection = []
    for i in s2:
        if i in s1: 
            s1.remove(i)
            intersection.append(i)
            
    return (65536 if len(union)==0 else int(len(intersection)/len(union)*65536))