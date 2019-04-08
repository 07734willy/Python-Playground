def remainder_one(elements):
    out = []
    counter = 0
    for element in elements:
        if counter % 5 != 1:
            out.append(element)
        counter += 1
    return out


#solution
def remainder_one(elements):
	return [num[1] for num in enumerate(elements) if num[0] % 5 != 1 ]

# Takes a list of tuples ex. [(1, 3), (2, 4)], and reverses each tuple
def flip_elements(elements):
    out = []
    for element in elements:
        a = element[0]
        b = element[1]
        out.append((b, a))
    return out

#solution
def flip_elements(elements):
	return [list(tuple(reversed(num))) for num in elements]



	# Finds pairs of +/- pairs of numbers ex. 6 and -6, or -4 and 4
# returns a list of these pairs as tuples (with duplicates)
def find_pairs(elements):
    out = []
    for a in elements:
        for b in elements:
            if a == -b:
                out.append((a, b))
    return out

#solution
def find_pairs(elements):
	return  set((a,b) for a in elements for b in elements if a == -b)





# Takes the max element out of the two lists at each index.
# So [0, 1, 9] and [2, 3, 4] yields [2, 3, 9]
def take_max(numbers1, numbers2):
    out = []
    for i in range(min(len(numbers1), len(numbers2))):
        a = numbers1[i]
        b = numbers2[i]
        out.append(max(a, b))

#solution
def take_max(numbers1, numbers2):
	return [max(num) for num in zip(numbers1, numbers2)] 



