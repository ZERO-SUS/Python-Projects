def si(p,t,r):
    return (p*t*r/100)
def ci(p,t,r):
    return p*((1+r/100)**t)-p
p = float(input("Enter the principle Ammout:"))
t = float(input("Enter the Time :"))
r = float(input("Enter the Rate of Intrest:"))
print(f" The Simple Intrest is : { si(p,t,r)}")
print(f" The Compound Intrest is : { ci(p,t,r)}")
print(f" The difference is : {ci(p,t,r)-si(p,t,r)}")

