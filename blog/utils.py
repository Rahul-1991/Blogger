from datetime import datetime


def get_time_difference(delta):
    mins, secs = divmod(delta.days * 86400 + delta.seconds, 60)
    hours = mins / 60
    return {
        'days': delta.days,
        'hours': hours,
        'mins': mins,
        'secs': secs
    }


def get_published_time_diff(updated_at):
    current_time = datetime.now()
    published_time = updated_at
    delta = current_time - published_time
    time_diff = get_time_difference(delta)
    if time_diff.get('days', 0):
        return 'published {} days ago'.format(time_diff.get('days'))
    elif time_diff.get('hours', 0):
        return 'published {} hours ago'.format(time_diff.get('hours'))
    elif time_diff.get('mins', 0):
        return 'published {} mins ago'.format(time_diff.get('mins'))
    else:
        return 'published {} seconds ago'.format(time_diff.get('secs', 0))