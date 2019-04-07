# The goal of this exercise is to get hands-on experience working with 
# list comprehensions, and other comprehensions. Write a complementary
# function to each of the below, which accomplishes the same logic in 
# a one-liner (using list/set/dict comprehensions).

# Exercise 1
# Adds 5 to each element
def add_five(numbers):
    out = []
    for num in numbers:
        out.append(num + 5)
    return out

# TODO Complete this function
def add_five_one_liner(numbers):
    pass


# Exercise 2
# Drops any small numbers (strictly less than 4)
def drop_small(numbers):
    out = []
    for num in numbers:
        if not num < 4:
            out.append(num)
    return out

# TODO Complete this function
def drop_small_one_liner(numbers):
    pass


# Exercise 3
# Returns a *set* of all distinct numbers (i.e. no repeats)
def get_distinct(numbers):
    out = set()
    for num in numbers:
        out.add(num)
    return out

# TODO Complete this function
def get_distinct_one_liner(numbers):
    pass



## Helper testing functions, for your convienence ##

def test_add_five(numbers):
    out1 = add_five(numbers)
    out2 = add_five_one_liner(numbers)
    assert(out1 == out2)

def test_drop_small(numbers):
    out1 = drop_small(numbers)
    out2 = drop_small_one_liner(numbers)
    assert(out1 == out2)

def test_get_distinct(numbers):
    out1 = get_distinct(numbers)
    out2 = get_distinct_one_liner(numbers)
    assert(out1 == out2)

# Main method
def main():
    # Feel free to add anything you need to test your solutions here
    pass

if __name__ == "__main__":
    main()
