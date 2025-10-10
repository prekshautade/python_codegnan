#print 0
n = int(input())
if n == 0:
   print("number is zero")
print("program done")

#eligible to vote
age = int(input())
if age>=18:
    print("eligible to vote")
else:
    print("not eligible")
    
#if-else remaining and balance amount
stock = 5
price = 10
req_count = 3
amount = 10
total_amount = price*req_count
if req_count<=stock and total_amount <= amount:
    print("remaining amount:",amount - total_amount)
else:
    print("balance money:",total_amount - amount)
    
#odd and even
number = int(input())
if number%2==0:
    print("even")
else:
    print("odd")
    
#positive and negative
number = int(input())
if number>=0:
    print("positive")
else:
    print("negative")
    
