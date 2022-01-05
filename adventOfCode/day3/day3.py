import numpy as np

def run():
    readings = read_input()
    print(f"Part One : {calc_part1(readings)}")
    print(f"Part Two : {calc_part2(readings)}")

def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    #data = [int(x) for x in data]
    #print(data)
    return data

def calc_part1(readings):
    gammaRate = []
    epsilonRate = []
    for column in range(0, len(readings[0])):
        zeros = 0
        ones = 0
        for number in readings:
            if number[column] == '0':
                zeros += 1
            else:
                ones += 1
        #print(f"zeros: {zeros} and ones: {ones}")  
        if zeros > ones:
            gammaRate.append('0')  
            epsilonRate.append('1') 
        elif zeros < ones:
            gammaRate.append('1')  
            epsilonRate.append('0') 
    #gamma
    #print(gammaRate)
    gammaString = ("").join(gammaRate)
    #print(gammaString)
    gammaInt = int(gammaString, 2)
    print(gammaInt)
    
    #epsilon
    #print(epsilonRate)
    epsilonString = ("").join(epsilonRate)
    #print(gammaString)
    
    #change from binary to int
    epsilonInt = int(epsilonString, 2)
    print(epsilonInt)
    
    return epsilonInt*gammaInt

def calc_part2(readings):
    firstData = readings.copy()
    #print(f"initial data: {firstData}")
    
    i = 0
    #oxygen rating
    while len(firstData) > 1:
        zeros = 0
        ones = 0
        
        for bitstring in firstData:
            if bitstring[i] == '0':
                zeros += 1
            else:
                ones += 1
        # list shortener
        if zeros > ones:
            firstData = [bitstring for bitstring in firstData if bitstring[i]=='0']
        else:
            firstData = [bitstring for bitstring in firstData if bitstring[i]=='1']
        i += 1
    
    oxygenRating = ''.join(firstData)
    print(f"Oxygen Rating: {oxygenRating}")
    
    #Finding the CO2 rating
    secondData = readings.copy()
    i = 0
    #oxygen rating
    while len(secondData) > 1:
        zeros = 0
        ones = 0
        
        for bitstring in secondData:
            if bitstring[i] == '0':
                zeros += 1
            else:
                ones += 1
        # list shortener
        if zeros > ones:
            secondData = [bitstring for bitstring in secondData if bitstring[i]=='1']
        else:
            secondData = [bitstring for bitstring in secondData if bitstring[i]=='0']
        i += 1
    
    co2Rating = ''.join(secondData)
    print(f"CO2 Rating: {co2Rating}")
    
    supportRating = binary_to_int(oxygenRating) * binary_to_int(co2Rating)
    print(f"Final Support Rating: {supportRating}")
    return supportRating

def binary_to_int(strBin):
    return int(strBin, 2)

if __name__ == "__main__":
    run()