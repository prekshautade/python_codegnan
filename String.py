#empty string representation
s1 = ""
s2 = str() #string function
#type() -this function returns the date type
print(type(s1))
print(type(s2))

#string operations
#concantenation by using '+' operator
s1 = "code"
s2 = "gnan"
print(s1 + s2)
print(s1+" "+ s2)

#string repetation using '*' operator
s1 = "code"
print(s1 * 3)

#string repetation using '*' operator
print("*" *1)
print("*" *2)
print("*" *3)
print("*" *4)
print("*" *5)
print("*" *6)

#string reading from user
s = input("enter :")
print(s)

#string methods
#l.case conversion
#lower()
#upper()
#title()
#captalize()
#swapcase()
s = "PrekshA"
lower_string = s.lower()
print("Lower case conv:", lower_string)
print("Upper case conv:",s.upper())
print("Title case conv:",s.title())
print("Capitalize of string:",s.capitalize())
print("Swapcase conv:",s.swapcase())


#find(sub) - it returns the sub string index position,otherwise-1
#index(sub) - it returns the sub string index positions,otherwise "valueError"
#count(sub) - it returns the count of asubstring present in string
s = "Codegnan"
print(s.find("o"))
print(s.index("o"))
print(s.count("n"))

#strip(pat) - it removes the pattern from both sides of string, by default pat is space
#lstrip(pat) - it removes the pattern from left side of string by default pat is space
#rstrip(pat) - it removes the pattern from right side of string by default pat is space
s = "   codegnan   "
print(s.strip())
print(s.rstrip())
print(s.lstrip())

#string accessing nd slicing
s = "codegnan"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])
print(s[::1])
print(s[-2])
print(s[-1])
print(s[2:5])
print(s[4:])
print(s[:4])
print(s[4:2:-1])
