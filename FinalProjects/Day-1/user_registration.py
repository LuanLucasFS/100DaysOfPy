# This is a program to simulate an user registration process.
# The user will be asked to provide their name, age, email and password.
# The program will then print the user's information.
# This program doesn't have any type of confirmation nor validation.
# It's just a simple program to show how to get user input and print it back.

print("Hello! Welcome to my app.")
print("To use our app you need to register first.")
print("Let's start the registration process.")

# Get user's name
name = input("What's your name?\n")
# Get user's age
age = input(f"How old are you?\n")
# Get user's email
email = input("What's your email?\n")
# Get user's password
password = input("Create a password\n")

print("Thank you for your cooperation. You are now registered.")

print("Name: " + name)
print("Age: " + age)
print("Email: " + email)
print("Password: " + password)
