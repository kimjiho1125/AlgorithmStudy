from collections import deque

def solution(operations):
    queue = deque()
    
    for operation in operations:
        op, num = operation.split()
        
        if op == 'I':
            queue.append(int(num))
        elif op == 'D' and num == '-1':
            if len(queue) != 0:
                queue.remove(int(min(queue)))
        elif op == 'D' and num == '1':
            if len(queue) != 0:
                queue.remove(int(max(queue)))
        
    return [max(queue),min(queue)] if len(queue) != 0 else [0,0]