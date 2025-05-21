import time


def print_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def analyze_even_odd(first_number_result, second_number_result):
    if first_number_result == "even" and second_number_result == "even":
        print("Both numbers are even.")
    elif first_number_result == "odd" and second_number_result == "odd":
        print("Both numbers are odd.")
    else:
        print("One number is even and one is odd.")

def calculate_num(first_number, second_number):


        operator = input("Operator (+, -, *, /) or 'exit' to quit: ")

        if operator == "+":
            result = (first_number + second_number)
            print(str(first_number)+ "+"+ str(second_number) + " = ", result)
        elif operator == "-":
            result = (first_number - second_number)
            print(str(first_number)+ "-"+ str(second_number) + " = ", result)
        elif operator == "*":
            result = (first_number * second_number)
            print(str(first_number)+ "*" +str(second_number) + " = ",result)
        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(str(first_number)+ "/" +str(second_number) + " = ", first_number / second_number)
        else:
            print("Invalid operator. Try again.")





name = input("Please enter your name: ")
print( "Hi " +name + " ,nice to meet you "  )
print("This is a special calculator, i would need two numbers from you ")

first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

print("First number " +str(first_number))
print("Second number " +str(second_number))
print(f"Thank you for putting in your numbers, {first_number} and {second_number}")

first_number_result = print_even_odd(first_number)
Second_number_result = print_even_odd(second_number)

print("I can see that the first number is: " + first_number_result)
print("And the second is " + Second_number_result)
analyze_even_odd(first_number_result,Second_number_result)

calculate_num(first_number, second_number)
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Thank you {name} for using the calculator on {current_time}")






