
# Makes a dictionary out of two lists (keys and values)
def make_dict(keys, values):
    out = dict()
    for i in range(min(len(keys), len(values))):
        out[keys[i]] = values[i]
    return out
# HINT: there's special syntax for a dict comprehension


# Takes a 2D matrix (any size), and returns a plain list of elements that
# it contains, which are larger than 4
def large_elements(matrix):
    out = []
    for row in matrix:
        for elem in row:
            if elem > 4:
                out.append(elem)
    return out


# Takes a 2D matrix (with only two rows) and flips it across its diagonal
# [[1, 7, 4],             [[1, 3],
# [[3, 2, 5]]   becomes    [7, 2],
#                          [4, 5]]
def matrix_transpose(matrix):
    out = []
    for i in range(len(matrix[0])):
        elem0 = matrix[0][i]
        elem1 = matrix[1][i]
        out.append([elem0, elem1])
    return out
# HINT: You'll need to use `zip()`


# Returns a list taking the max out of every two numbers
# [7, 1, 9, 10]  gives  [7, 10]
def max_every_other(numbers):
    out = []
    for i in range(0, len(numbers), 2):
        out.append(max(numbers[i], numbers[i+1]))
    return out
# HINT: again, `zip()`


# Forms lists of repeating elements, from a list of elements. Ex:
# [1, 2, 1, 4] produces
# [[1], [2, 2], [1], [4, 4, 4, 4]]
def repeat_elements(counts):
    out = []
    for count in counts:
        tmp = []
        for _ in range(count):
            tmp.append(count)
        out.append(tmp)
    return out


# A generator producing all powers of two on-demand
def power_of_twos():
    start = 0
    while True:
        yield 2 ** start
        start += 1
# HINT: this is a generator. Generator comprehensions use `()` instead 
#       of `[]`. Additionally, you'll want `count()` from `itertools`
#       `from itertools import count` at the top of the file


# Takes a matrix, and return a string in csv format
def make_csv(matrix):
    out = ""
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if i != 0:
            out += "\n"
        for j in range(cols):
            if j != 0:
                out += ", "
            out += str(matrix[i][j])
    return out
# HINT: you can use str.join() to join a bunch of strings into one.
#       "RR".join(["foo", "bar", "fizz", "buzz"]) yields
#       "fooRRbarRRfizzRRbuzz"
