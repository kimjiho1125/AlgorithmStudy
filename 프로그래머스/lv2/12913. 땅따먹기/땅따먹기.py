#완전 탐색 문제! -> 모든 경우의 수를 체크해 보자
def solution(land):
    #특수 규칙에 맞게 앞 행의 최대값을 더해가며 모든 경우의 최대값을 계산해 나간다.
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    
    #land 배열의 마지막 행의 최대값이 최종적인 최대값임
    return max(land[-1])