a =[]
n = int(input("Enter the number of array size :"))
for i in range(n):
    num =int(input("Enter Number :"))
    a.append(num)

def bsort(a):
    size = len(a)
    for i in range (size):
        for j in range (0,size-i-1):
            if a[j] > a[j+1]:
                temp =a[j]
                a[j] =a[j+1]
                a[j+1] =temp
bsort(a)
print("The sorted arry is :", a)
