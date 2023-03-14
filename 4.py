n = int(input("Enter the number of coins: "))
coins = input("Enter the coin sequence (H for heads, T for tails): ").split()

# Count the number of coins that need to be flipped to make all coins face the same side
num_flips = min(coins.count("H"), coins.count("T"))

print(f"The minimum number of coins to flip is: {num_flips}")