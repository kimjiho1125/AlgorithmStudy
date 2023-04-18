def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1,N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse = True)
    
#     answer = []
#     temp = {}
#     stages.sort()
#     perFail = 0.0
#     for i in range(len(stages)):
#         if i < len(stages) - 1  and stages[i] != stages[i+1]:
#             filteredList = [x for x in stages if x >= stages[i]]
#             perFail = stages.count(stages[i]) / len(filteredList)
#             temp[stages[i]] = perFail
#         elif (i == (len(stages)-1) and stages[i - 1] != stages[i]):
#             temp[stages[i]-1] = 0      
#     if len(temp) == 0:
#         answer.append(stages[0])
#         for i in range(1,stages[0]):
#             answer.append(i)
    
#     temp = sorted(temp.items(), key = lambda x : (-x[1],x[0]))
#     for item in temp:
#         answer.append(item[0])
#     return answer