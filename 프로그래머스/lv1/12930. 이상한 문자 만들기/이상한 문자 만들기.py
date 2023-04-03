def solution(s):
    s = list(s.split(' '))
    answer = []
    for string in s:
        string = list(string)
        for i in range(len(string)):
            if(i % 2 == 0):
                string[i] = string[i].upper()
            else:
                string[i] = string[i].lower()
        answer.append(''.join(string))
    return ' '.join(answer)