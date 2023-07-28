def solution(record):
#     result = []
#     #uid의 nickname 데이터를 저장할 딕셔너리를 생성한다
#     data = dict()
    
#     #record를 순회하며 최종적인 record를 만든다
#     for i in range(len(record)):
#         if record[i][0:6] == "Change":
#             situation, uid, nickname = record[i].split()
#             data[uid] = nickname
#         else:
#             if record[i][0:5] == "Enter":
#                 situation, uid, nickname = record[i].split()
#                 data[uid] = nickname
#     #결과 메시지를 result 배열에 추가한다
#     for i in range(len(record)):
#         if record[i][0:6] == "Change":
#             continue
#         elif record[i][0:5] == "Enter":
#             situation, uid, nickname = record[i].split()
#             temp = data[uid] + "님이 " + "들어왔습니다."
#             result.append(temp)
#         elif record[i][0:5] == "Leave":
#             situation, uid = record[i].split()
#             temp = data[uid] + "님이 " + "나갔습니다."
#             result.append(temp)

# 더 좋은 풀이
    result = []
    namespace = {}
    printer = {'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    
    for r in record:
        rr = r.split()
        if rr[0] in ['Enter','Change']:
            namespace[rr[1]] = rr[2]
    for r in record:
        if r.split()[0] != "Change":
            result.append(namespace[r.split()[1]] + printer[r.split()[0]])

    return result