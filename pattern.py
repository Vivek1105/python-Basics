# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=' ')
#     print()


# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=' ')
#     print()


# n = int(input())
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(0,2*n-2*i):
#         print(" ",end='')
#     for j in range(i,0,-1):
#         print(j,end='')


def reverseEveryWord (sentence):
    words = sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence
sentence = "Welcome To Coding Ninjas"
print(reverseEveryWord (sentence))