def solution(m, musicinfos):
    result = []
    count = 1
    
    m = m.replace('C#',"c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        startTime = int(musicinfo[0][:2])*60 + int(musicinfo[0][3:])
        endTime = int(musicinfo[1][:2])*60 + int(musicinfo[1][3:])
        playTime = endTime - startTime
        if playTime < 0:
            playTime *= -1
        title = musicinfo[2]
        sheet = musicinfo[3].replace('C#',"c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        
        if playTime > len(sheet):
            quotient, reminder = divmod(playTime, len(sheet))
            sheet = sheet + (sheet)*quotient + sheet[:reminder]
        
        if playTime < len(sheet):
            sheet = sheet[:playTime]
        
        if sheet.find(m) != -1:
            result.append([playTime,title,count])
            count += 1
    
    result.sort(key=lambda x : (-x[0],x[2]))
    
    return result[0][1] if result else "(None)"