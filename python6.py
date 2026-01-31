"""
#
# Functions
#
"""
def myFullName(firstName="Unknown", lastName="Forger"):
    return firstName + " " + lastName
print(myFullName("Eden", "Kamado"))
print(myFullName("Loid"))  
print(myFullName())
print(myFullName(lastName="Smith"))  # Using keyword argument

def redPotion(hp):
    return hp + 50
def bluePotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:", current_hp)
current_hp = redPotion(current_hp)
print("HP after red potion:", current_hp)