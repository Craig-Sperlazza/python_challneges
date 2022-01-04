def run():
    depths = read_input()
    print(f"Part One : {depth_part1(depths)}")   
    print(f"Part Two : {depth_part2(depths)}")  

def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    data = [int(x) for x in data]
    return data


def depth_part1(depths):
    count = 0
    prev = 0
    current = 0
    for i, line in enumerate(depths):
        current = line
        if i == 0:
            prev = line
            continue
        elif i != 0:
            #print(f"previous: {prev} current: {current}")
            if current > prev:
                count += 1
                #print(count)
            prev = current
    print(f"final count part1:")
    return count

def depth_part2(depths):
    count = 0
    for i in range(2,len(depths)):
        #print(f"the depths are {depths[i]}")
        prev = depths[i-2] + depths[i-1] + depths[i-3]
        current = depths[i-2] + depths[i-1] + depths[i]
        if current > prev:
            #print(f"previous: {prev} current: {current}")
            count += 1
            #print(count)
    print(f"final count part2:")
    return count

if __name__ == '__main__':
    run()