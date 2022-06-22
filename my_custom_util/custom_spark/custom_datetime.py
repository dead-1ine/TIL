import datetime

def get_timetuple(time_obj: datetime):
    year, month, day, hour, minute, second, *_ = ['{x:02}' for x in time_obj.timetuple()]
    return year, month, day, hour, minute, second


        