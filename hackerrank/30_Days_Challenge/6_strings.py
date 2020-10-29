
for j in range(int(input())):
    str0 = str(input())
    str1 = ''
    str2 = ''
    for i in range(len(str0)):
        if i % 2 == 0:
            str1 += str0[i]
        else:
            str2 += str0[i]

    print(f"{str1} {str2}")