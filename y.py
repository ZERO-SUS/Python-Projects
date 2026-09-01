import pymem
pm = pymem.Pymem("HillClimbRacing.exe")
ad = 0x011DCAD4
coin = pm.read_int(ad)
print(coin)

while True:
    o=int(input("Enter the number :"))
    p = pm.write_int(ad,o)
    print(coin)
