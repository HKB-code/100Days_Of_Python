import my_module

print(my_module.name)



import random

print(random.randint(1,9))

# random floating number
# random generate 0.0<=x<1.0
print(random.random())

# uniform generate 0.0<=x<=1.0
print(random.uniform(1,10))



toss = random.randint(0,1)
if(toss==0):
  print("Head")
else:
  print("Tails")
  
  
list = ["harshil", 22,"Jain"]
print(list)
print(list[0])

# extend(iterable)
# insert(i,x)
# remove(x): remove the first item from the list whose value is equal to x. It raises a ValueError. If there is no such item

list.extend([1,2,3])
print(list)

friends = ["harshil","peter","sam"]
# it can lead to an error that is list out of range ,(0,3)
print(friends[random.randint(0,len(friends))])
# The choice() method returns a randomly selected element from the specified sequence.

# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
print(random.choice(friends))

# The choices() method returns a list with the randomly selected element from the specified sequence.

# You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.

# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

print(random.choices(friends))