import math

def cal(fees, total_minutes):
    if total_minutes <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((total_minutes - fees[0]) / fees[2]) * fees[3]
    


def solution(fees, records):
    answer = []
    temp_dic = dict() #in - out 확인용
    dic = dict()      #누적 시간 기록
    for record in records:
        if int(record[6:10]) not in dic:
            dic[int(record[6:10])] = 0
        if len(record) == 13:
            #입차 시간을 분으로 계산하여 기록
            temp_dic[int(record[6:10])] = int(record[0:2])*60 + int(record[3:5])   
        if len(record) == 14:
            #출차 시간 - 입차 시간을 계산하여 dic에 기록
            dic[int(record[6:10])] += (int(record[0:2])*60 + int(record[3:5])-temp_dic[int(record[6:10])])
            del temp_dic[int(record[6:10])]
    
    if len(temp_dic) > 0:
        for key,value in temp_dic.items():
            dic[key] += 1439 - value
    
    dic = sorted(dic.items(), key=lambda x: x[0])
    print(dic)
    for total in dic:
        answer.append(cal(fees,total[1]))
    return answer