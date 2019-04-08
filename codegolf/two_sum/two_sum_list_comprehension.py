


def two_sums(numbers, target):
	return  [[numbers.index(num1), numbers.index(num2)]
	for num1 in numbers for num2 in numbers if num1 + num2 == target][0]




print(two_sums([2, 7, 11, 15],9))