# **CURRENCIES** **EXCHANGE**

# Currencies and their Exchange Rate
currencies = ["USD", "PKR", "EUR", "GBP", "INR"]
rates = [2.0, 340.0, 0.95, 0.84, 83.0 ]

# Show Rates
def view_rates():
  print("Exchange Rates: ")
  for i in range (len(currencies)):
    print (currencies[i], "=", rates[i])

# Conversion of Currencies
def convert_currency():
    print("Available Currencies:")
    for i in currencies:
        print("-", i)

    from_currency = input("Convert from currency: ")
    to_currency = input("Convert to currency: ")

    if from_currency not in currencies:
        print(f"Currency {from_currency} is not available!")

    if to_currency not in currencies:
        print(f"Currency {to_currency} is not available!")


    amount = float(input(f"Enter amount in {from_currency}: "))

    from_index = currencies.index(from_currency)
    to_index = currencies.index(to_currency)

    amount_in_usd = amount / rates[from_index]
    print(f"{amount} {from_currency} = {amount_in_usd:} USD")

    converted_amount = amount_in_usd * rates[to_index]
    print(f"{amount_in_usd:} USD = {converted_amount:} {to_currency}")

while True:
    print("===== Currency Exchange System =====")
    print("1. View Exchange Rates")
    print("2. Convert Currency")
    print("3. Exit")

    user_input = input("Enter your choice: ")

    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number!")
        continue

    if user_input == 1:
        view_rates()
    elif user_input == 2:
        convert_currency()
    elif user_input == 3:
        print("Good Bye!")
        break
    else:
        print("Please enter the correct number")