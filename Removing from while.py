#List element removal program
lst = [1, 2, 2, 3, 2, 1]
ele = 2
while ele in lst:
    lst.remove(ele)
print(lst)

    
#Counting with while loop
n = int(input())
i = 1
while i<n:
     print(i)
     i += 1
else:
    print("program done")
    

#Remove all occurrences using while loop
lst = [1,2,2,3,2,1]
ele = 2
n = len(lst)
i = 0
while i < n:
    if lst[i] == ele:
       lst.pop(i)
       n -= 1
    else:
        i += 1
print(lst)        
    
