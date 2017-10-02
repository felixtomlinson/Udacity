

days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# cleaned up variable and list


# this function is quite long and could be shorter
# what features does a leap year have?
def is_leap_year(year):
    leap_year = []
    a = 0
    while a < 25:
        leap_year.append(2016-(a*4))
        a = a+1
    if year in leap_year:
        # return booleans, rather than strings
        return True
    else:
        return False


def days_between_dates(y1, m1, d1, y2, m2, d2):
    days_y = 0
    # loops, checking if y2 is later than y1
    while (y2-1) > y1:
        # if it's higher, is it a leap year?
        if is_leap_year(y2) is False:
            # if so, add 366; if not, add 365
            days_y = days_y+365
        else:
            days_y = days_y+366
        # subtract one year from y2 and go back to the start
        y2 = y2-1
        # what happens when y2 is equal to y1?
    days_m = 0
    if y2 > y1:  # this line is now redundant
        for e in days_of_months[:(m2-1)] + days_of_months[(m1):]:
            days_m = days_m+e
    # skips directly to here
    elif y2 == y1 and m2 > m1:
        for e in days_of_months[m1:(m2-1)]:  # you're using m1 as an index - are you sure it's correct?
            days_m = days_m+e
    if days_m!=0 or m2>m1 :
        days_d = d2+days_of_months[(m1-1)]-d1
    elif m1==m2:
        days_d = d2-d1
        if days_d < 0:
            return 'ERROR'
    days= days_y+days_m+days_d
    return days


print days_between_dates(1992,01,01,2017,10,02)
print days_between_dates(2016, 12, 31, 2017, 1, 1)

# computers do this by converting to seconds since 1970, comparing, and then converting back
# that's...probably too specific. But you could do it with days
# consider:


def year_is_leap(year):
    if ((year % 4 is 0) and (year % 100 is not 0)) or (year % 400 is 0):
        return True
    else:
        return False


def convert_date_to_days(day, month, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    hard_coded_year = 1970
    """this function is called twice, and calculates days since an arbitrary and hard-coded date"""
    for y in range(hard_coded_year, year):
        # range is a function that takes a start and end integer, then gives you each int between the two
        if year_is_leap(y):
            # see above for function to check if year is leap
            days += 366
        else:
            days += 365
    # could have used a function here
    days += sum(days_in_months[0:month-1])  # this sums the list, up to the month before the month in the test
    days += day  # adds the days
    return days


def compare_dates(date_1, date_2):
    days_1 = convert_date_to_days(*date_1)
    days_2 = convert_date_to_days(*date_2)
    diff = abs(days_2-days_1)  # absolute value in case date 2 is before date 1
    print(diff)


test1 = ([1, 1, 1992], [2, 10, 2017])
test2 = ([1, 1, 2016], [31, 12, 2015])

compare_dates(*test1)
compare_dates(*test2)





