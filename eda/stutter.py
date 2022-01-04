# Write a function that stutters a word as if someone is struggling to read it. 
# The first two letters are repeated twice with an ellipsis ... and space after each, 
# and then the word is pronounced with a question mark ?.

def stutter(word):
    first_two = word[:2]
    answer = f"{first_two}... {first_two}... {word}?"
    return answer

if __name__ == "__main__":
    print(stutter('incredible'))
