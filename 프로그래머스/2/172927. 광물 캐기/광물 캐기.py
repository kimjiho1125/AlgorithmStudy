def solution(picks, minerals):

    result = 0
    
    m_dict = {"diamond" : 0, "iron" : 0, "stone" : 0}
    dict = {0 : (1, 1, 1), 1 : (5, 1, 1), 2 : (25, 5, 1)}
    
    array = []
    length = min(sum(picks)*5, len(minerals))
    
    for i in range(length):
        m_dict[minerals[i]] += 1
        if (i+1) % 5 == 0 or i == len(minerals) - 1:
            array.append([m_dict["diamond"],m_dict["iron"],m_dict["stone"]])
            m_dict["diamond"],m_dict["iron"],m_dict["stone"] = 0,0,0
            
    array.sort(key = lambda x: (x[0],x[1],x[2]),reverse = True)
    print(array)
    
    for dia,iron,stone in array:
        for i in range(3):
            if picks[i]:
                picks[i] -= 1
                result += (dia * dict[i][0] + iron * dict[i][1] + stone * dict[i][2])
                break
                
    return result