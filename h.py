import pymem 
pm = pymem.Pymem("HillClimbRacing.exe")
adress = 0x28CAD4
coin = pm.read_int(adress)
print("coins:",coin)
