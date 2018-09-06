# How many sundays are between 1/1/1901 and 12/31/2000?
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   Use a very imperative and self explanatory approach.
#   Deal with wrapping around years and months

months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
sundays = 0

year = 1901
month = 1

# The "lowest" sunday day.
day = 1 - (1 + 365) % 7  

if day == 8:
    day = 1
    sundays += 1

while True:
    day += 7

    days_of_month = months[month]
    if month == 2 and not year % 4:
        days_of_month += 1

    if day > days_of_month:
        if month == 12:
            if year == 2000:
                break
            
            month = 1
            year += 1
        else:
            month += 1
        
        day -= days_of_month

    if day == 1:
        sundays += 1


result = sundays