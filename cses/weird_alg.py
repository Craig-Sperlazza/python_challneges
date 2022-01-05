# Consider an algorithm that takes as input a positive integer n. 
# If n is even, the algorithm divides it by two, 
# and if n is odd, the algorithm multiplies it by three and adds one. 
# The algorithm repeats this, until n is one. 

# For example, the sequence for n=3 is as follows:
# 3→10→5→16→8→4→2→1

# Your task is to simulate the execution of the algorithm for a given value of n.
def formatVal(arr):
    """[summary]

    Args:
        arr ([arr]): arr of ints

    Returns:
        [string]: string of array values seperated by a ->
    
    Notes:
        We must change the floats to ints and then change the ints to str to use the join()
    """
    arrInt = map(int, arr)
    arrStr = map(str, arrInt)
    form = " ".join(arrStr) 
    return form

def weird(n, arr=[]):
    arr.append(n)
    if n == 1:
        final = formatVal(arr)
        return final
    elif n % 2 == 0:
        n = n / 2
        return weird(n, arr) 
    elif n % 2 != 0:
        n = (n * 3) + 1
        return weird(n, arr) 
    

    

if __name__ == "__main__":
    usrInput = int(input())
    print(weird(usrInput))