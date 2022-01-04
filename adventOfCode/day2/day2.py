def run():
    moves = read_input()
    print(f"Part One : {calc_position1(moves)}")  
    print(f"Part Two : {calc_position2(moves)}") 

def read_input():
    f = open("input.txt", "r")
    
    data = f.read().splitlines()
    print(data)
    return data


def calc_position1(moves):
    horizontal = 0
    depth = 0
    for i in range(len(moves)):
        value = int(moves[i][-1])
        print(value)
        if moves[i][0]== "u":
            depth -= value
        elif moves[i][0]== "d":
            depth += value
        elif moves[i][0]== "f":
            horizontal += value
    print(f"horizontal: {horizontal}, depth = {depth}")
    print(horizontal*depth)

def calc_position2(moves):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(moves)):
        value = int(moves[i][-1])
        print(value)
        if moves[i][0]== "u":
            aim -= value
        elif moves[i][0]== "d":
            aim += value
        elif moves[i][0]== "f":
            horizontal += value
            depth = depth + (aim * value)
    print(f"horizontal: {horizontal}, depth = {depth}")
    print(horizontal*depth)

if __name__ =="__main__":
    run()