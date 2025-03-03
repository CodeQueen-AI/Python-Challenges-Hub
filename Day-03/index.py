# Write a Python program that takes a number from the user and checks whether it is even
num = int(input("Enter a Number: "))
if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is not an Even number")

# Write a Python program that takes a number from the user and checks whether it is odd
num = int(input("Enter a Number: "))

if num % 2 != 0:
    print(f"{num} is an Odd number")
else:
    print(f"{num} is not an Odd number")

#Write a Python program that takes a number from the user and checks whether it is a prime number or not!
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a Number: "))
if prime(num):
    print("Yes! it's a Prime Number")
else:
    print("No! it's not Prime Number")
