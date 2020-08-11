from datetime import datetime, timedelta


def to_mssql_datetime(d: datetime):
    return f"{d.month:02}/{d.day:02}/{d.year} {d.hour:02}:{d.minute:02}:{d.second:02}"


def now():
    return datetime.now()


def now_plus(dias: int) -> datetime:
    return now() + timedelta(days=dias)


def now_minus(dias: int) -> datetime:
    return now() - timedelta(days=dias)

def cal_days_diff(a,b):

    A = a.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    B = b.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    return (A - B).days