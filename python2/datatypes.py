"""
sugar = 12
print(f"INITIAL SUGAR VALUE:{sugar}")
print(f"ID SUGAR VALUE:{id(sugar)}")
sugar = 22
print(f"SECONDARY SUGAR VALUE:{sugar}")
print(f"ID OF  SUGAR VALUE:{id(sugar)}")
spice_mix = set()
print(f"The value of spice is:{id(spice_mix)}")
spice_mix.add("ginger")
spice_mix.add("garlic")
spice_mix.add("pepper")
print(f"The value of spice is:{id(spice_mix)}")
print(f"The holding of spice is:{spice_mix}")

#Arithmetic
a = 18
b=26
c= a+b
d=a-b
e=a*b
f=a%b
i=a**b
print(f"The sum is:{d}")
print(f"The sum is:{e}")
print(f"The sum is:{f}")
print(f"The sum is:{i}")

# boolean
is_boiling = 1
is_empty=0
if is_boiling:
    print(f"The Tea is hot")
else:
         print(f"The Tea is empty")

# lOGICAL OPERATOR
if is_boiling and is_empty:
    print(f"OHHH empty")
elif is_boiling or  is_empty:
    print(f"TEA IS THERE")
else:
     printf("bye")
# FLOAT
rupee=360000.00
print(f"The Total salary is{rupee}")

#strings
cus_name = input(f"Enter ur name")
chai_name = input (f"Which is ur favorite chai")
print(f" {cus_name}'s Favourite chai is{chai_name}")
print(f"The flavour of chai is:{chai_name[0:7]}")

secret=chai_name.encode("utf8")
print(f"The secret code is:{secret}")

#TUPLES
masala_spices = ("cardomom","cinnamon","clove","ginger")
'(spice1,spice2,spice3,spice4) = masala_spices
print(f"The total spices are:{spice1},{spice2},{spice3},{spice4}")

a,b=2,1
a,b=b,a
print(a)
print(b)

#List
Ingredients = ["milk","Tea","Water"]
Ingredients.append("sugar")
print(Ingredients)
Ingredients.insert(2,"cardomom")
print(Ingredients)
Res=Ingredients.pop()
print(Res)
strong = ["blacktea"] * 3
print(strong)

#Set andFrozenset

mix ={"apple","mango"}
mix1 = {"grapes","pineapple","apple"}
mix2 = mix - mix1
print(mix2)
"""
chai_order = dict(type="masala",size = "large",sugar = 2)
print(chai_order)
chai_order["base"] = "blacktea"
print(chai_order)
print(f"the keys are:{chai_order.keys()}")
print(f"the values are:{chai_order.values()}")
extra = {"spice": "elachi"}
chai_order.update(extra)
print(chai_order)
