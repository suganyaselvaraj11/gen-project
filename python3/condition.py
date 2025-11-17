"""
kettle_boil = True
sugar = input("enter yes if u hav sugar")
if (kettle_boil and sugar == "yes"):
    print("Pour water")
else :
    print("its not hot")


cup = input("enter the cup size: ")

if cup == "small":
    print("price is Rs.10")
elif cup == "medium":
    print("price is Rs.20")
elif cup == "big":
    print("price is Rs.50")
else:
    print("no size")
    
order_amt = int(input("enter the amount"))
if (order_amt >=50 and order_amt<=300):
    print("No delivery fee")
else:
    print("50+ extra")
    """
seat_alloc = input("enter the seat u want(sleeper/1ac/2ac/3ac):")

match seat_alloc:
    case "sleeper":
        print("Fare is Rs.100")
    case "1ac":
        print("Fare is Rs.1000")
    case "2ac":
        print("Fare is Rs.500")
    case "3ac":
        print("Fare is Rs.300")
    case "_":
        print("Invalid seat")