def reverse(num):

	result = int(str(num)[::-1]) if num > 0 else int('-' + str(num)[::-1].replace('-',''))
	return result if -2147483648 <= result <= 2147483647 else 0
