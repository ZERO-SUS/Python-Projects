def check():
    w=l=c=0
    with open("5.txt", "r") as file:
        for line in file:
            l+=1
            w += len(line.split())
            c += len(line)
    print("lines : ", l)
    print("words : ", w)
    print("characters : ", c)

user =input("Enter the Sentence :")
with open("5.txt", "w") as file:
    file.write(user)
check()
