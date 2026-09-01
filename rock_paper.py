import random
print("you VS computer Rock paper syser")
win = [(1,3),(2,1),(3,2)]
p = {1:("Rock"),
     2:("Paper"),
     3:("scser")}
while True:
    print("_____________________________________")
    player = int(input("Enter rock-1 or paper-2 or syser-3:"))
    if (player>3)or(player<1):
            print("plz select only 1-3 number")
    while True:
        while True:
                if (player>3)or(player<1):
                    player = int(input("Enter rock-1 or paper-2 or syser-3:"))
                else:
                    break
        player_val=p[player]
        computer = random.randint(1,3)
        computer_val = p[computer]
        result = (player,computer)
        if (result == win[0]) or (result == win[1]) or (result == win[2]):
            print(f"Your choise is:{player_val}")
            print(f"Computer choise is :{computer_val}")
            print("you won!!!")
            break
                        
        else:
            print(f"Your choise is:{player_val}")
            print(f"Computer choise is :{computer_val}")
            print("You loose!!")
            break
                            
                        
                        
                         

        

                    
                
        
    
