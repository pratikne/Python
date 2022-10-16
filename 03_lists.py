
'''IMP - LISTS[]
#lists are ordered
#indexing starts from 0
#lists are mutable..can be changed
#lists of diff types valid
#slicing possible same as strings
#List methods ::: sort,reverse,append,insert,pop,remove,clear,count
for more...check in Python docs
'''
a=[1,2,3,4,5]
print(a)
print(a[0])
a[0] = 10 
print(a[0])
#print(a[5]) #index out of range

#creating lists with items of diff types
b = [45, "Pratik", 4.5, False]
print(b[1:3]) #from index 1 till 3 not included

#Lists Method
#l1.sort

l1=[1,8,7,15,12]
l2=l1
l2.sort() #Asc sort
#l2.sort(reverse=True) #returns None.. Desc Sort
print(l2)


l2.reverse()
print(l2)

###Appends at the end ( Add karna)
l2.append(45)
l2.append(55)
l2.insert(0,34) #inserts value 34 at index 0
l2.insert(2,34) #inserts value 34 at index 2
print(l2)

l2.pop(5) #removes value from index provided i.e 7nd index value is removed
l2.remove(34) #removes 45 value from list ( 1st occurenece only)
print(l2)

# l2.clear()
# print(l2)

count = l2.count(55)
print(count)

print(sum(l1)) #returns sum total of values in the list

"""This is Docstring"""
'''
Iterators concept'''
ita=iter(a)
# print(next(ita))
# print(next(ita))
# print(next(ita))
# print(next(ita))
# print(next(ita))
# print(next(ita)) --StopIteration exception as list is ended

while True:
    try:
        print((next(ita)))
    except StopIteration:
        break

