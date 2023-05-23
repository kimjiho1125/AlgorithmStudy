#[핵심 아이디어]날짜를 모두 일로 표시하여 비교한다
def to_days(date):
    year, month, day = map(int,date.split('.'))
    return year*12*28 + month*28 + day

def solution(today, terms, privacies):
    term_to_day = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expired = [
        i+1 for i,privacy in enumerate(privacies) if to_days(privacy[:-2]) + term_to_day[privacy[-1]] <= today
    ]
    return expired
    
    