def solve(S, P):
    for x in range(1, S+1):
        if P % x == 0:
            y = P // x
            if x + y == S:
                return x, y
    return None

S = int(input("Enter the sum: "))
P = int(input("Enter the product: "))

result = solve(S, P)

if result is None:
    print("No solution found.")
else:
    print(f"The numbers are {result[0]} and {result[1]}.")