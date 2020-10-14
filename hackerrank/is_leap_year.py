def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        #print("here")
        leap = True
        return leap
    elif year % 4 == 0 and year % 100 == 0:
        #print("here2")
        return leap
    elif year % 4 == 0:
        #print("here3")
        leap = True
        return leap
    #print("here4")
    return leap

year = int((2000))
print(is_leap(year))