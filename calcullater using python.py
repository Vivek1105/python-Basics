def add(n1, n2):
    return  n1+n2

def subtract(n1,n2):
    return  n1-n2

def multiply(n1,n2):
    return  n1*n2

def divide(n1,n2):
    return  n1/n2

print("select operation \n" \
      "1. add\n" \
      "2. subtract \n" \
      "3. multiply \n" \
      "4. divide \n")

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))

number_2 = int(input("Enter second number: "))

if select == 1:

    print(number_1, "+", number_2, "=",

          add(number_1, number_2))



elif select == 2:

    print(number_1, "-", number_2, "=",

          subtract(number_1, number_2))



elif select == 3:

    print(number_1, "*", number_2, "=",

          multiply(number_1, number_2))



elif select == 4:

    print(number_1, "/", number_2, "=",

          divide(number_1, number_2))

else:

    print("Invalid input")