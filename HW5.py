#Name: Gavin Merrell
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
namelist = ["Gavin", "Ethan", "Sam", "Waylon", "Jaxton"]
print(namelist)
#2. Append a new name onto the Name List.
namelist.append('grant')
print(namelist)
#3. Print out the 4th name on the list.
print (namelist[5])
#4. Create a list with 4 different integers in it.
numlist = [1, 2, 3, 4]
print(numlist)
#5. Insert a new integer into the 2nd spot and print the new list.
numlist.insert(1, 5)
print(numlist)
#6. Sort the list from lowest to highest and print the sorted list.
numlist.sort()
print(numlist)
#7. Add the 1st three numbers on the sorted list together and print the sum.
numlistsum = numlist[0] + numlist[1] + numlist[2]
print(numlistsum)
#8. Create a list with two strings, two variables, and too boolean values.
mixedlist = ['string 1', 'string 2', 10, 20, False, True]
print(mixedlist)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
mixedlist.append(input("Give me an Index value"))


