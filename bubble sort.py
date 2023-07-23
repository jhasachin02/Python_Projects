#Write a program for bubble sort.

list1 =[]
num = int(input("HOW MANY NUMBER YOU WANT TO ENTER:"))
print("ENTER VALUES :")
for k in range(num):
    list1.append(int(input()))

print("UNSHORTED LIST :" ,list1)

for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]

print("SHORT LIST :",list1)            
