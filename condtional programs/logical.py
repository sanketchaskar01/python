# check if the year is leap

year=int(input('enter the year'))

if year % 400 == 0 or (year %4 == 0 and year %100 != 0):
    print(year,'is leap year')
else:
    print(year,'is not leap year')

# not
if not year % 400 == 0 or (year %4 == 0 and year %100 != 0):
    print(year,'is not leap year')
else:
    print(year,'is  leap year')

