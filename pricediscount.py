#def calculate_discount(price= float(input("Enter original price: ")), 
 #                        discount_percent =float(input("Enter discount percentage: "))):
  #  if discount_percent >= 20:
   #  return price - price*discount_percent/100
   #else:
    #   return price
    
#print(f'Final Price: ', calculate_discount())



def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get input from user
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if final_price < price:
    print(f"🎉 Discount applied! Final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price is: ${final_price:.2f}")
