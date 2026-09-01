
while True:
    space=0
    reg_u = input("Ener the New User Name ( no space):")
    for i in reg_u:
        if i ==" ":
            space+=1
    if space == 0:
        break
                
    elif space>0:
        print("Plz Enter the New User me with out space!")
