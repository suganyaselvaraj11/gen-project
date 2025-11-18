"""
def take_order(name,flavour):
    print(f"Mr.{name} wants the {flavour} chai")


take_order("Hitesh","Ginger")
take_order("Amal","Cardamom")


def fetch_sales():
    print(f"Fetching valid sales data")

def filter_valid_sales():
    print(f"Filtering valid sales Data")

def summarize_data():
    print(f"summarize sales")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")
generate_report()


def calculate_bill(cup,price_per_cup):
    return cup* price_per_cup
my_bill = calculate_bill(5,10)
print(my_bill)

def add_vat(price,vat_rate):
    return price * (100+vat_rate)/100
orders = [100,150,200]

for price in orders:
    final_amount = add_vat(price,10)
    print(f"original:{price},Final with VAT:{final_amount}")
    
def addition(m1,m2):
    return m1+m2
def subraction(m1,m2):
    return m1-m2
def multiply(m1,m2):
    return m1*m2
def divide(m1,m2):
    return m1/m2

def calculate():
    
    total1= addition(2,4)
    total2= subraction(2,4)
    total3= multiply(25,10)
    total4=divide(9,3)
    print(total1)
    print(total2)
    print(total3)
    print(total4)
calculate()

#scope
def chai_counter():
     chai_order = "Lemon"  
     def print_order():
      chai_order = "Ginger"
      print("Inside:",chai_order)
      print_order()
      print("outer",chai_order)
chai_counter()
chai_order = "Tulsi"
print("Global:",chai_order)

chai = input("Enter ur faav flavour")
def making(order):
    print(f"I am Making:{order} Tea")

making(chai)

#args,kwargs
def make_salad(*fruit,**extras):
    print("fruits are:",fruit)
    print("Toppings are:",extras)

make_salad("apple","strawberry",topping="chocochip",sweet="honey")

def maketea(order=[]):
    order.append("Masala")
    print(order)
maketea()


def getorder():
  print("here is ur order")
mylikes = getorder()
print(mylikes)

def makechai(cup_left):
    if cup_left == 0:
        return("chai is over")
    return("yes,still it is there")
res = makechai(5)
print(res)

#mulitple vaalues
def makecoffee():
    return 50,30,2
chicory,coffee,sugar = makecoffee()
print(chicory)
print(coffee)
print(sugar)

#lamda
chai_types = ["ginger","elachi","cinnamaon","ginger","clove"]
strong = list(filter(lambda x:x != "ginger",chai_types))
print(strong)
"""
def veg(order="brinjal"):
    """ This is a vegetable"""
    print("PURPLE COLOR VEG")
print(veg.__doc__)
print(veg.__name__)