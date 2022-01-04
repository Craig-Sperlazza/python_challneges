# Create a function that takes a number num and returns its length.

def num_len (num):
    str_num = str(num)
    count = 0
    for i in str_num:
        count += 1
    return count

if __name__ == "__main__":
    print(num_len(10000))