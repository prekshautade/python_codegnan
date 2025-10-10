#set example
s = {1,2,34,20.25,"Codegnan",(1,2,3),1,2}
print(s)

#emptyset creation
s1 ={}
s2 = set()
print(type(s1),type(s2))

#read integers
s = set(map(int,input("enter number:").split()))
print(s)

#set operations
s1 = {1,2,"hi","hello"}
s2 = {"python","java"}
print("union:",s1.union(s2))
print("intersection:",s1.intersection(s2))
print("difference:",s1.difference(s2))
print("symmectric difference:",s1.symmetric_difference(s2))
print("subset:",s1.issubset(s2))
print("superset:",s1.issuperset(s2))
print("dis joint set:",s1.isdisjoint(s2))

#example
s1 = {1,2,10,9}
s2 = {40,20,60,10}
print("union:",s1.union(s2))
print("intersection:",s1.intersection(s2))
print("difference:",s1.difference(s2))
print("symmectric difference:",s1.symmetric_difference(s2))
print("subset:",s1.issubset(s2))
print("superset:",s1.issuperset(s2))
print("dis joint set:",s1.isdisjoint(s2))

#example 2
s1 = {1,2,5}
s2 = {1,3,4,5}
print("union:",s1|s2)
print("intersection:",s1&s2)
print("difference:",s1-s2)
print("symmectric difference:",s1^s2)

#union()-it returns all elements from sets without duplicates
#intersection()-it returns all comman elements from sets
#difference()-it returns only one current set elements not other set elements
#symmetric difference()-it returns all non-comman elements from sets
#subset()-it checks current set is subset to other set or not
#superset()-it checks current set is superset to other set or not
#dis joint set()-it checks all set wheather it have comman elements or not
#add(ele)-it add elemnts to set if element not present in set,otherwise nothing
#remove(ele)-it removes the elements from set if element present in set ,otherwise 'keyError'
#discard()-it removes the elements if elements present in set ,otherwise nothing
#update()-it update the new_set of elements in current set
#pop()-it returns and removes the elements from set
s1 = {1,2,3.5,65,43}
s1.add(100)
s1.add(1)
print(s1)
s1.remove(100)
print(s1)
s1.discard(100)
s1.discard(2)
print(s1)
print(s1)


