import pymem
pm = pymem.Pymem("HillClimbRacing.exe")
coin = 0x006BCAD4
dim = 0x006BCAEC
print("Current coins:",pm.read_int(coin))
print("Current dimond:",pm.read_int(dim))
while True:
    us = int(input("Enter the Coin to hack"))
    pm.write_int(coin,us)
    u = int(input("Enter the dimond to hack"))
    pm.write_int(dim,u)
    

