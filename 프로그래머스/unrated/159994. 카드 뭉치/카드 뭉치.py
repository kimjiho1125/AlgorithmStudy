def solution(cards1, cards2, goal):
    cards1Index = 0
    cards2Index = 0
    result = "Yes"
    for str in goal:
        if cards1Index < len(cards1) and str in cards1[cards1Index]:
            cards1Index += 1
            continue
        elif cards2Index < len(cards2) and str in cards2[cards2Index]:
            cards2Index += 1
            continue
        else:
            result = "No"
            break
    return result