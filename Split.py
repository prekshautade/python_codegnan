s= "The sky is blue and ocean is blue"
print(s.split('sky'))

#split(pat) - it splits the string where the pattern is match and returns as list of substring
#sep.join(iterable) - it joins the list of string into single string with sepeator
s = "The sky is  blue and ocean is blue"
print(s.split())
print(s.split('blue'))
print(s.split('u'))
print(s.split('zs'))

#join
a = ['The', 'sky', 'is', 'blue', 'and', 'oceans', 'is', 'blue']
print(":".join(a))

#chr() - it returns character of ASCII number
#ord() - it returns ASCII value of character
print(ord("A"))
print(chr(65))
print(chr(128514))

#string checking functions
#islower() - it returns true,when entire string is in lower case
#isupper() - it returns true,when entire string is in upper case
#isalpha() - it returns true,when entire string is only charatcers
#isalnum() - it returns true,when entire string is characters or digits
#istitle() - it returns true,when entire string is title case
#isdigit() - it returns true ,when entire string is digits
print("Codegnan".islower())
print("codegnan".islower())
print("CODEGNAN".isupper())
print("codegnan".isalpha())
print("Codegnan1".isalnum())
print("Codegnan".istitle())
print("Codegnan".isdigit())

#member ship operators
# in,not in
print("p" in "codegnan")
print("c" in "codegnan")

#sstring comparison
s1 = "abcd"
s2 = "abcde"
print(s1==s2)
print(s1 > s2)
print(s1 < s2)
print("ABC" < "abc")

#identity operator
#string comparison
s1 = "abcd"
s2 = "abcd"
print(id(s1), id(s2))
print(s1 == s2)
print(s1 is s2)

#sum built in function
#len() - it returns the length of string
print(len("Codegnan"))
print(max("Codegnan"))
print(min("Codegnan"))

#replace - it replace  the old substring with a new substring
s = "codegnan"
print(s.replace('c','p'))
print(s.replace('n','p' ,2))


