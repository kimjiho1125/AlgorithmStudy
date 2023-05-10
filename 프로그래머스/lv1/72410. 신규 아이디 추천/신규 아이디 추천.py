def solution(new_id):
    available = ["-","_","."]
    preIndex = -1
    i=0

    #1단계
    new_id = new_id.lower()
    
    #2단계
    for s in new_id:
        if s.isalpha() == True or s.isdigit() == True or s in available:
            if s == ".":
                continue
        else:
            new_id = new_id.replace(s,"")
            
    #3단계,4단계
    while(i < len(new_id)):
        if i == 0 and new_id[i] == ".":
            new_id = new_id[1:]
            continue
        elif new_id[i] == ".":
            if preIndex == -1:
                preIndex = i
            elif preIndex+1 == i:
                new_id = new_id[:i]+new_id[i+1:]
                i -= 1
                continue
            elif preIndex+1 != i:
                preIndex = i
        if i == len(new_id)-1 and new_id[i] == ".":
            new_id = new_id[:i]
            break
        i += 1
    #5단계
    if len(new_id) == 0:
        new_id += "a"
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[len(new_id)-1] == ".":
        new_id = new_id[:len(new_id)-1]
    #7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[len(new_id)-1]
    
    return new_id
                
           
            
            