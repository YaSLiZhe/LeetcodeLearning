first, *rest = [1, 2, 3, 4]
print(first, rest) # 1 [2, 3, 4]
print(*rest) # 2 3 4
a = "l", "m"
print(*a)

# *args: arguments
# We dont know how many toppings(arguments) we have
# **kwargs: keyword arguments
# *toppings handle these arguments: "pepperoni", "olives" and put them into a tuple
# **details will take these keyword arguments delivery=True, tip=5 and place them into a dictionary as key value pairs
def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    # print(toppings)
    print("\nDetails of the order are:")
    for key, value in details.items():
        print(f"- {key}: {value}")

order_pizza("small", "pepperoni", "olives", delivery=True, tip=5)