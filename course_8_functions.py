"""functions"""

# I watch this course : https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

# A function is a collection of code which performs a specific task

#TODO Create a function that says Hi ! to the user. 

## There's a lot to say here : You must use the keyword "def" to start a function.
### Always use descriptive name to your functions
#### Then you got to write ":" to say to python that all the code below is part of the function. All the code included to a function must be indented

def say_hi():
    print("Hello User !")

# To execute a function you have to "call" it. This way :

say_hi()

## You can get your function more powerfull if you give it parameters

def say_hi_2(name):
    print("Hello"+ name+" !\n How are you doin' ?")

say_hi_2(" Hugo")
say_hi_2(" Wonderer")

# Let's give it two parameters

def say_hi_with_age(name, age):
    print("Hello"+ name+"\nYou're "+ str(age))

say_hi_with_age(" Hugo", 23)