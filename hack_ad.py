import pymem
pm = pymem.Pymem("HillClimbRacing")
coin_ad = 0x0037CAD4
dim_ad = 0x0037CAEC
def hack(ad):
    coin = pm.read_int(ad)
    print(coin)
    while True:
        o = int(input("Enter the num for hack:"))
        p = pm.write_int(ad,o)
        print("Sucessfully hacked!")
        break
while True:
    hack(coin_ad)
    hack(dim_ad)
