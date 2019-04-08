def find(numbers, target):

	counter = 1
	comparison = numbers[counter:]

	result = []

	for number in numbers:
		for num in comparison:
			if number + num == target:
				return [numbers.index(number), numbers.index(num)]
			else:
				counter += 1
				print(comparison)


print(find([1, 2, 7, 11, 15],9))
