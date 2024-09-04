# object initialization.

# note when an instance does not have defined attributes, they can de assign attributes using the dot notation. as follows.

class Dog:
    pass

fido = Dog()
snoppy = Dog()

# modifiying their attributes using the dot notation.
fido.breed = 'german shephard'
snoppy.breed= 'bull dog'
print(fido.breed)
print(snoppy.breed)

# to provide objects with unique attributes upon instations we use the __init__ method.

# __init__ 
# every time we initialize an object, the python interpteter calls a magic method called __init__.
# magic methods are special methods to be called by developers but are invoked by different cues and operators that act on their objects.
#  the __init__ method can be used in every class. though is invoked when you initialize a class.
# for example

class Another_Dog:
    def __init__(self):
        print("A dog is born!")

    #creating a personalized method.
    def bark(self):
        print("Woof!") 

fido = Dog() # this will return "A dog is born"

# __init__ can be modified to takes some arguments. this allows us to customize the behaviour of unique objects.

class SecondDog:
    def __init__(self, name):
        print(f"{name} is born!")

    def bark(self):
        print("Woof!")

    def showing_self(self):
        print(f"hello there {self}")
        return self
           

fido = SecondDog("Fido")
print(fido)
snoppy = SecondDog("Snoppy")
print(snoppy)
print(fido.showing_self())
# self 
# modifying __init__ has allowed us to provide individul instances of the class behaviours and attributes.
print(fido is fido.showing_self())
# inside the showing_self() method we use the self keyword.
# the self keyword refers to the instance or object that the showing_self() method is being called on.
# /so when we cann the showing_self() method in the isntance fido,the method will return the Dog isntace that id fido.


# operating on self in as isntance method.

class Dog:
    def __init__(self,name):
        self.name = name
    def dog_owner(self,  owner_name):
        self.owner = owner_name

doggy = Dog("doggy")
doggy.dog_owner("sharon")
print(doggy.owner)

# optional __init__ arguments.
# there are a number of things that are importantnto know about a dog before you adopt it.
# while other things are not as important. for example the dogs favourite toy.
#  to accomodate these lessimportant details, we can set default values in any method or function.

class AnotherDog:
    def __init__(self, weight, age, favourite_toy = "Any"):
        self.weight = weight
        self.age = age
        self.favourite_toy = favourite_toy
    def barking(self):
        print("woof!")
        return "woof!"

snoppy = AnotherDog("30kg", 8, "Tennis ball")

print(snoppy.barking())