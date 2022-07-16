"""
Time calculator
"""

import re


def minutes(sum_s_d_m, sum_s_d_h):
    sum_s_d_h += int(sum_s_d_m / 60)
    sum_s_d_m %= 60
    return sum_s_d_h, sum_s_d_m


def hours(sum_s_d_h, cont_day):
    cont_day += int(sum_s_d_h / 24)
    sum_s_d_h %= 24
    if (sum_s_d_h % 12) == 0:
        sum_s_d_h_t = 12
    else:
        sum_s_d_h_t = sum_s_d_h % 12
    return sum_s_d_h, cont_day, sum_s_d_h_t


def back(sum_s_d_h, cont_day, sum_s_d_h_t, sum_s_d_m):
    if sum_s_d_h > 12 and cont_day == 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} PM (next day)')
    elif sum_s_d_h > 12 and cont_day > 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} PM ({cont_day} days later)')
    elif sum_s_d_h < 12 and cont_day == 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} AM (next day)')
    elif sum_s_d_h < 12 and cont_day > 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} AM ({cont_day} days later)')
    return


def more12less24(sum_s_d_h, sum_s_d_m):
    if (sum_s_d_h % 12) == 0:
        sum_s_d_h_t = 12
    else:
        sum_s_d_h_t = sum_s_d_h % 12
    print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} PM')
    return

def day_w(day):
    w_k = day.lower()
    day_lower = re.findall('monday|tuesday|wednesday|thursday|friday|saturday|sunday', w_k)
    days_w = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    day_f = None
    for i in range(6):
        day_f = re.search(day_lower[0], days_w[i])
        if day_f !=  None:
            day_f = i
            break
    return day_f, days_w


def third_argument(sum_s_d_h, cont_day, sum_s_d_h_t, sum_s_d_m, days_w, day_f):
    if sum_s_d_h > 12 and cont_day == 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} PM {days_w[day_f].capitalize()} (next day)')
    elif sum_s_d_h > 12 and cont_day > 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} PM {days_w[day_f].capitalize()} ({cont_day} days later)')
    elif sum_s_d_h < 12 and cont_day == 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} AM {days_w[day_f].capitalize()} (next day)')
    elif sum_s_d_h < 12 and cont_day > 1:
        print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} AM {days_w[day_f].capitalize()} ({cont_day} days later)')

    return

def more12less24_third(sum_s_d_h, sum_s_d_m, days_w, day_f):
    if (sum_s_d_h % 12) == 0:
        sum_s_d_h_t = 12
    else:
        sum_s_d_h_t = sum_s_d_h % 12
    print(f'Returns: {sum_s_d_h_t}:{sum_s_d_m} PM {days_w[day_f].capitalize()}')

    return

def add_time(start, duration, day = None):

    # var inicialitation and regex search
    start_h = int(re.findall('^[0-9]*[0-9]', start)[0])
    start_m = int(re.findall('[:]([0-9].*)\s', start)[0])
    start_ap = re.findall('\s(AM|PM)', start)
    duration_h = int(re.findall('^[0-9]*[0-9]', duration)[0])
    duration_m = int(re.findall('[:]([0-9].)$', duration)[0])

    # Hour of start plus hour of duration
    sum_s_d_h = start_h + duration_h
    #Minute of start plus minute of duration
    sum_s_d_m = start_m + duration_m
    cont_day = 0
    # If there are just two arguments

    if day == None:
        # If sum_s_d_m is > 60 means that is an hour plus to sum_s_d_h

        if sum_s_d_m >= 60:
            sum_s_d_h = (minutes(sum_s_d_m, sum_s_d_h)[0])
            sum_s_d_m = (minutes(sum_s_d_m, sum_s_d_h)[1])
        # If start is AM or PM, if sum_s_d_h > 24 means that it´s one o more days later
        if start_ap[0] == 'AM':
            if sum_s_d_h > 24:
                cont_day = (hours(sum_s_d_h, cont_day)[1])
                sum_s_d_h_t = (hours(sum_s_d_h, cont_day)[2])
                back(sum_s_d_h, cont_day, sum_s_d_h_t, sum_s_d_m)
            elif sum_s_d_h >= 12 and sum_s_d_h <= 24:
                more12less24(sum_s_d_h, sum_s_d_m)
            elif sum_s_d_h < 12:
                print(f'Returns: {sum_s_d_h}:{sum_s_d_m} AM')
        elif start_ap[0] == 'PM':
            sum_s_d_h += 12
            if sum_s_d_h > 24:
                cont_day = (hours(sum_s_d_h, cont_day)[1])
                sum_s_d_h_t = (hours(sum_s_d_h, cont_day)[2])
                back(sum_s_d_h, cont_day, sum_s_d_h_t, sum_s_d_m)
            elif sum_s_d_h >= 12 and sum_s_d_h <= 24:
                more12less24(sum_s_d_h, sum_s_d_m)
            elif sum_s_d_h < 12:
                print(f'Returns: {sum_s_d_h}:{sum_s_d_m} AM')
    # If there are 3 arguments we make the third to lower case to find with regex what day of the week is
    else:
        day_f = (day_w(day)[0])
        days_w = (day_w(day)[1])
        if sum_s_d_m >= 60:
            sum_s_d_h = (minutes(sum_s_d_m, sum_s_d_h)[0])
            sum_s_d_m = (minutes(sum_s_d_m, sum_s_d_h)[1])
        if start_ap[0] == 'AM':
            if sum_s_d_h > 24:
                cont_day = (hours(sum_s_d_h, cont_day)[1])
                sum_s_d_h_t = (hours(sum_s_d_h, cont_day)[2])
                day_f += cont_day
                if day_f > 6:
                    day_f = 0
                third_argument(sum_s_d_h, cont_day, sum_s_d_h_t, sum_s_d_m, days_w, day_f)
            elif sum_s_d_h >= 12 and sum_s_d_h <= 24:
                more12less24_third(sum_s_d_h, sum_s_d_m, days_w, day_f)
            elif sum_s_d_h < 12:
                print(f'Returns: {sum_s_d_h}:{sum_s_d_m} AM {days_w[day_f].capitalize()}')
        elif start_ap[0] == 'PM':
            sum_s_d_h += 12
            if sum_s_d_h > 24:
                cont_day = (hours(sum_s_d_h, cont_day)[1])
                sum_s_d_h_t = (hours(sum_s_d_h, cont_day)[2])
                day_f += cont_day
                if day_f > 6:
                    day_f = 0
                third_argument(sum_s_d_h, cont_day, sum_s_d_h_t, sum_s_d_m, days_w, day_f)
            elif sum_s_d_h >= 12 and sum_s_d_h <= 24:
                more12less24_third(sum_s_d_h, sum_s_d_m, days_w, day_f)
            elif sum_s_d_h < 12:
                print(f'Returns: {sum_s_d_h}:{sum_s_d_m} AM {days_w[day_f].capitalize()}')

