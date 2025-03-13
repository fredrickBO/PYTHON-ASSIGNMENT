print("1. Add")
print("2. Subtract")
print("3. Division")
print("4. Multiple")

operation = input()
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if operation == "1":
  result = str(int(num1) + int(num2))
  print("sum is " + result)

elif operation == "2":
  result = str(int(num1) - int(num2))
  print("The difference is " + result)

elif operation == "3":
  result = str(int(num1) / int(num2))
  print("The division is " + result)

elif operation == "4":
  result = str(int(num1) * int(num2))
  print("The multiplication is " + result)

else:
  print("Invalid entry, try again!")
