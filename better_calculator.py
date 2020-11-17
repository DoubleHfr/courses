"""Building a better calculator"""

# I'm following this tutorial : https://www.youtube.com/watch?v=rfscVS0vtbw&t=52s&ab_channel=freeCodeCamp.org

num_1 = float(input("Please enter a number: "))
op = input("Enter operator: ")
num_2 = float(input("Please enter another a number: "))

if op == "+":
    print(num_1 + num_2)

elif op == "-":
    print(num_1 - num_2)

elif op == "/":
    print(num_1/num_2)

elif op == "*":
    print(num_1*num_2)

else :
    print("Invalid operator")
