x = {"bro" : "gg",
     "lol" : "tt",
     "yo" : "CHICKEN"}
count=0
for key , value in x.items():
    print(f"{key:10}   -  {value}")
    count+=1
print(f"the total names = {count}")
