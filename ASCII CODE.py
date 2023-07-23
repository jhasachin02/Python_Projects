 # Write a program to display ASCII code of a character and vice versa.

n =int(input("Enter a number"))
for i in range(n):
    print(( chr (85+i)+ ' ')*(i + 1))
