from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 0
    sumWeight = 0
    crossBridge = deque()
    crossedBridge = []
    maxlen = len(truck_weights)
    
    while len(crossedBridge) < maxlen:
        sec += 1
        if len(crossBridge) > 0:
            if crossBridge[0][1] == bridge_length:
                temp = crossBridge.popleft()[0]
                sumWeight -= temp
                crossedBridge.append(temp)
            for i in range(len(crossBridge)):
                if crossBridge[i][1] < bridge_length:
                    crossBridge[i][1] += 1
            
        if len(truck_weights) != 0 and len(crossBridge) < bridge_length and sumWeight + truck_weights[0] <= weight:
            temp = truck_weights.pop(0)
            sumWeight += temp
            crossBridge.append([temp,1])
        
    return sec