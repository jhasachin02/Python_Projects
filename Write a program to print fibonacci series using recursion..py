 # Write a program to print fibonacci series using recursion.

def  fib (n1 ,n2,n):
    if n==0:
        return
    res=n1+n2
    print(res)
    fib(n2,res,n-1)


a = 0
b = 1
n = int(input("ENTER THE NUMBER TO BE PRINTED"))
print(a)
print(b)
fib(a,b,n-2)
