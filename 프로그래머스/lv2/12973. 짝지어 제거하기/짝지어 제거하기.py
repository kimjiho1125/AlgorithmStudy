def solution(s):
    stack = []
    
    for alphabet in s:
        if len(stack) == 0: 
            stack.append(alphabet)
        elif stack[-1] == alphabet:
            stack.pop()
        else: 
            stack.append(alphabet)
    
    return 1 if len(stack) == 0 else 0
        

    