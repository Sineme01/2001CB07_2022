def factorial(num):
    return 1 if (num==1 or num==0) else num * factorial(num - 1)
number = int(input("Enter the number: "))
print("Factorial of",number,"is",
factorial(number))
