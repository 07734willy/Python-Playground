#1
def do_something(x, y):
    return x + y

#answer:
do_something = lambda x,y: x + y
#nothing to change

#2
def drop_value(numbers, value):
    return [num for num in numbers if num != value]

#answer:
numbers = [1,2,3]
target = [1]

drop_value = list(filter(lambda value: value not in target, numbers))
#nothing to change

#3
def find_max_vals(matrix):
    return [max(row) for row in matrix]

#answer:
find_max_vals = list(map(lambda matrix: max(matrix),[[1,2,3], [4,5,6]]))

def find_max_vals(matrix):
    return list(map(max, matrix))

#4
def get_digits(number):
    return [int(digit) for digit in str(number)]

#answer:
get_digits = list(map(lambda number: int(number), list(str(235))))

def get_digits(number):
    return map(int, number)

#5
def sort_lists(*lists):
    tuples = [(len(row), row) for row in lists]
    tuples.sort()
    return [row for length, row in tuples]

#answer:
sort_lists = lambda *lists: sorted(lists)

def sort_lists(*lists):
    return list(map(sorted, lists))

#6
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

#answer:
get_abs_min = lambda numbers: min(abs(num) for num in numbers)

def get_abs_min(numbers):
    return min(numbers, key=abs)

#7
def max_row_sum(matrix):
    return max(sum(e for e in row) for row in matrix)

#answer:
max_row_sum = lambda matrix: max(sum(array) for array in matrix)

def max_row_sum(matrix):
    return max(matrix, key=sum)

#8
def count_nonzero(numbers):
    return len([num for num in numbers if num != 0])

def count_nonzero(numbers):
    return sum(map(bool, numbers))

#my 'genius' answer
count_nonzero = lambda numbers: len(numbers) - numbers.count(0)
