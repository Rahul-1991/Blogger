def get_time_difference(delta):
    mins, secs = divmod(delta.days * 86400 + delta.seconds, 60)
    hours = mins / 60
    return {
        'days': delta.days,
        'hours': hours,
        'mins': mins,
        'secs': secs
    }
