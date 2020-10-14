import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

input_date = input("Please enter a date MM DD YYYY")
#print(input_date)

input_lst = input_date.split()
#print(input_lst)

# print(int(input_lst[2]))
# print(int(input_lst[1]))
# print(int(input_lst[0]))

day = calendar.weekday(int(input_lst[2]), int(input_lst[0]), int(input_lst[1]))

print(calendar.day_name[day].upper())