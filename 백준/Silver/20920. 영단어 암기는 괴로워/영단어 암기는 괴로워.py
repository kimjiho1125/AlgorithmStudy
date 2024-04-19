import sys
input = sys.stdin.readline

n,m = map(int, input().split())
word_dict = dict()

for _ in range(n):
    word = input().strip()
    l_word = len(word)
    if l_word < m:
        continue
    #만약 dictionary에 해당 단어가 존재하지 않으면
    if word not in word_dict:
        #초기화
        word_dict[word] = [1,l_word,word]
    #빈도 수 1증가 시키기
    elif word_dict[word]:
        word_dict[word][0] += 1
    
word_list = sorted(word_dict.items(), key=lambda x : x[1][2])    
word_list = sorted(word_list, key=lambda x : (x[1][0],x[1][1]), reverse=True)

for word in word_list:
    print(word[0])