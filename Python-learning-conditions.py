# Learning if, else, and elif statements in Python
# This script demonstrates the use of conditional statements in Python.

# Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")

# Example 2: if-else statement
temperature = 30
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's a cool day.")

# Example 3: if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Example 4: Nested if statements

number = 10
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")


# Example 5: Using logical operators in conditions

is_raining = True
has_umbrella = False
if is_raining and not has_umbrella:
    print("You need to stay indoors.")
else:
    print("You can go outside.")


