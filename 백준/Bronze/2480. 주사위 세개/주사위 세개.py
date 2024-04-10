cases = list(map(int, input().split()))
count = dict()

for case in cases:
    if case not in count:
        count[case] = 1
    else:
        count[case] += 1

count = sorted(count.items(), key = lambda x: (x[1], x[0]), reverse = True)

#모두 같은 눈인 경우
if len(count) == 1:
    print(10000 + count[0][0] * 1000)
elif len(count) == 2:
    print(1000 + count[0][0] * 100)
elif len(count) == 3:
    print(count[0][0] * 100)
    