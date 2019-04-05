def reverse(num):

	numbers = str(num)

	negative = '-'
	
	result = ''

	length = len(numbers) -1

	while length >= 0:
		if numbers[length]!= negative:
			result += numbers[length]
		length -= 1
	
	final = 0
		
	if numbers[0] == negative:
		final += int(negative + result)
	else:
		final += int(result)

	if -2147483648 <= final <= 2147483647:
		return final
	else:
		return 0
