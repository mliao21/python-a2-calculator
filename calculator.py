# calculator.py
# Melissa Liao
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 2 git repository.
#


# Prints out a brief instruction on what information needs to be provided by the user.
print("Please indicate 3 integer values and 2 operators to calculate your expression: ")


# get_integer prompts the user to input a number. Values will be returned as integer type.
def get_integer(i):
    num = input("Enter your integer value #" + str(i + 1) + ": ")
    return int(num)

# get_operator prompts the user to input an operator.
def get_operator(i):
    while True:
        # The user must input in any of the 4 basic operators.
        # Otherwise, it will loop and prompt for re-entry until valid operator is inputted. 
        op = input("Enter your operator #" + str(i + 1) + ": ")
        if op not in ("+", "-", "*", "/"):
            print("Entered value is not a valid operator.")
        elif op in ("+", "-", "*", "/"):
            break
    return op

# Sets a number of times the user can input its integer and operators.
num_of_int = 3
num_of_op = num_of_int - 1

# Empty lists that stores the values input by the user. 
# Integers and operators are in separate list.
n = []
o = []

# Executes the get_integer function by the number of times (3) provided.
# And adds the inputted integer values to list 'n'. 
for i in range(num_of_int):
    a = get_integer(i)
    n.append(a)

# Executes the get_operator function by the number of times (2) provided.
# And adds the inputted operator values to list 'o'. 
for i in range(num_of_op):
    b = get_operator(i)
    o.append(b)

# operator_zero compares the first inputted string operator value with the corresponding arithmetic operation.
# Once value matches with the value of the criteria, it will return to execute the arithmetic function.
def operator_zero(x,y):
    if o[0] == '*':
        return x * y
    elif o[0] == '/':
        return x / y
    elif o[0] == '+':
        return x + y
    elif o[0] == '-':
        return x - y

# operator_one does the same as operator_zero but instead it compares with the second inputted operator.
def operator_one(x,y):
    if o[1] == '*':
        return x * y
    elif o[1] == '/':
        return x / y
    elif o[1] == '+':
        return x + y
    elif o[1] == '-':
        return x - y

# get_result determines the correct order of the operation. 
# It also calculates the result from the values inputted by the user. 
def get_result():
    if o[0] in ('*', '/'):
        return operator_one(operator_zero(n[0],n[1]), n[2])
    else:
        return operator_zero(n[0], operator_one(n[1],n[2]))

# Prints out all the values inputted by the user in an mathematical expression with its result. 
print("Your calculated result: ", n[0], o[0], n[1], o[1], n[2], "= ", get_result())







