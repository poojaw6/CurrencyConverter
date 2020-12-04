#Currency Converter
with open("currency.txt") as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    #3rd column is redundant comun - inverse of 1INR so we will ignore it
    parsed = line.split("\t")
    # print(parsed)
    # break
    currencyDict[parsed[0]] = parsed[1]

# print(currencyDict)

amount = int(input("Enter amount in INR:\n"))

print("Enter the name of currency you want to convert this amount to: \nAvailable Options: \n")
[print(item) for item in currencyDict.keys()]

currency = input("Please enter one the currency values:\n")
print(f"{amount} Indian Rupees is equal to {amount*float(currencyDict[currency])} {currency}")
