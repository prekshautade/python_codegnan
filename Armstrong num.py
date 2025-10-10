##armstrong number
n = int(input())
temp1 = temp2 = n
length = 0
while 0 < temp1:
    rem = temp1 % 10
    length += 1
    temp1 //= 10
res = 0
while 0 < temp2:
    rem = temp2 % 10
    res = res +rem** length
    temp2//=10
if res == n:
    print(f"{n} is a armstrong number")
else:
    print(f"{n} is a not armstrong number")


#Armstrong number program”
n = 153
res = 0
num = n
length = len(str(n))
while n > 0:
    rem = n % 10
    res += rem ** length
    n //= 10
print(res)
