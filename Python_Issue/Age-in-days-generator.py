days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def year_is_leap(year):
    if ((year % 4 is 0) and (year % 100 is not 0)) or (year % 400 is 0):
        return True
    else:
        return False


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    
    days_y = 0
    while (y2-1)>y1:
        if year_is_leap(y2)==False:
            days_y=days_y+365
        else:
            days_y=days_y+366
        y2=y2-1
        
    days_m = 0
    if y2>y1:
        for e in days_of_months[:(m2-2)] + days_of_months[(m1-1):]:
            days_m=days_m+e
    elif y2==y1 and m2>m1:
        for e in days_of_months[m1-1:(m2-2)]:
            days_m=days_m+e
            
    if days_m!=0 or m2>m1 or (m1==12 and m2==1):
        days_d = d2+days_of_months[(m1-1)]-d1
    elif m1==m2:
        days_d = d2-d1
        if days_d < 0:
            return 'ERROR'
        
    days= days_y+days_m+days_d
    
    return days


print daysBetweenDates(1992,01,01,2017,10,02)
print daysBetweenDates(2016, 12, 31, 2017, 1, 1)
