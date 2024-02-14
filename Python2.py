num1 = float(input("Please input the first number: "))
num2 = float(input("Please input the second number: "))

multiplication_result = num1 * num2

if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Division by zero is undefined"

print("The multiplication of", num1, "and", num2, "is:", multiplication_result)
print("The division of", num1, "by", num2, "is:", division_result)