
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# TODO write a `ChildrensBook` class that inherits from Book
#      `ChildrensBook` inherits from `Book` because its a subset
#      of Book, and needs to contain every property a Book does

# TODO write a `Bookshelf` class, which contains a books property
#      Bookshelf does NOT inhert from Book, because it is not a subset
#      of book, i.e. it does not contain an author or title
#      it is comprised of books, so it should conains a books property

# =====================================================================


class Dessert:
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe


# TODO write a `Cake` class, making use of `Dessert` if at all possible


# TODO write a `Meal` class, making use of `Dessert` if at all possible


# TODO write an `Ingredient` class, making use of `Dessert` if at all possible


# TODO write a `Plate` class, making use of `Dessert` if at all possible


# TODO write a `Food` class, making use of `Dessert` if at all possible


# NOTE not all of the above can make use of the `Dessert` class. 
# Some will inherit from it, others contain a deserts property. 
# Its practice using your own judgement to see what depends on what


# TODO Modify `Dessert` to inherit from any of the above classes you wrote,
# if applicable, and to include any of them as properties as you see fit.
# Not all of the classes can/should be used inside `Dessert`



# =====================================================================

class Lamborghini(Car):
    # class properties

    def __init__(self, *vargs):
        # object properties
        pass


# TODO modify `Lamborghini` to include two class properties and two object properties

# Keep in mind that class properties hold their specific value
# across all instances of Lamborghini's, while object properties
# vary from Lamborghini to Lamborghini. 

# For example:

class IPhone(Phone):
    wireless = True # all IPhone's are wireless, but not all `Phone`s are
    smart = True # same as above

    def __init__(self, generation, capacity):
        self.generation = generation # varies from IPhone to IPhone
        self.capacity = capacity # same as above



# ===============================================================


# TODO make three classes- Sofa, Furnature, and Cushions, 
# inheriting as you see fit. Include a class property for both sofa 
# and furnature, and at least one object property for all three.
