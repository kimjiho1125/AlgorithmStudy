words = []
answer = ''
max_len = 0

for _ in range(5):
    s = list(input())
    words.append(s)
    if max_len < len(s):
        max_len = len(s)

for j in range(max_len):
    for word in words:
        if j < len(word):
            answer += word[j]

print(answer)