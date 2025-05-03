# Coin Interpreter Program - Sprint 2

# Define the coin values
coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

# Get user input
input_str = input("Enter a sentence with coins (For Example:'1 penny and 2 nickels'): ")

# Convert the input to lowercase and split it by 'and'
coin_phrases = input_str.lower().split(" and ")

total = 0.0

for phrase in coin_phrases:
    parts = phrase.strip().split()
    
    # Expecting two parts: number and coin
    if len(parts) != 2:
        print(f"Invalid format for phrase: '{phrase}'")
        continue

    quantity = int(parts[0])
    coin = parts[1]

    # Fix plural to singular form
    if coin == "pennies":
        coin = "penny"
    elif coin.endswith("s"):
        coin = coin[:-1]

    # Calculate value
    if coin in coin_values:
        value = quantity * coin_values[coin]
        total += value
    else:
        print(f"Unknown coin type: '{coin}'")

# Print the final dollar amount
print("Total in dollars: $", round(total, 2))
