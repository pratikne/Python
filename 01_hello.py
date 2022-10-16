'''
********************
Author : Pratik Negi
********************
'''

import os
print("Hello world")
print(os.listdir()) #print content of files using os module

a = "Pratik" #string
b = 9  #int
c = 3+2j #complex
d = 9.2 #float
e='P' #string
f=True #bool - True/False
n = None #None type

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(n)
print(type(n))

p = input("Enter your name : ")  #input in form of String always even if input is a number..so typecast it accordingly
q = input("Enter your age :")
q = int(q) #typecasted to int
print("Hi" , p , ", Your age is" , q) #again to str for printing

#diff string literals
x="Pratik's"
y='Pratik"s'
z=''' Pratik's or Pratik"s 
    or Pratik '''
#x[1] = 'R' #cant as string is immutable

#String slicing
name = "Pratik"
print(name[0:4]) # [0,4) .. include from 0 index to 4-1 index
#prints Prat
print(name[1:4]) # [1,4) .. include from 1 index to 4-1 index
#prints rat
print(name[:4]) # [0,4) .. include from default 0 index to 4-1 index
#prints Prat
print(name[1:]) # [1,end) .. include from 1 index till end length() i.e 6 .. 6-1
#prints ratik
print(name[-1:]) # [-1,end) .. include from -1 index till end 
#prints k
print(name[-5:-1]) 
#prints rati

name = "PratikNegiJi"
print(name[0:10:2]) #2 is the skip value.i.e skip every 2nd value starting from 0th index till 8-1
#prints PaiNg

'''
 P  R  A  T  I  K
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1 
'''






#Module 
#Pip

#Ctrl + / --> comment/uncomment