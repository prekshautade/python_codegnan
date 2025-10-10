#example of dictionary
d = {1:"a","a":1,"hi":"hello",(1,2,3):(10,20,30),12.241:10.00}
print(d)


#duplicate keys
d = {1:"a","a":1,"hi":"hello",(1,2,3):(10,20,30),12.241:10.00,1:'z'}
print(d)


#list cant be used as keys
d = {1:"a","a":1,"hi":"hello",[1,2,3]:(10,20,30),12.241:10.00,1:'z'}
print(d)


#values access by passing keys
d = {1:"a","a":1,"hi":"hello",(1,2,3):[10,20,30],12.241:10.00,1:'z'}
print(d[1])


#update values and items
d[1]="x"
print(d[1])
print(d["a"])
d['1']='x'
print(d['1'])
print(d)


#empty dictionary representation
d1={}
d2=dict()
print(type(d1),type(d2))


##methods
##get(key,default)- it returns the values if key is present in dictionary,otherwise default value
##update(new_dict)- it updates the dictionary with new_dictionary items
##pop(key)-it returns and removes the item if key is present in dictionary otherwise it will be keyerror
##popitem()-it returns and remove the last item
##keys()-it returns and removes the last item
##values()-it returns list of values
##items()-it returns the list of tuple of key value pairs
##clear()-it removes all item form dict

#get
d = {1:"a","a":1,"hi":"hello",(1,2,3):[10,20,30],12.241:10.00,1:'z'}
print(d.get(1))
print(d.get(10))
print(d.get(10 ,"noootttt presenttt"))
print(d.get(10,0))

#update
d1 = {"batch":39,"Course":"PFS"}
d2 = {"Course":"JFS","lang":"java"}
d1.update(d2)
print(d1)

#popitem(),clear()
d = {'batch':39,'Course':'PFS','lang':'python'}
print(d.popitem())
print(d.pop('Course'))
print(d)
d.clear()
print(d)








