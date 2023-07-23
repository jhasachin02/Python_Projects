import pickle
fo=open("binary record", "wb")
dic={}                             #write data in binary file
n=int (input ("enter no. of students"))
for k in range (n) :
    rollNo = int(input ("enter roll no"))
    name=input("enter name")
    mark=int (input("enter marks"))
    dic[rollNo]={}
    dic[rollNo] ["Name"]=name
    dic[rollNo] ["Marks"]=mark
pickle.dump (dic, fo)
fo.close()
# read data from a binary file
fo=open("binary record", "rb+")
d=pickle.load (fo)
rollNo=int (input ("enter roll no. to update marks"))
for k in d:
    if k==rollNo:
        m=int (input ("enter the marks"))
        d[k]["Marks"]=m
        print (d)
    if (rollNo not in d):
        print ("roll no does not exist.")
        break
pickel.dump(d,fo)
fo.close()
