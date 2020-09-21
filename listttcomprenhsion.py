l1=[1,2,3,4]
res=[]#comprehension means chota krdena
for i in l1:#loop
    res.append(i**3) #expression or logical part i
print(res)
"""
we can write above code as 
res=[i**] for i in l1]
l2=[2,3,,5]

lembda function :
when you need to implement east fuctionality
easy code 
it is used to create anonymous fun, funs without name 
lambda fn are used with map ,filter,reduce
used to create small, one time ,and anyonymous fb object in python
syntax:
lambda agruements: expression
general fun bnane k liye def use krte h
lembda is used when developer forgets to make fun ..thn instantly fun is make
lambda agrument colon expression """

list1=[1,2,3]
ress=[x**2 for x in list1]#list comprehensio
print(ress)
  

def cube (x):
    return x*x*x
result=cube(5)
print(result)
a=lambda y :y**3
print(a(5))

def sq(x):
    return x*x
result= sq(5)
print(result)
 #usinf lmbda fn
sq=lambda x:x**2
print(type(sq))
print(sq(5))
#filter
"""filter function in python takes in a fun and a list of agruements
this offeers in elegent way to filter out all the elements of a sequence for which the function returntrue
syntax :
filter (fn,sequence)
create a list of no. divisible by 2 or 4 using list compre"""
