# importing math module to gain access to various mathematical functions and constants
import math

# start an infinite loop to keep calculator running & get the first number from the user (integer)
while True:
    input1 = int(input("What is the first number? "))

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
        input2 = int(input("What is your second number? "))

        # perform the calculation using the chosen operator
        if operator == "+":
            answer = input1 + input2 # addition

        elif operator == "-":
            answer = input1 - input2 # subtraction

        elif operator == "x":
            answer = input1 * input2 # multiplication

        elif operator == "%":
            answer = input1 // input2 # division

        # handling invalid user input
        else:
            print("I dont understand that.")

        # displaying calculator result
        print(f"{input1} {operator} {input2} = {answer}")

    # ask user if they want to perform another calculation
    choice = input("Do you want to perform another calculation? [Y/N] ")

    # if choice is 'n' calculator will stop
    if choice.lower() == "n":
        break