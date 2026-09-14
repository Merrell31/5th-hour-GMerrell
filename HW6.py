#Name: Gavin Merrell
#Class: 5th Hour
#Assignment: HW6

print('hello world')
#1. Create a list with 9 different numbers inside.
numlist = [1,2,3,4,5,6,7,8,9]
print(numlist)
#2. Sort the list from highest to lowest.
numlist.sort()
print(numlist)
#3. Create an empty list.
emptylist = []
print(emptylist)
#4. Remove the median number from the first list and add it to the second list.
numlist.pop(4)
print(numlist)
#5. Remove the first number from the first list and add it to the second list.
numlist.remove(1)
emptylist.insert(0,5)
#6. Print both lists.
print (emptylist)
print (numlist)
#7. Add the two numbers in the second list together and print the results.
emptylistadded = emptylist[1] + emptylist[0]
print(emptylistadded)
#9. Sort the first list from lowest to highest and print it.

numlist.sort()
print(numlist)