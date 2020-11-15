"""Learn List functions"""

# I watch this course : https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

lucky_numbers = [4, 14, 17, 21, 10, 3]
friends = ["Karen", "Hugo", "Adèle", "Corine", "Pascal"]

## Some functions

friends.extend(lucky_numbers) #Get the lists together
friends.append("Tom")# Add individual element to the end of the list
friends.insert(1, "Sebastien") # Inserts an element to a list at a specific index mentioned
friends.remove("Karen") # Removes an item from the list
friends.clear() # Get rid of all the elements of the list
friends.pop() # Removes the last element of the list
friends.sort() # Sorts the list in an alphabetical way or ascending order for numbers
friends.reverse() # Reverses a list
friends2 = friends.copy() # Copies the friends list in friends2
print(friends.index("Karen")) # Tells me if there is a Karen in the list friends (his index)
print(friends.count("Corine")) # Tells me how many times Corine is in the list
print(friends)