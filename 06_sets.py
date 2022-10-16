'''
SET{}
*no key value pair
*unindexed
*unordered
*immutable
*no duplicates are added (only unique elements)
*collection of non repetitive elements
*IMP ::: only immutable objects can be added

* a= {}
above will create empty dictionary but not set
'''

a={1,3,5,7,1}
print(a)
print(type(a))

b = {}   #b is empty dictionary
print(b)
print(type(b)) # <class 'dict'>


###creates empty set
c = set()
print(c)
print(type(c)) # <class 'set'>

#to add elements, .add() is used
c.add(2)
c.add(1)
c.add(1) #ignored as 1 is already present
c.add("Pratik") #allowed as string is immutable
#c.add([1,2,3]) #TypeError: unhashable type: 'list'...list is mutable
c.add((1,2,3)) #allowed as tuple is immutable
#c.add({1:23}) #TypeError: unhashable type: 'dict'...dict is mutable
print(c)


print(len(c))  #prints length of set
c.remove(2)
#c.remove(5) # KeyError: 5 as 5 wasnt present in set c
print(c)


c.pop()  #removes any 1 random element from set
print(c)

newUnionset = c.union({1,2,3,4,5})  #joins 2 sets(common is inclued just once) and returns new set
newIntersectset = c.intersection({"Pratik"})  #returns new set which is common in noth sets
print(newUnionset)
print(newIntersectset)


c.clear()
print(c)


sp={20,20.0,20.00,"20"} # 20.0,20.00 are ignored as Python internally sees them as 20 int
print(sp)
print(len(sp))