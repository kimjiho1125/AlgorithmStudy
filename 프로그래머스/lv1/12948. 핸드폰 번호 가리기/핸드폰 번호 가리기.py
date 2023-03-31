def solution(phone_number):
    # phone_number = list(phone_number)
    # for i in reversed(range(len(phone_number) - 4)):
    #     phone_number[i] = "*"
    # result = ''.join(phone_number)
    # return result
    return '*'*(len(phone_number)-4)+phone_number[-4:]