def coutcharacters():
    vowles = "aeiouAEIOU"
    v = c =u = l =0
    with open("text.txt", "r") as file:
        text = file.read()
        for char in text:
            if char.isalpha():
                if char  in vowles:
                    v += 1
                else:
                    c+=1
                if char.isupper():
                    u+=1
                else:
                    l+=1
            
    print("Vowles : ",v)
    print("Consonents: ", c)
    print("Uppercase :", u)
    print("Lowercase :", l)

user = input("Enter the sentence :")
with open("text.txt","w") as f:
    f.write(user)
coutcharacters()