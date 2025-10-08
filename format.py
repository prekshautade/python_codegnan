###old style output formatting - uning comma
##name = "ravi"
##age = 20
##print("name is",name,"and age is",age) 
##
###modulo operator formating
###access specifiers
###%d - intergers
###%f - float
###%s - string
##name = "ravi"
##age = 20
##print("Name is %s and age is %d"%(name,age))
##
###dor format
##name = "ravi"
##age = 20
##print("Name is {} and age is {}".format(name,age))
##print("Name is {} and age is {}".format(age,name))
##
##name = "hello"
##age = 40
##salary = 20000.0
##print("Name is {} and age is {} and salary is {}".format(name,age,salary))
##
###f - format
### dor format
##name = "ravi"
##age = 20
##percentage = 95.6926
##print(f"Name is {name} and age is {age} and i have {percentage}")
##print(f"Name is {name} and age is {age} and i have {percentage:.2f}")
##num = 1
##print(f"{num:0{5}d}")
##print(f"{num:4{5}d}")
##
###eval() funtion - it evaluates the string represented expressions
##res = eval('52+3')
##print(res)
##print('52+3')
##print(eval('53+3'))
##
###eval
##num = eval(input())
##print(type(num),num)

s = input().strip().split()
print(s)
l = list(map(int,s))
print(l)

