# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 1: Add the elements of two lists
# Elements at the same position are added together.

list1 = [10, 20, 30, 40]
list2 = [5, 15, 25, 35]

result = []                          # empty list to store the sums
for i in range(len(list1)):          # go through each index
    result.append(list1[i] + list2[i])

print("List 1:", list1)
print("List 2:", list2)
print("Sum of elements:", result)
