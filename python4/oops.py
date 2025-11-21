"""
class chai:
    name = "tata chakra"
    color = "Red"

ginger_tea = chai()
print(f"The first brand is:{ginger_tea.name}")
print(f"The color is:{ginger_tea.color}")
ginger_tea.name = "Brooke bond"
ginger_tea.color = "Brown"
ginger_tea.cup="small"
print(f"The first brand is:{ginger_tea.name}")
print(f"The color is:{ginger_tea.color}")
print(f"The first brand is:{ginger_tea.cup}")
print(f"The first brand is:{chai.name}")
del ginger_tea.cup
print(f"The first brand is:{ginger_tea.cup}")

class chaicup:
    size = 150
    def describe(self):
        return (f"A {self.size} chai cup")
cup = chaicup()
print(cup.describe())
cup1 = chaicup()
cup1.size=200
print(chaicup.describe(cup))

class chai():
    def chaiorder(self,flav,price,size):
        self.flav = flav
        self.price = price
        self.size = size
    def ordersummary():
        return(f" Ur order is {self.flav} chai and price is{self.price}andthe size is{self.size}")
    
order = chai("ginger",200,"small")
print(order.ordersummary)

class A:
    label = "A:apple class"
class B(A):
    label = "B:Banana class"
class C(A):
    label = "C:cherry class"
class D(C,B):
    pass
cup = D()
print(cup.label)
print(D.__mro__)
"""
class chaiutil:
    def clean_ing(text):
        return[item.strip()for item in text.split(",")]
raw = ["water,sugar,milk"]   
cleaning = chaiutil.clean_ing(raw)
print(cleaning)