import pickle
while True:
    f = open("6.dat","wb")
    n = int(input("Enter the number of students :"))
    for i in range(n):
        name = input("Enter Name of Student :")
        ma = int(input("Maths Marks :"))
        phy = int(input("Physics Marks :"))
        chem = int(input("Chemistry Marks :"))
        cs = int(input("Computer Marks :"))
        eng = int(input("English Marks :"))
        kan = int(input("Kannada Marks :"))
        text =[name,ma,phy,chem,cs,eng,kan]
        pickle.dump(text,f)
    f.close()
    file =open("6.dat","rb")
    while True:
        try:
            p=pickle.load(file)
            print(p)
        except:
            pass
    file.close()
