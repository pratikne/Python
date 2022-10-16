'''
IMP : TUPLE()
--constant lists
#Can print via index but cant update..i.e immutable
#empty tuple is valid
t = ()
#single value tuple
t=(7)  ... It isnt tuple...just a plain int t datatype storing 7
t=(7,) ..Now its tuple having 1 value
'''

t=(1,2,5,7,2)
print(t)
print(t[2])
#t[0] = 5 #TypeError: 'tuple' object does not support item assignment


###METHODS

print(t.count(2))
print(t.index(5)) #returns index at which value provided


##Alt -  multiple cursors

