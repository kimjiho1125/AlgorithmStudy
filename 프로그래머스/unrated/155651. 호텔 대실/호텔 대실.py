from collections import defaultdict

#시간을 변환하기 위한 함수
def getTime(time):
    HH,MM = map(int,time.split(":"))
    return HH * 60 + MM

def solution(book_time):
    
    MAX, now, books = 0, 0, defaultdict(int)
    
    for book_info in book_time:
        start, end = getTime(book_info[0]), getTime(book_info[1])
        books[start] += 1
        books[end + 10] -= 1
    
    print(books)
    books = sorted(list(map(list,books.items())))
    print(books)
    
    for b in books:
        now += b[1]
        MAX = max(MAX,now)
    
    return MAX
    