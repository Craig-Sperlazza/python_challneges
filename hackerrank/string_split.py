"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points."""

# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(word):
    """Kevin gets a point for word begin with vowels
    Stuart gets a point for word begin with consonants

    Args:
        word ([string]), all caps
    """
    stuart = 0
    kevin = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    length = len(word)

    for i in word:
        sum = length - count
        if i in vowels:
            kevin += sum
        else:
            stuart += sum
        count += 1

    if kevin > stuart:
        print(f"Winner Kevin {kevin}")
        print(f"Stuart {stuart}")
    if kevin < stuart:
        print(f"Winner Stuart {stuart}")
        print(f"Kevin {kevin}")
    if kevin == stuart:
        print(f"Draw")



if __name__ == "__main__":
    print(minion_game("BANANA"))
    print(minion_game("BAANANAS"))


