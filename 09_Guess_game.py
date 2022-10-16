#Flask, Django is the framework made from python
#Tenserflow is a library

#to make user module
import py_compile

'''
create file with m<file_name>.py_compile
Eg: m01_hello.py

to import above module here 

import m01_hello

m01_hello.<whatever>

IMP NOTE :: for running from same module, use below

if __name__ == "__main__":
    pass

for same program, --name-- is same as main
but for different progran, --name-- is the module from where it is ran   

'''




'''
EXCEPTION HANDLING

try,except,finally blocks


try:
    #Code possibly throwing error
except Exception as e:
    #Handle it or print it



*a try can have multiple except handlings

try:
    pass
except ValueError:
    pass
except ZeroDivisionError:
    pass
except:   ##For all remaining
    pass

*********RAISING EXCEPTIONS************
*raise is use to raise custom exceptions

Eg:

try:
    pass
except:
    raise ValueErroe("Some error message")

It will raise above error if try is not fulfilled and program execution stops


*Sometimes try is used with else..else will only execute when try is successfully executed without raisig an exception
try:
    pass
except:
    pass
else:
    pass


***********FINALLY**********

finally will always execute even if try is successfull or Not (regardless of error).
even if except quits/exits the programs..finally will still execute
if try raises an exception, except will run for that exception and then finally block will run
unseccess case ::: try -> except -> finally
success case:::    try -> finally
try:
    pass
except:
    pass
finally:
    pass 
'''

import random
randno = random.randint(1,100)
userguess =  None
guesses = 0

while (userguess != randno):
    print("")
    print("---------------------------------------------------")
    print("Press q to quit:")
    userguess=input("Enter your guess : ")
    print("---------------------------------------------------")

    if(userguess=="q"):
        break
    try:
        userguess=int(userguess)
        guesses += 1
        if(userguess == randno):
            print("You guessed it right")
        elif(userguess > randno):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    except Exception as e:
        print(f"Exception : Invalid number : {e}")
        #print(e)
else:    
    print(f"You guessed the number in {guesses} guesses.")

    with open("Hiscore.txt",'r') as f:
        hiscore = int(f.read())

    if(guesses<hiscore):
        print("You have just broken the high score")
        print(f"Earlier High score : {hiscore}")
        print(f"Your New High score : {guesses}")
        with open("Hiscore.txt",'w') as f:
            f.write(str(guesses))

print("Thanks for playing:)")





