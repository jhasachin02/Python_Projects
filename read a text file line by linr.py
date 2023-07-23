# Write a program to read a text file line by line and display each word separated by '#'.

file = open("sachin.txt","r")
content = file.readlines()
for line in content:
    words = line.split()
    for word in words:
        print(word+" ", end='')
    print("")
