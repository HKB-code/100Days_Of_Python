programming_dictionary={
  'Bug':"An error ina aprogram that prevents the program from running as expected ",
  'Functions':"A piece of code that you can easily call over and over again",
   'Loop':"The action of doing something over and over again" ,
   123: "integer"
   
}
# when you're trying to retrieve the data from that key,you also have to make sure that you provide the key in its actual data type.
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

programming_dictionary["Bool"] = "True/False"

print(programming_dictionary)

empty_dictionary = {}


# wipe the existing dictionary
# programming_dictionary = {}
# That can be really useful if you wanted to clear out a user's progress,

# or for example, if a game restarts, then all the scores and stats will probably have to be wiped empty.

# So this is one way that you could do that.
# print(programming_dictionary)


# edit an item in an dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])


  capitals = {
  "France": "Paris",
  "Germany":"Berlin"
  }

# Nested list in dictionary
# travel_vlog = {
#   "France": ["Paris","Lille","Dijon"],
#   "Germany": ["Stuttgart","Berlin"]
# }

# Print lille
# print(travel_vlog["France"][1])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

num_entries = int(input("How many ebtries you want to add?"))

dicts = {input(f"Enter the Key {i+1} "): input(f"Enter the Value { i+ 1}") for i in range(num_entries) }
print(dicts)

use_dict = {}
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print({**dict1,**dict2,**use_dict})



n = int(input("How many ebtries you want to add?"))
dict = {}
for i in range(n):
  key = input("key")
  value = input("value")
  # dict[key]  = value
  dict.update({key:value})

print(dict)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

for key, value in d2.items():
  d1[key] = value

print(d1)

# Without Overwriting Existing Keys
# If you want to add key-value pairs without overwriting existing keys, you can use the setdefault() method or a custom approach.

# Using setdefault()
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# for key, value in dict2.items():
#     dict1.setdefault(key, value)

# print(dict1)

for key, value in dict2.items():
  if key in dict1:
    if isinstance(dict1[key],list):
      dict1[key].append(value)
    else:
      dict1[key] = [dict1[key],value]
  else:
    dict1[key] = value

print(dict1)