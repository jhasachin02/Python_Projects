#Write a recursive pyhton program to test if a string is palindrome or not.

def check(st):
    rev = st[:: -1]
    print("string : ",st)
    print("Reverse : ",rev)
    if(st==rev):
        return True
    else:
        return False

x = input("ENTER A STRING : ")
if check(x):
    print("IT IS A PALINDROME")
else:
    print("IT IS NOT A PALINDROME")
