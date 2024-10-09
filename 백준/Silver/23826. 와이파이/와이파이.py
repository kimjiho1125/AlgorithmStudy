import sys

input = sys.stdin.readline

N = int(input())

rooms = []
hot_spots = []
max_speed = 0

for i in range(N+1):
  x, y, e = map(int, input().split())

  # i=0일 경우 소학습실의 정보
  if i == 0:
    study_room = (x,y,e)
  # i!=0일 경우 방들의 정보
  else:
    rooms.append((x,y,e))
    #핫스팟이 켜져 있는 경우
    if e != 0:
      hot_spots.append((x,y,e))
  
#와이파이 속도를 계산하는 함수
def measure_speed(location1, location2):

  a, b, p = location1
  c, d = location2[0], location2[1]
  #location1에서 켜진 와이파이가 location2에 도달할 때의 와이파이의 세기
  speed = max(0, p - (abs(a-c) + abs(b-d)))

  return speed


#각 방에서의 와이파이 속도 계산하기
for room in rooms:
  #소학습실에서 해당 방까지의 와이파이의 세기 계산
  speed = measure_speed(study_room, room)
  #핫스팟을 사용하는 방에서 해당 방까지의 와이파이 세기 계산해서 빼기
  for hot_spot in hot_spots:
    speed -= measure_speed(hot_spot, room)
  #최대 속도 갱신
  if speed > max_speed:
    max_speed = speed 
  
#와이파이를 연결 할 수 없는 경우 -> IMPOSSIBLE 출력
if max_speed != 0:
  print(max_speed)
#와이파이를 연결할 수 있는 경우 -> 최고 속도 출력
else:
  print("IMPOSSIBLE")