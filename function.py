def percent(marks):
    return(sum(marks)/300)*100
marks1 = [43,45,32]
p1 = percent(marks1)

marks2 = [65,75,55]
p2 = percent(marks2)
print(p1,p2)



quze
def greet(name):
    print("gud mrng" +name)
greet("viv")



#type of function
def mysum(n1,n2):
    return n1+n2
s = mysum(33,34)
print(s)



#default parameter value
def greet(name=" koi v"):
    print("gud mrng" +name)
greet(" viv")
greet()