# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
#
# For numbers which are multiples of both three and five output “FizzBuzz”.

from typing import List

def fizzBuzz(n: int) -> List[str]:
    fb_list = []
    for i in range(1, (n + 1)):
        if i % 3 == 0 and i % 5 == 0:
            fb_list.append("FizzBuzz")
        elif i % 3 == 0:
            fb_list.append("Fizz")
        elif i % 5 == 0:
            fb_list.append("Buzz")
        else:
            fb_list.append(str(i))
    return fb_list


if __name__ == "__main__":
    n = 15
    print(fizzBuzz(15))