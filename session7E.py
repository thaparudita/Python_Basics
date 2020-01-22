menu = {
    "roti = 20",
    "paneer = 200",
    "dal = 100",
    "salad = 10",
}

cart = []
print(cart, type(cart), len(cart))

choice = "yes"

while choice == "yes":

    foodItem = input("enter a food item : ")
    cart.append(foodItem)
    choice = input("would like to add more items (yes/no) : ")

print(cart)
totalPrice = 0
for item in cart:
    totalPrice = totalPrice + menu[item]
    if amount > 200 and promoCode == "Zomato":
        amount = amount - (0.4 * amount)
        print(">> Promo Code Zomato Applied Successfully. 40% OFF. Please Pay: \u20b9", amount)

    elif amount > 100 and promoCode == "JUMBO":

        discount = 0.5 * amount
        # Nested if/else
        if discount > 150:
            amount -= 150
        else:
            amount -= discount

        print(">> Promo Code JUMBO Applied Successfully. 50% OFF. Please Pay: \u20b9", amount)

    else:
        print(">> No Promo Code Found and no Discount Available")
        print(">> Please Pay: \u20b9", amount)

print("total price :", totalPrice)
promoCode = input("enter a promocode : ")

cart.extend(["salad", "noodles"])

print("surprises in cart", cart)

cart.insert(1, "soya champ")

cart.pop(2)
print(cart)

