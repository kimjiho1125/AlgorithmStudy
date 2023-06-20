from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t],t))
    return len(set(tangerine[:k]))
    
    