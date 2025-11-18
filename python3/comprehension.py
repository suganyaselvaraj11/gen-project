#List comprehension

menu = ["plain dosa","masaladosa","onion dosa","Butter dosa"]

serving = [order for order in menu if "masala" in order]
print(serving)

#set comprehension

menu = ["plain dosa","masaladosa","onion dosa","Butter dosa","masaladosa","plain dosa"]

serving = {order for order in menu }
print(serving)

menu = {
        "masala chai":["ginger","elachi","cinnamon"],
        "Tulsi chai":["tul","elachi"],
        "Green chai":["leaf","lemon"],
        }

serving = {spices for order in menu.values() for spices in order}
print(serving)


menu = {
        "masala chai":50,
        "Tulsi chai":70,
        "Green chai":100,
        }

serving = {tea:price/10 for tea,price in menu.items() }
print(serving)