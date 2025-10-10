#reverse number
n = int(input())
res = 0
while 0 < n:
    rem = n % 10
    res = res*10+rem
    n//=10
print(res)


##Reverse of number
n = 456
res = 0
while n > 0:
 rem = n % 10
 n = n // 10
 res = res * 10 + rem
print(res)
