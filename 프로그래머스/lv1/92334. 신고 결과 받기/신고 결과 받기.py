def solution(id_list, report, k):
    answer = []
    reportedCount = dict()
    user_info = dict()
    reportedId = []
    
    for i in id_list:
        user_info[i] = []
        reportedCount[i] = 0
    
    for case in report:
        reporter, reported = case.split(' ')
        if reported not in user_info[reporter]:
            user_info[reporter].append(reported)
            reportedCount[reported] += 1
            if reportedCount[reported] == k:
                reportedId.append(reported)
    
    for value in user_info.values():
        count = 0
        for i in value:
            if i in reportedId:
                count += 1
        answer.append(count)
        
    return answer