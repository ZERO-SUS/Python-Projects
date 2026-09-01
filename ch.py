import pymem 
pm = pymem.Pymem("HillClimbRacing.exe")
adress = 0x002CCAD4

coin= pm.read_int(adress)


print("coins:",coin)
while True:

    f=int(input("Enter the value to change tha coin:"))
    pm.write_int(adress,f)
    
