def solution(array, commands):
    result = []
    for command in commands:
        temp = array[command[0]-1 : command[1]]
        temp.sort()
        result.append(temp[command[2] - 1])
    return result