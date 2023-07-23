# to find a prime no

a=int(input("enter a number"))
lim = int(a/2)+1
for i in range(2,a):
    rem = a%i
    if rem==0:
        print(a, "is not a prime number" )
        break
else:
    print(a, "is  a prime number")


            
    
