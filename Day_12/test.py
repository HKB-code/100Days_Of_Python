# enemies = 1

# def increase_enemies():
#     enemies =2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # Local Scope
# def drink_potion():
#   potion_strength=2
#   print(potion_strength)
  
# drink_potion()
# # print(potion_strength)

# player_health=10

# def drink_potions():
#   potion_strength=2
#   print(player_health)
  
# drink_potions()


# The most important thing to remember from this is if you create a variable within a function, then

# it's only available within that function.

# But if you create a variable within an if block, or a while loop, or a for loop or anything that has

# the indentation and the colon, then that does not count as creating a separate local scope.
# In Python, the scope of variables created within if, for, while blocks, etc., is not limited to the block itself. They are accessible in the surrounding code as well.


# game_level = 3
# enemies1 = ["Skeleton", "Zombie","Alien"]

# def create_enemy():
#    if game_level<5:
#       new_enemies = enemies1[0]
#       print(new_enemies)
      
# create_enemy()


# Not a good way of programming always create a local variable so that if certain conditions are not meet, you will not get a name error....
# game_level =13
# enemies = ["Skeleton", "Zombie","Alien"]

# def create_enemy():
#   new_enemies=""
#   if game_level<5:
#    new_enemies = enemies[0]
#   print(new_enemies)
  
# create_enemy()



# Modifying Global Scope
enemies = 1
 
# def increase_enemies():
#    global enemies
#    enemies += 2
#    print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# dont try to modify it within a function that has local scope
# instead return from it 


def increase_enemies(enemy):
   
   print(f"enemies inside function: {enemies}")
   return enemy+2

enemies =increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


# Global Constants: You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to modifiy them.Global constants are normally declared in ALL_CAPS with a underscore in between..
PI= 3.14
GOOGLE_URL = 'https://www.google.com'

def my_func():
  print(PI)
  print(GOOGLE_URL)
my_func()

# x=30
# def ok():
#   # x+=1
#   print(x)
# ok()