def solution(sizes):
    # maxwidth = 0
    # maxheight = 0
    # for size in sizes:
    #     if(size[0] < size[1]):
    #         size[0],size[1] = size[1],size[0]
    #     if(maxwidth < size[0]):
    #         maxwidth = size[0]
    #     if(maxheight < size[1]):
    #         maxheight = size[1]
    # return maxwidth*maxheight
    # 더 좋은 풀이
    return max([max(x) for x in sizes]) * max([min(x) for x in sizes])