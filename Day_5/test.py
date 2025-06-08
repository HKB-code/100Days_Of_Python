import random
for i in range(5):
    print(i)
    friends = ["Rolf","sam","henry"]
print(friends[0])
# In Python, variables defined inside a loop are still available outside the loop, as long as they were not declared inside a function or a block with a more restrictive scope.
# Here, friends is created inside the loop, but since Python doesn't have block-level scope (like C++ or JavaScript), friends remains accessible even after the loop ends. So, print(friends[0]) will output "Rolf" without any issue.

n = int(input("enter number"))
strNum = ""
for i in range(n+1):
    if(i>0):
        strNum+=str(i)
print(strNum)

fruits = ["Mango","apple","grapes"]
for fruit in fruits:
  print(fruit+"pie")
for i in range(0,20,2):
  print(i)


# sum(iterable, start)
# max(n1, n2, n3, ...)
# Or:
# max(iterable)

st_score = [212,89,112,150,56,95,2199]
hig_score = st_score[0]
for i in st_score:
   if(hig_score<i):
      hig_score = i
print(hig_score)


z =0 
for i in range(0,101):
   z+=i
print(z)

for i in range(1,101):
   if(i%3==0) and (i%5==0):
      print("FIZZBUZZ")
   elif(i%5==0):
      print("Buzz")
   elif(i%3==0):
      print("Fizz")
   else:
      print(i)
