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
