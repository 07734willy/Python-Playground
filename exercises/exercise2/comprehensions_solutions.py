


def large_elements(matrix):
	return [num2 for num1 in matrix for num2 in num1 if num2 > 4]




def max_every_other(numbers):
	return [max(numbers[i], numbers [i+1]) for i in range(0, len(numbers),2)]

max_every_other([7,1,9,10])

def power_of_twos():
    start = 0
    while True:
        yield 2 ** start
        start += 1


def power_of_twos():
	yield (2 ** x for x in itertools.count(0,1))

