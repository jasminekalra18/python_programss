#dictionary
countrynames=['india','pakistan','japan','englan']
capitalnames=['delhi','islamabad','tokeyo','london']
capitalnames[2]


#zip do list to combine kr k show krega
y=list(zip(countrynames,capitalnames))
print(y)


#key value pair
dict1={'india':'delho','paks':'islamba','jaspan':'tokeyo',"engliand":'london'}
print(dict1)

print(dict1['india'])
print(dict1['jaspan'])

dict12={
        "dsa":[20,18],
        "dms":30 ,
        "os": 14 
       }
print(dict12["dsa"])
dict12["os"]=18
print(dict12)
dict12["dsa"][1]=26
print(dict1.keys(),
dict1.values(),
dict1.items())

dict12={
        "dsa":{"mt1":200,"mt2":18},
        "dms":30 ,
        "os": 14 
       }

dict3={}
print(type(dict3))

s1=set()
print(type(s1))

#file handling
fp=open("jas.txt","r")
print(fp.read())
fp.close()
fp=open("jas.txt","r")
str1=fp.read()
fp.close()
fp=open("jas.txt","r")
fp.readline()
fp.readline()
fp.close()
fp=open("jas.txt","r")
fp.readlines()[2]
fp=open("jas.txt","r")
fp.read()
fp.readlines()
fp.readline()
fp.read()

fp=open("new.txt","w")
fp.write("jasmine kalra ")
fp.close()

#append mode
fp=open("new.txt","a")
fp.write("jasmine kalra ")#dir(Fp)
fp.close()

fp=open("new.py","w")
fp.write("\n #this is a single line ")
fp.close()

