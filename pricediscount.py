def calculate_discount(price= float(input("Enter original price: ")), 
                         discount_percent =float(input("Enter discount percentage: "))):
    if discount_percent >= 20:
     return price - price*discount_percent/100
    else:
       return price
    
print(f'Final Price: ', calculate_discount())

