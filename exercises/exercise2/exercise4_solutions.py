#1

# TODO: use list comp AND zip
def subtraction(numbersA, numbersB):
    out = []
    for i in range(min(len(numbersA), len(numbersB))):
        out.append(numbersA[i] - numbersB[i])
    return out

#answer:
def subtraction(numbersA, numbersB):
	return ([i[0] - i[1] for i in list(zip(numbersA, numbersB))])

#2

# TODO use map and str- no comprehensions
def letters_in_string(word):
    return [letter for letter in word]

#answer (seriously I find the 'use str' really weird)
def letters_in_string(word):
    return word + ''

print(list(map(letters_in_string, 'meow')))

#answer2 pythonic
def letters_in_string(word):
	return list(word)

#answer3 functional (probably the answer you're looking for)
def letters_in_string(word):
	return list(map(lambda x: str(x), word))


#3

# TODO fill both of the following two functions in with some calculation (anything), and call them both.
#      don't edit the function's arguments

def calculate(input_list):
    pass

def calculat32(*vargs):
    pass


#answer :
def calculate(input_list):
	return [num ** 2 for num in input_list]

def calculat32(*vargs):
	return [num + 2 for num in vargs]

calculate(calculat32(1,2,3))
#output [9,16,25]


#4
# TODO use the short-circuiting behavior demonstated in the following function to the `ternary` into
#      an expression of `or`s and variables

# returns varA if varA is not 0/None/[]/False, otherwise returns varB
def short_circuit_demo(varA, varB):
    return varA or varB


# TODO use the above example to convert this function to `or`s
def ternary(varA, varB, varC):
    tmp = varC if varC else varA
    return varB if varB else tmp


#answer:
def ternary(varA, varB, varC):
    return varB if varB else (varC if varC else varA)


#5
# TODO return true is any of the values in `numbers` are greater than 3
#      use `any()` and a comprehension
def any_above_three(numbers):
    for num in numbers:
        if num > 3:
            return True
    return False

#answer
def any_above_three(numbers):
	return any([num for num in numbers if num >3])

#6
# TODO same behavior, except if all values are larger than 3
# hint: `all`
def all_above_three(numbers):
    for num in numbers:
        if num <= 3:
            return False
    return True

#answer
def all_above_three(numbers):
	return all([num > 3 for num in numbers])

#7
# use the following example to see how for-else is used, for the next problem

def last_zero(numbers):
    index = 0
    for i, val in enumerate(numbers):
        if val == 0:
            index = i
    else:
        raise Exception("No zeros found")
    return index


# TODO iterate over two lists simulaneously, report the index of the first pair with equal value. 
#      raise an exception if there's no such pair
# example: [1, 3, 4, 5], [3, 5, 4, 7]  would return 2 (the index of the 4's)
# NOTE this cannot be done as a one-liner, but could be done in three.
# Either way, use `zip` to make your life easier, and for-else for the sake of practice

#answer
def index_of_same_element(numsA, numsB):
    for num in list(zip(numsA, numsB)):
    	if num[0] == num[1]:
    		return list(zip(numsA, numsB)).index(num)
    else:
    	raise Exception("No pairs found!")



#8
# TODO strip this solution down to 4 lines (including def ... ), by solely 
#       removing whitespace and adding `;` where need be

def random_thing(numbers, const):
    for num in numbers:
        if 3 < num < 12:
            return True
    temp = const + max(numbers)
    return temp


#answers (NOTE: Python won't run both 'return' statements with ';' line break. Tested on 2.7 and 3.7 IDEs to no avail, so I'm giving you answers less than the # of lines you intended instead)
def random_thing(numbers, const):
	return any(3 < num < 12 for num in numbers), const + max(numbers)

def random_thing(numbers, const):
	result = any(3 < num < 12 for num in numbers); temp = const + max(numbers)   
	return result, temp

 
#9            
# TODO sort a string consisting solely of digits (there may be duplicates) in the following order
#      1 < 4 < 3 < 5 < 9 < 7 < 2 < 8 < 0 < 6
#      don't fret if you can't get it-  this one is mainly meant to be an eye-opener to what crazy things
#      you can do with functional programming

def digit_sort(digits):
    pass

#answer (NOTE: Took me a long-ass time to figure out)
def digit_sort(digits):

	orders = {'1': 0, '4': 1, '3': 2, '5': 3, '9': 4, 
	'7': 5, '2': 6, '8': 7, '0': 8, '6': 9}

	result = '' 

	for num in sorted(digits, key = orders.__getitem__):
		result += num

	return int(result)


#10
# TODO do this, but without using the word `list`, and without using comprehensions.  You'll need to use the
#      unpacking operator `*`, and plain old []'s (no comprehension though)

def set_to_list(input_set):
    return list(input_set)

#answer
def set_to_list(input_set):
 	return [*input_set]  
	



