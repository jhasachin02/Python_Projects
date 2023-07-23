#Write a python program to sum the sequence given below. Take the input n from the user.1+1/1!+1/2!+1/3!+⋯+1/n!

n = int(input("ENTER A NUMBER YOU WANT TO ADD :"))
sum = 1
for a in range (1,n+1):
    f=1
    for  b in range (1,a+1):
        f*f*b
        sum = sum +(1/f)
print (sum)     

