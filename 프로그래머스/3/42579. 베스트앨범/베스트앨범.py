def solution(genres, plays):
    answer = []
    song_num = len(plays)
    song_info = dict()
    genre_cnt = dict()
    for i in range(song_num):
        if genres[i] not in song_info:
            song_info[genres[i]] = [(i,plays[i])]
            genre_cnt[genres[i]] = plays[i]
        else:
            song_info[genres[i]].append((i,plays[i]))
            genre_cnt[genres[i]] += plays[i]
    
    for key,value in song_info.items():
        value.sort(key = lambda x : (-x[1],x[0]))
        
    genre_cnt = sorted(genre_cnt.items(), key = lambda x : -x[1])
    
    for genre, num in genre_cnt:
        if (len(song_info[genre]) == 1):
            answer.append(song_info[genre][0][0])
        else:
            answer.append(song_info[genre][0][0])
            answer.append(song_info[genre][1][0])
    
    return answer