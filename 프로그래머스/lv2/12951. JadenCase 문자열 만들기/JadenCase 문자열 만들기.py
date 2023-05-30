def solution(s):
    answer = " ".join(word[0].upper() + word[1:].lower() if word != "" and word[0].isalpha() else word.lower() for word in s.split(" "))
   
    return answer