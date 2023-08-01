def solution(dirs):
    history = []
    coord_x, coord_y = 0, 0
    
    for dir in dirs:
        current_coord = str(coord_x) + ',' + str(coord_y)
        if dir == 'U':
            if coord_y + 1 <= 5:
                coord_y += 1
        elif dir == 'D':
            if coord_y - 1 >= -5:
                coord_y -= 1
        elif dir == 'R':
            if coord_x + 1 <= 5:
                coord_x += 1
        elif dir == 'L':
            if coord_x - 1 >= -5:
                coord_x -= 1
        next_coord = str(coord_x) + ',' + str(coord_y)
        if current_coord != next_coord:
            history.append(current_coord + "to" + next_coord)
            history.append(next_coord + "to" + current_coord)

    result = set(history)
    return len(result)/2