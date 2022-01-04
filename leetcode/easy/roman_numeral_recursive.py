def romanToInt(s: str, sum: int = 0) -> int:
    if len(s) == 0:
        return sum
    elif len(s) == 1:
        if s[0] == 'I':
            return sum + 1
        elif s[0] == 'V':
            return sum + 5
        elif s[0] == 'X':
            return sum + 10
        elif s[0] == 'L':
            return sum + 50
        elif s[0] == 'C':
            return sum + 100
        elif s[0] == 'D':
            return sum + 500
        elif s[0] == 'M':
            return sum + 1000
    elif s == 'IV':
        return sum + 4
    elif s == 'IX':
        return sum + 9
    elif s == 'XL':
        return sum + 40
    elif s == 'XC':
        return sum + 90
    elif s == 'CD':
        return sum + 400
    elif s == 'CM':
        return sum + 900
    else:
        end = s[-2:]
        if end == 'IV':
            start_str = s[:-2]
            return romanToInt(start_str, sum + 4)
        elif end == 'IX':
            start_str = s[:-2]
            return romanToInt(start_str, sum + 9)
        elif end == 'XL':
            start_str = s[:-2]
            return romanToInt(start_str, sum + 40)
        elif end == 'XC':
            start_str = s[:-2]
            return romanToInt(start_str, sum + 90)
        elif end == 'CD':
            start_str = s[:-2]
            return romanToInt(start_str, sum + 400)
        elif end == 'CM':
            start_str = s[:-2]
            return romanToInt(start_str, sum + 900)
        else:
            start_str = s[:-1]
            print(start_str)
            if s[-1] == 'I':
                return romanToInt(start_str, sum + 1)
            elif s[-1] == 'V':
                return romanToInt(start_str, sum + 5)
            elif s[-1] == 'X':
                return romanToInt(start_str, sum + 10)
            elif s[-1] == 'L':
                return romanToInt(start_str, sum + 50)
            elif s[-1] == 'C':
                return romanToInt(start_str, sum + 100)
            elif s[-1] == 'D':
                return romanToInt(start_str, sum + 500)
            elif s[-1] == 'M':
                return romanToInt(start_str, sum + 1000)
        

# print(romanToInt('IV'))
# print(romanToInt('XIX'))
# print(romanToInt('MCMXLIX'))
print(romanToInt('III'))
