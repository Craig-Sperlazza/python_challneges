#https://www.algoexpert.io/questions/Validate%20Subsequence

#a sequence must be a subset of an array

def isValidSubsequence(array, sequence):
	if len(sequence) == 0:
		return True
	if len(array) == 0:
		return False
	else:
		for i in range(len(sequence)):
			for j in range(len(array)):
				if sequence[i] == array[j]:
					array = array[j+1:]
					sequence = sequence[i+1:]
					return (isValidSubsequence(array, sequence))
			return False
					