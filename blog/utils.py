from datetime import datetime


# get the time difference in the format of days, hours, mins, secs
def get_time_difference(delta):
    mins, secs = divmod(delta.days * 86400 + delta.seconds, 60)
    hours = mins / 60
    return {
        'days': delta.days,
        'hours': hours,
        'mins': mins,
        'secs': secs
    }


def publish_time_format(time_measure, time):
    return 'published {} {} ago'.format(time, time_measure)


# display the last time when the post ws updated
def get_published_time_diff(updated_at):
    delta = datetime.now() - updated_at
    time_diff = get_time_difference(delta)
    for time_measure in ['days', 'hours', 'mins', 'secs']:
        if time_diff.get(time_measure, 0):
            return publish_time_format(time_measure, time_diff.get(time_measure))
    return publish_time_format('secs', 0)
