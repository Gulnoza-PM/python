def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Enter number: "))
exp = int(input("Enter its degree: "))
print("The result of exponentiation is:", power(base, exp))