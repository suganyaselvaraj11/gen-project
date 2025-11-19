"""def serve_chai():
    yield "cup1:Masalachai"
    yield "cup2:Elachichai"
    yield "cup3:Greenchai"

stall = serve_chai()

for cup in stall:
     print(cup)
     

def coffee():
    yield "my name is brew"
    yield "my name is bru"
    yield "my name is sunrise"
cup = coffee()

for straw in cup:
   print(straw)
   
def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count+=1
ref = infinite_chai()

for _ in range(9):
    print(next(ref))
    """
def local_chai():
    yield "Masala chai"
    yield "Ginger chai"
def imported_chai():
    yield "Matcha"
    yield "Oolang"
def full_menu():
    yield from local_chai()
    yield from imported_chai()
for chai in full_menu():
    print(chai)
def chai():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed,no more chai")
stall = chai()
print(next(stall))
stall.close()
