board = ["1","2","3","4","5","6","7","8","9"]
player = "X"

while True:
    print()
    print(board[0], "|", board[1],"|",board[2])
    print("--+---+--")
    print(board[3], "|", board[4],"|",board[5])
    print("--+---+--")
    print(board[6], "|", board[7],"|",board[8])

    pos = int(input(f"Player{player}, choose 1-9:")) - 1

    if board[pos] in ["X","0"]:
        print("Already taken")
        continue
    board[pos] = player

    wins= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    won= False
    for a,b,c in wins:
        if board[a] == board[b] == board[c]:
            print(f"Player {player} wins")
            won = True
            break
        if won:
            break
        if all(x in ["X", "0"] for x in board):
            print("Draw")
            break
        player = "o"
        
        if (player == "X"):
            player = "0"
        else:
            player ="0"
        


































































"""import random
while True:
    print("This game is number gussing game have funn!!!!!")
    print("For the levels type | Easy-1 | meadium-2 | Hard-3")
    y=int(input("Enter the level number:"))
    if (y==1):
        o=(int(random.uniform(1,50)))
        while True:
            u = int(input("Enter your gussing number( between 1- 50 only!!:"))
            print("-----------------------------------------------------------")
            if(o>u):
                print("your number is lesser than prize number")
            if(o==u):
                print("conguralation!! you number is right",o)
                print("YOU HAVE WON")
                break
            elif(o<u):
                print("your number is greater than prize number")
                print("=========================================================")
    if (y==2):
        o2=(int(random.uniform(1,100)))
        while True:
            u2 = int(input("Enter your gussing number( between 1- 100 only!!:"))
            print("*****************************************")
            if(o2>u2):
                print("your number is lesser than prize number")
            if(o2==u2):
                print("conguralation!! you number is right",o2)
                print("YOU HAVE WON")
                break
            elif(o2<u2):
                print("your number is greater than prize number")
                print("________________________________________________________")
    if (y==3):
        o3=(int(random.uniform(1,1000)))
        while True:
            u3 = int(input("Enter your gussing number( between 1- 1000 only!!:"))
            print("________________________________________________________")
            if(o3>u3):
                print("your number is lesser than prize number")
            if(o3==u3):
                print("conguralation!! you number is right",o3)
                print("YOU HAVE WON")
                break
            elif(o3<u3):
                print("your number is greater than prize number")
                print("________________________________________________________")"""

