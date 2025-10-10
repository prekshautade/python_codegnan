#interger to string,float,boolean,conversion
num = int(input())
print(num)
val=float(num)
print(val)
print(bool(num))
print("string type number:",str(num))

#reading dict from user
n=int(input())
d={}
for i in range(3):
    key,value = map(int,input().split())
    d[key] = value
print(d)
