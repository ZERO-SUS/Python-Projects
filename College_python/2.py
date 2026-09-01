num = int(input("Enter a number :"))
print("""1. Sum
2. Factorial
3. Exit""")
user = int(input("Enter the (option 1,2,3):"))

def sum(num):
    if (num ==0):
        return 0
    else:
        return num + sum(num - 1)
def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)
if user == 1:
    print(f"The sum of {num} is : {sum(num)}")
elif user == 2:
    print(f"The Factorial of {num} is : {factorial(num)}")
else:
    print("Exit")