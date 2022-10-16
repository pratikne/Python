import pandas as pd
import numpy as np

dict1={"name":["Pratik","Ritik"],
        "Maths":[98,99]}
ser = pd.Series([1,2,3])
print(ser)

dft = pd.DataFrame(dict1)
print(dft)

#dft.to_csv('students.csv')

ser1=pd.Series(np.random.rand(10))


dft1=pd.DataFrame(np.random.rand(100,5))

print(ser1)
print("--------------------")
print(dft1)
print("--------------------")
print(dft1.head(50))
print("--------------------")
print(dft1.tail(50))
print(dft1.to_numpy())

newdft = dft1  #Creates view

newdft[0][0] = 10 #changes applivable to original as well

print(dft1[0][0])
print(newdft[0][0])

copydft = dft1.copy()  #This creates actual copy

copydft[0][0] = 20

print(dft1[0][0])
print(copydft[0][0])

print(dft1.loc[[0,2,5],[1,3]])
print(dft1.loc[[0,2,5],:])

print(dft1.loc[(dft1[1] < 0.3) & (dft1[3] > 0.1)])

print(dft1.describe())

print(dft1.count())
# print(dft1.max())
# print(dft1.min())
# print(dft1.median())
# print(dft1.mean())
# print(dft1.mode())

