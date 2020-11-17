"""comparisons"""

# I'm still watching this great course :  https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

#Global variables : 

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else :
        return num3

print(max_num(3,2,8))

# Comparisons signs

## "==" checks if the values are equals
## "">=" greater of equals
## "!=" checks if it's not equal