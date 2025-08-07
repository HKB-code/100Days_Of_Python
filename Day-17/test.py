class Order:
    pass
    """Well, if we actually really want to leave this function or this class empty, we can use a keyword
which is 'pass'.
And all it does is it just passes.
It says, I don't want to have a go right now.
Just continue to the next line of code."""
 
# of course to initialize an object from a class we have to add the parentheses at the end.
order_1 = Order()

"""How can I specify all these starting pieces of information

when I create my object from the class? Now,

in order to do this, we have to understand something called a constructor,

which is a part of the blueprint that allows us to specify what should happen

when our object is being constructed.

And this is also known in programming as initializing

an object. When the object is being initialized,

we can set variables or counters to they're starting values."""

class User:
    def __init__(self):
        """this init function is where we initialize or create the starting
values for our attributes. Now,
the important thing to remember is that the init function is going to be called
every time you create a new object from this class."""
        print("new user created")
        """We have our init function and inside the init function

in addition to this thing called self

which is the actual object that's being created or being initialized,

in addition, you can add as many parameters as you wish.

And that parameter is going to be passed in when an object gets constructed from

this class. And once you receive that data,

then you can use it to set the object's attributes."""
user_1 = User()

"""We know that we can create an object by calling the name of the class and then

adding the parentheses. But if inside our init function

we have some additional parameters,

then we can also pass in data to those parameters

which will be used to set the attributes for that object.

So in this case, once this line of code has completed,

then my_car.seats is going to be equal to five.

And this is exactly the same as if we created our

my_car object first and then we said my_car.seats = 5.

It's completely the same.

But it does make it a lot quicker when you're creating a lot of objects that

need all the same attributes"""

class Car:
    def __init__(self,seats):
        self.seats = seats

casr_1 = Car(5)
print(casr_1.seats)


class Cheff:
    """remember that when you add parameters to the constructor

which is the init function,

you're now saying that whenever a new object is being constructed from this

class, it must provide these two pieces of data."""
    def __init__(self,id,username):
        self.id = id
        self.username  = username
        #default attributes
        self.rating = 0
        self.followers = 0
        self.following = 0
        """ Now a method,

unlike a function, always needs to have a self parameter as the first parameter.

This means that when this method is called,

it knows the object that called it."""
    def follow(self,cheff):
            cheff.followers+=1
            self.following+=1

cheff_1 = Cheff(1,"john")
cheff_2 = Cheff(2,"peter")  
  
cheff_1.follow(cheff_2)
print(cheff_1.followers)
print(cheff_1.following)
print(cheff_2.followers)
print(cheff_2.following)

print(cheff_1.id)

"""So the self keyword becomes quite important when we're working with classes and

objects. It's a way for us to refer to the object

that's going to be created from this class inside the class blueprint.

So you'll never see self when you're using objects

but you see it a lot when you're writing your code inside your class."""