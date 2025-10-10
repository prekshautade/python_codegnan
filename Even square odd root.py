#Even-square, odd-root program
lst = [1,2,3,4,5]
res = []
for i in range(len(lst)):
    if lst[i] % 2 == 0:
       res.append(lst[i] ** 2)
    else:
       res.append(lst[i] ** 0.5)
print(res)
