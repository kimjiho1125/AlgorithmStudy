n = int(input())

# 첫번째 줄 출력
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

d = [0,1]

# 확장된 피보나치 함수
for i in range(2, abs(n) + 1):
  d.append((d[i-1] + d[i-2]) % 1000000000)

# 결과 출력
print(d[abs(n)])