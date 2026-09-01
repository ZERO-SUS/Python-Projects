def coutcharacter():
    with open("data.txt", "r") as file:
        text=file.read()
    vowles ="aeiouAEIOU"
    v=c=u=l=0
    for letter in text:
        if letter.isalpha():
            if letter in vowles:
                v+=1
            else:
                c+=1
            if letter.isupper():
                u+=1
            else:
                l+=1
    print("Vowles :", v)
    print("Consonent :",c)
    print("uppercase :" ,u )
    print("Lowercase :",l)
user =input("Enter the sentence:")
with open("data.txt", "w") as file:
    file.write(user)
coutcharacter()
