basket = []
price = []
print("****** welcome to ishop calcolator *******")
try:
  number_items = int(input("Enter the number of items in your basket: \n"))
except ValueError:
  print("Invalid number entered. Please enter a valid whole number.")
  number_items = 0
for i in range(number_items):
  item = input("Enter the name of the item: \n")
  if item :
     basket.append(item)
  else :
    print("You have not entered any item")
  try:
    price_item = float(input("Enter the price of the item: \n"))
    price.append(price_item)
  except ValueError:
    print("Invalid price entered. Please enter a valid number.")
confirm_basket = input("Do you want to see your basket? (yes/no): \n")
if confirm_basket == "yes" :
   print(f"\nYour basket: {basket}")
confirm_price = input("Do you want to see the price of your items? (yes/no): \n")
if confirm_price == "yes" :
  print("\nThe price of your items: ", (sum(price)))
     