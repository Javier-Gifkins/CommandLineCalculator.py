# importing math module to gain access to various mathematical functions and constants
import math

# start an infinite loop to keep calculator running & get the first number from the user (integer)
while True:
    input1 = int(input("What is the first number?"))

    # ask the user for an operator
    operator = input("Which operator will you choose? [+/-/x/%/sqrt] ")

    # if user picks square root then a second input number is not required
    if operator == "sqrt":

        # compute the square root of the first number
        answer = math.sqrt(input1)

        # display the result
        print(f" The square root of {input1} = {answer}")

    # get the second number from the user
    else:
        input2 = int(input("What is your second number?"))