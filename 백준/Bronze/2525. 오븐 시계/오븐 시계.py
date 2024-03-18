import sys

#입력조건 입력받기
current_h, current_m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

#시간 계산
if time >= 60:
    h, m = divmod(time, 60)
    current_h += h
    current_m += m
else:
    current_m += time

if current_m >= 60:
    h, m = divmod(current_m, 60)
    current_h += h
    current_m = m

if current_h >= 24:
    current_h -= 24

print(current_h, current_m)