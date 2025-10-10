##armstrong number
##an armstrong numbers is number that is equal to sum off its own digits each raised to the
##power off the number of digits
aremstrong_list = []
for n in range(1,100):
    length = len(str(n))
    temp2 = n
    res = 0
    while 0 < temp2:
        rem = temp2 % 10
        res = res + rem ** length
        temp2 //=10
    if res == n :
        armstrong_list.append(n)
print(armstrong_list)
