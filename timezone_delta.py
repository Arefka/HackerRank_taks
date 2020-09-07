import datetime
'''
===============================================================

    When users post an update on social media,such as a URL, image, status update etc.,
    other users in their network are able to view this new post on their news feed.
    Users can also see exactly when the post was published,
    i.e, how many hours, minutes or seconds ago.

    Since sometimes posts are published and viewed in different time zones,
    this can be confusing. You are given two timestamps of one such post
    that a user can see on his newsfeed in the following format:

    Day dd Mon yyyy hh:mm:ss +xxxx

    Here +xxxx represents the time zone.
    Your task is to print the absolute difference (in seconds) between them.

    The first line contains T, the number of testcases.
    Each testcase contains 2 lines, representing time t1 and time t2.

    Input contains only valid timestamps
    year <= 3000

    Print the absolute difference (t1 - t2) in seconds.

===============================================================
'''

def time_calculation(first_date: str, second_date: str) -> str:
    format = '%a %d %b %Y %H:%M:%S %z'
    first_point = datetime.datetime.strptime(first_date, format)
    second_point = datetime.datetime.strptime(second_date, format)
    return str(int(abs((first_point - second_point).total_seconds())))

def datetime_distance_calculation(periods: list):
    for period in periods:
        print(time_calculation(period[0], period[1]))

################# example: #################
user_periods = [['Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000'],
                ['Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000']]

datetime_distance_calculation(user_periods)