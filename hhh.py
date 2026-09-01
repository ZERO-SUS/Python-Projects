def domian(d):
    if(d[-1]=="m" and d[-2]=="o" and d[-3]=="c" and d[-4]=='.' and d[-5]=="l" and d[-6]=="i" and d[-7]=="a" and d[-8]=="m" and d[-9]=="g" and d[-10]=='@'):
        print("It is google mail domain")
    elif(d[-1]=="m" and d[-2]=="o"and d[-3]=="c"and d[-4]=='.'and d[-5]=="l"and d[-6]=="i"and d[-7]=="a"and d[-8]=="m"and d[-9]=="e"and d[-10]=='@'):
        print("It is just e-mail domain")
while True:
    n=input("Enter the email address:")
    domian(n)
