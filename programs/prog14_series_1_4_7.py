# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 14: Input a positive integer n and display the series 1, 4, 7, 10 ... n
# Each term is 3 more than the previous one, so we use a step of 3 in range().

n = int(input("Enter a positive integer: "))

if n > 0:
    print("Series:")
    for i in range(1, n + 1, 3):     # start=1, stop=n (included), step=3
        print(i, end=" ")
    print()
else:
    print("Please enter a positive integer.")
