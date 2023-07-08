Grocery = { 
"Cornflakes" : {"quantity" : 15 , "price" : 100} 
, "Muesli" : {"quantity" : 14 , "price" : 150}
, "Oats" : {"quantity":10, "price" : 80}
,"Wheat Flakes" : {"quantity" : 5, "price" : 75}
,"Granola" : {"quantity" : 8, "price" : 125
}}
Grocery['Cornflakes']["quantity"]+=2
Grocery["Oats"]["price"]+=10
Grocery["wheat flour"]={"quantity":6,"price":50}

for item,details in Grocery.items():
    quantity=details["quantity"]
    price=details["price"]
    print(f"{item}:quantity-{quantity}kg , price -{price:.2f}rupees")
