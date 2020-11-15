"""Learning if statements"""

# I watch this course : https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

## Let's start with writing an exemple :

# Variables :
is_male = True
is_tall = True

if is_male:
    print("You are a male") # everything inside the indentation will be part of the condition

else: # = Otherwise
    print("You're not a male")

# We can also check two condition on the same time with the "or" keyword

if is_male or is_tall:
    print("Your are a male or tall or both") # This is exactly how the "or" keyword works

else: # If a else is used it means that none of the two conditions above is complete
    print("Your are neither male nor tall") # Obviously

# We can also use the "and" keyword & the "elif" keyword

if is_male and is_tall: # The two conditions has to be completed to run.
    print("Your are a tall male")
elif is_male and not(is_tall): # "Elif" stands for else if (sinon si) "and not" and not obviously. 
    print("Your are a short male") #Please note that the "and not" keyword will negate the bolean. eg. turn into false if it's true and vice versa
elif not(is_male) and is_tall: # Same process but applied to is male and is tall to cover all the possibilities.
    print("Your are not a male but you're tall")
else:
    print("Your are neither a male nor tall or even both")
