 # Write a program to calculate the factorial of an integer using recursion.

def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)

n = int(input("ENTER A NUMBER"))
result = fact(n)
print("factorial of ", n , "is", result )
