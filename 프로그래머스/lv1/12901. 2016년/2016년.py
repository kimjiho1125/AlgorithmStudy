def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    temp = -1
    for i in range(0,a-1):
        temp += days[i]
    temp += b
    return week[temp % 7]