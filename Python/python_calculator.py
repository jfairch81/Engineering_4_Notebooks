# Jude Fairchild - Adapted With Harry DH
# Calculator Program that adds, subtracts, multiplys, divides, and mods

# Addition Function
def add(x, y):
    return x + y

# Subtraction Function
def subtract(x, y):
    return x - y

# Multiplication Function
def multiply(x, y):
    return x * y

# Division Function
def divide(x, y):
    return x / y
# Modulo Function
def mod(x, y):
    return x % y
# Choose your type
print("Select operator: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
while True:
    
	operator = input("Enter operator (1/2/3/4/5): ") # takes input

	if operator in ('1', '2', '3', '4', '5'):
		num1 = float(input("Enter the  first number: "))
		num2 = float(input("Enter the second number: "))

		if operator == '1': # add
			 print(num1, "+", num2, "=", add(num1, num2))
		elif operator == '2': # sub
			print(num1, "-", num2, "=", subtract(num1, num2))
		elif operator == '3': # mult
			print(num1, "*", num2, "=", multiply(num1, num2))
		elif operator == '4': # div
			print(num1, "/", num2, "=", divide(num1, num2))
		elif operator == '5': # mod
			 print(num1, "%", num2, "=", mod(num1, num2))			 
		break # Breaks loop
	else:
		print("Try Again, Invalid")

