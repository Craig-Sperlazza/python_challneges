# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    first = string[0:position]
    second = string[(position+1):]
    return first + character + second

if __name__ == '__main__':
    print(mutate_string('abracadabra', 5, 'k'))