def solution(skill, skill_trees):
    answer = 0
    skills = []
    #스킬트리에 있는 스킬들을 순서대로 리스트에 저장
    for s in skill:
        skills.append(s)
        
    for skill_tree in skill_trees:
        order = 0
        flag = True
        for s in skill_tree:
            if s in skills:
                if s == skills[order]:
                    order += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1
            
    return answer