
#example
t = (1,2,3, [10,20,30], "codegnan")
print(t)

#t[0]=100 - type error

#index based and sliceable
t=(1,2,3,[10,20,30],"codegnan")
print(t[2],t[-2],t[-4])

#read tuple of intergers from user
t=tuple(map(int,input().split()))
print(t)   

#index based and sliceable
t =(1,2,3,[10,20,30],"codegnan")
print(t[2],t[-2],t[-4])
print(t[-1:2:-1])
print(t[3:-4:-1])

#single element representation in tuple
t = (29)
t2 = (20)
print(type(t))
print(type(t2))

#tuple operations
#concatination operations
t1 = (1,2,3)
t2 = ('A','B')
t3 = (t1 + t2)
print(t3)

#tuple operations
#repetation operations
t1 =(1,2,3)
t=(t1*3)
print(t)


##tuple methods
##index(ele)-it returns index of element otherwise valueError
##count(ele)-it return
t=(1,2,3,[10,20,30],"codegnan")
ind=t.index(3)
count=t.count(3)
print(ind,count)

#built in functions
##len(),min(),max(),sum()
t=(1,2,3,4,5)
print(len(t),min(t),max(t),sum(t))

#string to tuple conversion
s = "codegnan"
print(list(s))
print(tuple(s))
      
#tuple to list conversion
t = (1,2,3,4,5)
print(list(t))
      
