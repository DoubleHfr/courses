"""working with strings"""

# I watch this course : https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

print("Hugo\nBruneau") # If you put a \n in the middle of a string it will create a new line within the string
print("Hugo\" Bruneau") # If I want to put a " in my string I can do the same process as above 

name = "Hugo Bruneau" # A Variable

print(name + " is cool") #Concatained my variable and a string using "+" sign

#TODO Using basic functions to work with strings

print(name.lower()) # It turns my string into caps unlocked
print(name.upper()) # It turns my string into caps locked
print(name.isupper()) # Checks if my string is intirely in caps locked
print(len(name)) # checks the lengh of a string

print(name[0]) #Grabs a specific character in my string (the index starts at 0)
print(name.index("u")) #Tells me in which index is located the "u" is in the string eg. where is the u. 
## Please note that in the index function we can also put full words in it and it will returns where the word starts

print(name.replace("Bruneau", "Lisner")) # Remplace a selected part of the string by another

## We can also combine functions
print(name.upper().isupper())

