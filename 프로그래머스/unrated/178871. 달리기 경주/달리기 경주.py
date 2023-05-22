def solution(players, callings):
    hashMap = dict()
    for i,v in enumerate(players):
        hashMap[v] = i
    
    for call in callings:
        pre, index = hashMap[call]-1, hashMap[call]
        hashMap[players[pre]],hashMap[call] = hashMap[call], hashMap[players[pre]]
        players[pre], players[index] = players[index], players[pre]
        
    return players