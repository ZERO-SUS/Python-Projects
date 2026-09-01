import pickle
f = open("7.dat", "wb")
o = open("7-90%.dat", "wb")
n =int(input("Enter the Number of students: "))
for i in range(n):
    name = input("Enter the name of the student: ")
    mat =int (input("Maths Marks :"))
    chem =int (input("Chemistry Marks :"))
    phy =int (input("Physics Marks :"))
    eng =int (input("English Marks :"))
    kan =int (input("Kannada Marks :"))
    cs=int (input("Computer Science Marks :"))
    total = mat + chem + phy + eng + kan + cs
    per = (total/600) * 100
    text =[name, mat, chem, phy, eng, kan, cs,]
    pickle.dump(text,f)
    if per>=90:
        pickle.dump(text,o)
f.close()
o.close()
file = open("7.dat", "rb")
for i in range(n):
    p =pickle.load(file)
    print(p)
file.close()
top =open("7-90%.dat","rb")
print("Students with 90% and above marks:")
while True:
    try:
        pp =pickle.load(top)
        print(pp)
    except:
        pass
top.close()