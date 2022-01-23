a = 10
#if elif else ladder in python

if(a>8):
    print("value of a is greater than 8")
elif(a>6):
    print('value of a is greater than 6')
elif(a<6):
    print('value of a is less than 6')
else:
    print("value is not greater")

#multiple if statements
if(a>9):
    print('value of a is greater than 9')
    if(a>8):
        print("value of a is greater than 8")
    if(a>15):
        print("value of a is greater than 5")
    else:
        print("value of a is greater than")



#question
age = int(input("enter your age"))
if(age>18):
    print("yes")
else:
    print("no")


#LOGICAL OPERATORS
age = 21
name = "vishu"
if age>20 and name=="vishu":      #bot conditon must be satisfied
    print("yes")
else:
    print("no")

age = 21
name = "vishu"
if age>20 or name=="viv":     # atleat one condition must be satisfied
    print("yes")
else:
    print("no")


#is and in
a = none
if(a is none):
    print("yes")
else:
    print("no")


a = [23,43,4]
print(45 in a)