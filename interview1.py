"""Question 1: Days Between 3.0"""


def days_between(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    days = 0
    cm_days_in_year = {0: 0, 1: 31, 2: 59,  3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
    while year1 < year2:
        if year2 - year1 >= 4:
            days += 1461
            year1 += 4
        else:
            days += 366 if year1 % 4 == 0 else 365
            year1 += 1

    days_to_month1 = cm_days_in_year[month1-1] + 1 if month1-1 > 1 and year1 % 4 == 0 else cm_days_in_year[month1-1]
    days_to_month2 = cm_days_in_year[month2-1] + 1 if month2-1 > 1 and year2 % 4 == 0 else cm_days_in_year[month2-1]

    days += days_to_month2 - days_to_month1

    days += day2 - day1

    return days


print(days_between(2010, 10, 24, 2011, 1, 17))


