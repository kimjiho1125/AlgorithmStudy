def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        #바로 다음 번호의 접두어와 일치하지 않으면 나머지 번호들과도 어차피 일치하지 않음을 이용(정렬을 했기 때문에)
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    
    return answer