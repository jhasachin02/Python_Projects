# Write a program to find sum of all elements of a list using recursion

def listsum(x):
    if len(x)== 0:
        return 0
    else:
        return x[0]+listsum(x[1: :])

	
a=eval(input("ENTER THE LIST ELEMENTS "))
sum =listsum(a)
print("SUM OF LIST ELEMENTS =",sum)
