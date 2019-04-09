

# TODO Implement this, using `lambda` instead of `def`
def do_something(x, y):
    return x + y


# TODO Implement this using `filter`
def drop_value(numbers, value):
    return [num for num in numbers if num != value]


# Find the max of each list
# TODO Implement this using `map` and `max`
def find_max_vals(matrix):
    return [max(row) for row in matrix]


# Convert a numerical value to a sequence of its digits
# TODO Implement this using `map`
def get_digits(number):
    return [int(digit) for digit in str(number)]


# Sort the lists based on length
# NOTE This function accepts multiple lists, not a list of lists
# TODO Implement this using `sort()` or `sorted()`
def sort_lists(*lists):
    tuples = [(len(row), row) for row in lists]
    tuples.sort()
    return [row for length, row in tuples]

# Take the min value of the array, based on absolute value / magnitude
def get_abs_min(numbers):
    try:
        non_neg_min = min(num for num in numbers if num >= 0)
    except: non_neg_min = -1
    try:
        neg_min = max(num for num in numbers if num < 0)
    except: neg_min = 1

    if neg_min == 1:
        return non_neg_min
    if non_neg_min == -1:
        return neg_min
    if abs(neg_min) < non_neg_min:
        return neg_min
    return non_neg_min

# Calculate the largest sum of any row of elements in the matrix
# TODO Implement this using `map`
def max_row_sum(matrix):
    return max(sum(e for e in row) for row in matrix)


# Count the number of non-zero elements in the array
# TODO Just don't use list comprehensions
def count_nonzero(numbers):
    return len([num for num in numbers if num != 0])
