list1=[1,2,3,4,5]
#tuple
t=(1,2,3,4,5)
print(type(t))
"""t[0]=10""" #immutable and read only
print(t)
print(len(t))

tt=(10,20,13)
print(tt.index(20))

ttt = (1,20,3,20,20)
print(ttt.count(20))
print(ttt.count(1))

tttt = (2)
tttt1=(2,)
print(type(tttt))
print(type(tttt1))

t=(20.4,40, True)

print(divmod(23,5))

x,y= divmod(23,5) #unpacking
p,q,s =tt
print(p,q,s)

list2=[]
for x in list1:
    print(x**2)
    list2.append(x**2)


#list comprehension
print([x**2 for x in list1])

print([x+1 for x in list1])



def f1(x):
    return(x**2)

"""
f1(list1[0])
f1(list1(1))
map funtion
syntax:
list(map(f1,list1))
if u already have list of values
 nd you wnt to do the exacr same 
 operation on each of the element int """
list1=["ram","shym","sita"]

def f2(str1):
     return len(str1)
print(list(map(f2,list1)))

list1=[1,2,3,4,5]
def f3(x):
    return x**3
list(map(f3,list1))



#filter
list1=(1,20,3,10,4,12)
def f4(x):
    if x>10:
        return False#sirf true false return krwane wae function me hi yeh kam krta h

    else:
        return True
print(f4(6))

print(list(filter(f4,list1)))


"""
#lambda = function define hi ni krna bs 
print(list(filter(lambda x: x>10,list1)))

list1=["ram","shym"]
list(map(lambda str1: len(str1),list1))
[len(item for item in list1)]
"""
list1=[1,2,3,4,5,6,7,8,9]
def f5(x,y):
    return x+y

#reduce 
import functools
functools.reduce(f5,l)
