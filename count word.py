#Write a program to count number of words in a file

file = open("sachin.txt","r")
count = 0
for line in file :
    word = line.split(" ")
    count+= len(word)
file.close( )
print("NUMBER OF WORDS IN A TEXT FILE :,",count)
