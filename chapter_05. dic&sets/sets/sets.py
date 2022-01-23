#this syntax create an epty dictionary not not a set
# a = {}
# print(type(a))

# #this syntax can create empty set
# b = set()
# print(type(b))




#creating an empty set 
c = set()
print(type(c))

#adding value to an empty set
c.add(2)
c.add(4)
c.add(5)
c.add(2)         #repeate value does not allow in sets
c.add((2,3,4))
#c.add({4:5})     # can not add list and dictionary in sets
print(c)

print(len(c))  #print the length of set
c.remove(4)   #remove 4 from the set
print(c.pop())   #remove random number
c.clear
print(c)