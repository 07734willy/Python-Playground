#1
def make_dict(keys, values):
    out = dict()
    for i in range(min(len(keys), len(values))):
        out[keys[i]] = values[i]
    return out


#answer
def make_dict(kets, values):
	return {keys[i]:values[i] for i in range(len(keys))}

def make_dict(keys, values):
    return {key, value for key, value in zip(keys, values)}

#2
def large_elements(matrix):
    out = []
    for row in matrix:
        for elem in row:
            if elem > 4:
                out.append(elem)
    return out

#answer
def large_elements(matrix):
	return [elem for row in matrix for elem in row if elem > 4]
# nothing to improve

#3
def matrix_transpose(matrix):
    out = []
    for i in range(len(matrix[0])):
        elem0 = matrix[0][i]
        elem1 = matrix[1][i]
        out.append([elem0, elem1])
    return out

#answer
def matrix_transpose(matrix):
	return list([[matrix[0][i], matrix[1][i]] for i in range(len(matrix[0]))])

def matrix_transpose(matrix):
    return [list(tup) for tup in zip(matrix[0], matrix[1])]

# OR

def matrix_transpose(matrix):
    return [list(tup) for tup in zip(*matrix)]


#4
def max_every_other(numbers):
    out = []
    for i in range(0, len(numbers), 2):
        out.append(max(numbers[i], numbers[i+1]))
    return out

#answer
def max_every_other(numbers):
	return [max(numbers[i], numbers [i+1]) for i in range(0, len(numbers),2)]


def max_every_other(numbers):
    return [max(pair) for pair in zip(numbers[::2], numbers[1::2])]


#5
def repeat_elements(counts):
    out = []
    for count in counts:
        tmp = []
        for _ in range(count):
            tmp.append(count)
        out.append(tmp)
    return out

#answer
def repeat_elements(counts):
	return [[count] * count for count in counts]	
#nothing to improve

#6
def power_of_twos():
    start = 0
    while True:
        yield 2 ** start
        start += 1

#answer
def power_of_twos():
	yield (2 ** x for x in itertools.count(0,1))
#nothing to improve

#7

# I don't really understand #7 :( 

"\n".join(", ".join(str(e) for e in row) for row in matrix)
