def add_five(numbers):
    out = []
    for num in numbers:
        out.append(num + 5)
    return out

# TODO Complete this function
def add_five_one_liner(numbers):
    return [num + 5 for num in numbers]

def drop_small(numbers):
    out = []
    for num in numbers:
        if not num < 4:
            out.append(num)
    return out

# TODO Complete this function
def drop_small_one_liner(numbers):
    return [num for num in numbers if num < 4]

def get_distinct(numbers):
    out = set()
    for num in numbers:
        out.add(num)
    return out

# TODO Complete this function
def get_distinct_one_liner(numbers):
    return set(num for num in numbers)