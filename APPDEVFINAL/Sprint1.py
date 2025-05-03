# Coin Interpreter Program - Sprint 1

# Define the coin values
coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

# Get user input
input_str = input("Enter a sentence with coins (For Example: '1 penny and 2 nickels'): ")

# Split the sentence by 'and'
coin_phrases = input_str.lower().split(" and ")

total = 0.0

for phrase in coin_phrases:
    parts = phrase.strip().split()
    
    if len(parts) != 2:
        print(f"Invalid format for phrase: '{phrase}'")
        continue

    quantity = int(parts[0])
    coin = parts[1]

    # Purposefully added Bug: This only strips 's' from the end, not handling "pennies"f
    if coin.endswith("s"):
        coin = coin[:-1]

    if coin in coin_values:
        value = quantity * coin_values[coin]
        total += value
    else:
        print(f"Unknown coin type: '{coin}'")

# Print the final dollar amount
print("Total in dollars: $", round(total, 2))
