
"""
Name = ["Amal","Siddhu","Kousik","Pranav"]
for x,item in enumerate(Name,start=1):
    print(f"{x}:{item}Sharma")
    

Fruits = ["Apple","Orange","Strawberry","Mango"]
Cost = [100,250,450,320]
for x,y in zip(Fruits,Cost):
    print(f"{x} Cost: {y} Rupees")


Temperature = 40
while (Temperature>=40):
    print(f"The current Temp is {Temperature}")
    Temperature = Temperature + 15
   
    if Temperature == 55:
        continue
    elif Temperature ==100:
        print("Tea is ready to boil")
        break

Fruits = ["Apple","Orange","out of stock","Strawberry","Mango","exit"]
for x in Fruits:
   
     if x == "out of stock":
        print("its sold out")
        continue
     elif x == "exit":
        print("Tat's over")
        
value = 28
if(remainder:=value%5):
    print(f"The Remainder is {remainder}")
    """
veg = ["tomato","onion","cabbage"]
while(x:=input("Enter the veg u want")) not in veg:
       print (f"The {x} is not available")