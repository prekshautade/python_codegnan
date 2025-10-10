#which is big
a = int(input())
b = int(input())
if a>=b:
    print(" a is bigger")
else:
    print(" b is bigger")

#greater than
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

#positive even and odd negative even and odd
num = int(input("Enter a number: "))
if num == 0:
    print("zero")
elif num > 0 and num % 2 == 0:
    print("positive even")
elif num > 0 and num % 2 == 1:
    print("positive odd")
elif num < 0 and num % 2 == 0:
    print("negative even")
else:
    print("negative odd")


    
#list is prenst or not or List membership check program
num = int(input("Enter a number: "))
a = [1,2,3,4,5,6,7,8,9]
if num in a:
    print("It is present")
else:
    print("It is not present")


##electricity bill calculator
##units consumed given:
##first 100 units - $1.5 per unit
##next 200 units - $2.5 per unit
##above 300 units - $4 per unit
##calculate total bill.
first = 1.5
next = 2.5
above = 4
first*next*above
calculate = first*100 + next*200 + above*300
print("total bill is :",calculate)

          
