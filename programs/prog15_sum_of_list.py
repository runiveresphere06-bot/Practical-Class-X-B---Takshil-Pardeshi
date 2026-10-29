# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 15: Input a list and find the sum of the numerical values present in it
# Enter items separated by commas, e.g.  10, apple, 20.5, 7, hello
# Non-numeric items are ignored.

items = input("Enter list items separated by commas: ").split(",")

total = 0
for item in items:
    item = item.strip()              # remove extra spaces
    try:
        total += float(item)         # works only if the item is a number
    except ValueError:
        pass                         # skip items that are not numbers

print("List:", [i.strip() for i in items])
print("Sum of numerical values:", total)
