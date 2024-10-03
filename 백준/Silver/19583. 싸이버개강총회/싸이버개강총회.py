import sys

input = sys.stdin.readline
check_list = set()
cnt = 0

#시간 변환
def change_to_minutes(time):
  return int(time[:2]) * 60 + int(time[3:])

S, E ,Q = map(change_to_minutes, input().split())

while True:
  try:
    time, nickname = input().split()
    time = change_to_minutes(time)

    if time <= S:
      check_list.add(nickname)
    elif E <= time <= Q and nickname in check_list:
      check_list.remove(nickname)
      cnt += 1
  except:
    break

print(cnt)