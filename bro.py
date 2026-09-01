import pymem
while True:
    
    p=input("Enter the user name:")
    l=input("Enter the password:")
    pt=("zero")
    lt=("1")
    if(p==pt) and (l==lt):
        pm = pymem.Pymem("HillClimbRacing")
        ad = 0x0035CAD4# GOLD COINS
        ag = 0x0035CAEC# DIMOND
        
        coin = pm.read_int(ad)
        dim =pm.read_int(ag)
        print("------------------------------------------------")
        print("HACKS BY ZERO SUS")
        print("------------------------------------------------")
        print("Current coins:",coin)
        print("Current Dimonds:",dim)
        while True:
            i = int(input("Enter the number for coin:"))
            o = pm.write_int(ad,i)
            print("sucessfully hacked Coin bro!")
            print("------------------------------------------------")
            y = int(input("Enter the number for Dimond:"))
            ip = pm.write_int(ag,y)
            print("sucessfully hacked Dimond bro!")
            print("------------------------------------------------")
    else:
        print("Plz Enter the correct user name and password")
        print("------------------------------------------------")
        
    


    
