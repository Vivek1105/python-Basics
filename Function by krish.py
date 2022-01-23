# def count(a):
#     n = len(a)
#     Result =[0]*n
#     c = [0]*10
#     for i in range (0,n):
#         c[a[i]] +=1
#     for i in range(1,10):
#         c[i] += c[i-1]
#     i = n-1
#     while i>=0:
#         Result[c[a[i]]-1] = a[1]
#         c[a[i]] -= 1
#         i = i-1
#         return Result
# a = list(map(int,input("enter number:").split()))
# print(count(a))


# def count_sort(arr):
#     max_element = int(max(arr))
#     min_element = int(min(arr))
#     range_of_elements = max_element - min_element + 1
#     count_arr = [0 for _ in range(range_of_elements)]
#     output_arr = [0 for _ in range(len(arr))]
#     for i in range(0, len(arr)):
#         count_arr[arr[i] - min_element] += 1
#     for i in range(1, len(count_arr)):
#         count_arr[i] += count_arr[i - 1]
#
#     for i in range(len(arr) - 1, -1, -1):
#         output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
#         count_arr[arr[i] - min_element] -= 1
#
#     for i in range(0, len(arr)):
#         arr[i] = output_arr[i]
#
#     return arr
#
#
# # Driver program to test above function
# arr = [-5, -10, 0, -3, 8, 5, -1, 10]
# ans = count_sort(arr)
# print("Sorted character array is " + str(ans))




def counting_sort(l):
    size = len(l)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[l[i]] += 1

    for j in range(1,10):
        count[j] += count[j-1]

    a = size-1
    while a >= 0:
        output[count[l[a]]-1] = l[a]
        count[l[a]] -= 1
        a -= 1

    for k in range(0, size):
        l[k] = output[k]

l1 = [2,5,1,3,5,6,4,3,2,6]
counting_sort(l1)
print(l1)