

# TODO: use list comp AND zip
def subtraction(numbersA, numbersB):
    out = []
    for i in range(min(len(numbersA), len(numbersB))):
        out.append(numbersA[i] - numbersB[i])
    return out

# TODO use map and str- no comprehensions
def letters_in_string(word):
    return [letter for letter in word]


# TODO fill both of the following two functions in with some calculation (anything), and call them both.
#      don't edit the function's arguments

def calculate(input_list):
    pass

def calculat32(*vargs):
    pass

# ^ the pupose is so that you learn what the `*` does in the function signature
#  HINT: it makes it turn `n` separate arguments into a single list of those `n` values


# TODO use the short-circuiting behavior demonstated in the following function to the `ternary` into
#      an expression of `or`s and variables

# returns varA if varA is not 0/None/[]/False, otherwise returns varB
def short_circuit_demo(varA, varB):
    return varA or varB


# TODO use the above example to convert this function to `or`s
def ternary(varA, varB, varC):
    tmp = varC if varC else varA
    return varB if varB else tmp



# TODO return true is any of the values in `numbers` are greater than 3
#      use `any()` and a comprehension
def any_above_three(numbers):
    for num in numbers:
        if num > 3:
            return True
    return False


# TODO same behavior, except if all values are larger than 3
# hint: `all`
def all_above_three(numbers):
    for num in numbers:
        if num <= 3:
            return False
    return True


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

def index_of_same_element(numsA, numsB):
    pass



# TODO strip this solution down to 4 lines (including def ... ), by solely 
#       removing whitespace and adding `;` where need be

def random_thing(numbers, const):
    for num in numbers:
        if 3 < num < 12:
            return True
     temp = const + max(numbers)
     return tmp




# TODO sort a string consisting solely of digits (there may be duplicates) in the following order
#      1 < 4 < 3 < 5 < 9 < 7 < 2 < 8 < 0 < 6
#      don't fret if you can't get it-  this one is mainly meant to be an eye-opener to what crazy things
#      you can do with functional programming
def digit_sort(digits):
    pass


# TODO do this, but without using the word `list`, and without using comprehensions.  You'll need to use the
#      unpacking operator `*`, and plain old []'s (no comprehension though)

def set_to_list(input_set):
    return list(input_set)


