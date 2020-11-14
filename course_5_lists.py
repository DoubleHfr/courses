"""learn what's list and how to deal with a large amount of data"""

# I watch this course : https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

#TODO list my favorites colors

my_fav_colors = ["Blue", "Green", "Grey", "Cyan", "Magenta", "Yellow"] # A square bracket allows us to store a list a values
## You can also store numbers and boleans in a list 

# How to access individual elements in a list ? 
## You can refer to their index just as we saw before. 

print(my_fav_colors[1]) # It will returns me the green color

## Let's grab to elements like green and grey

print(my_fav_colors[1:]) # The ":" refers to a column and grabs the element at index 1 + the elements left from there

# I can also specify a range

print(my_fav_colors[1:3]) # It grabs the element at index position one to the index position three but without including it