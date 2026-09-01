menu = {
    "pizza" :87,
    "chips" :20,
    "soda" :40,
    "burger" :150,
    "red bull":125,
    "monster white" :250
    }
cart=[]
total=int()
p=0
for key,value in menu.items():
    print(f"{key:20}: ${value}")
while True:
    ask = input("Enter the food to purchase(q to quit):")
    if (ask=="q")or(ask=="Q"):
        break
    elif(menu.get(ask)is not None):
        cart.append(ask)
    else:
        print("Plz enter the valid only")
print("----------Your Cart--------")
for ask in cart:
    total+=menu.get(ask)
    p+=(ask.count("pizza"))
    print(ask)
print(f"Your total: ${total}")
print("have a nice day")
print(p)
    






        
