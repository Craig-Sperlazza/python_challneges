def romanToInt(s: str) -> int:
    total = 0
    
    for i in range(len(s)):
        
    
    
    end = s[-2:]
    # start_str = s[:-2]
    # print(end)
    # print(start_str)
    if end != 'IV' and end != 'IX':
        start_str = s
    elif end == 'IV':
        total += 4
        start_str = s[:-2]
    elif end == 'IX':
        total += 9
        start_str = s[:-2]
    
    if len(start_str) == 0:
        return total
    else:
        for i in start_str:
            if i == 'I':
                total += 1
            elif i == 'V':
                total += 5
            elif i == 'X':
                total += 10
            elif i == 'L':
                total += 50
            elif i == 'C':
                total += 100
            elif i == 'D':
                total += 500
            elif i == 'M':
                total += 1000
    return total


print(romanToInt('IV'))
print(romanToInt('XIX'))

'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

'''

