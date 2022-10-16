'''
DICTIONARY{}
*   {Key:value}
*Nested dict possible

*Unordered
*Mutable
*indexed via key
*cannot contain Duplicate key - new value will be overridden for that key
'''

myDict = {1:"Pratik",
          2:"Ritik",
          3:[1,2,3,4,5],
          4 : {"Pratik":"Negi"},
          "New":2
         }
print(myDict)
print(myDict[3])    
print(myDict.get(10))   #get returns None if key is not present
#print(myDict[10])       #returns KeyError
print(myDict[4]["Pratik"])

myDict[3]=3.5
print(myDict)

#Keys and values can be converted into list
l1=list(myDict.keys())
l2=list(myDict.values())
print(l1)
print(l2)
print(myDict.items())  #Type dict_items..showcases entire dict in tuple format
#prints the (key,value) contents of the dictionary

updDict={"qwerty":23}
myDict.update(updDict) #adds the updDict content in myDict dictionary
myDict.update({9:"Newvalue"})
print(myDict.items()) 

dict3={2:[1,2,3],
    1:[2,3,1]
    }
#Sorting via keys
for i in sorted(dict3.keys()):
        print(i, end=" ")

print("")
for i in sorted(dict3.values()):
        print(i, end=" ")
print("")
