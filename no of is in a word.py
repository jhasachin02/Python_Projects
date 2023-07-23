#Write a program to count the number of times the occurrence of 'is' word in a text file


file = open("sachin.txt","r")
count = 0
data=file.read()
word = data.split( )
for i in word :
    if i== 'is':
        count =+1
print(" TOTAL WORDS  'is':",count)
file.close()


