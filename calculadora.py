import sys

# Python types:
#  str, i.e. "test"
#  int, i.e. 1
#  bool, i.e. True
#  ...

# configuration of calculator
success_message = "Great, you entered an integer"
error_message = "You did not enter an integer. Program will stop now"

print("Please enter number one:")
number_one = input()

try:
    number_one = int(number_one)
    print(success_message)
except:
    print(error_message)
    sys.exit(0)

print("Please enter operation - your options are: +, -, *,/")
operation = input()

print("Please enter number two:")
number_two = input()
try:
    number_two = int(number_two)
    print(success_message)
except:
    print(error_message)
    sys.exit(0)


if operation == "+":
    print("you want to make an addition. Ok, i will sum up")
    result = number_one + number_two
    print("Result addition:", result)
elif operation == "-":
    result = number_one - number_two
    print("Result rest:", result)
elif operation == "*":
    result = number_one * number_two
    print("result mult", result )
elif operation == "/":
    result = number_one / number_two
    print("result div", result)
else:
    print("Sorry, you did not enter a valid operator")


    


