def solution(babbling):
    result = 0
    available = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for i in available:
            if i*2 not in word:
                word = word.replace(i,' ')
        if len(word.strip()) == 0:
            result += 1
    return result
        