# Write a program to check a number whether it is palindrome or not.

number = int(input("enter a number"))
temp = number
reverse = 0

while( number>0):
      dig = number%10
      reverse = reverse*10 + dig
      number = number //10

if temp== reverse:
    print ( "number is a palindrome" )
else :
    print ( "number is not a palindrome")
