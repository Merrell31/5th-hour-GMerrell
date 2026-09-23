#Name: Gavin Merrell
#Class: 5th Hour
#Assignment: HW8
from random import random

#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
randint1 = random.randint(1,10)
randint2 = random.randint(1,10)
randint3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(randint1, randint2, randint3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
randint1added = randint1 + 2
print(randint1added)
randint2subtracted = randint2 - 4
print(randint2subtracted)
randint3multiplied = randint3 * 1.5
print(randint3multiplied)
#6. Print each result from #5 on the same line.
print( randint1added, randint2subtracted, randint3multiplied)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
randintlist = [random.randint(1,6),random.randint(1,6), random.randint(1,6),random.randint(1,6)]
print(randintlist)
#8. Sort the list in #7 and print it.
sortlist = sorted(randintlist)
print(sortlist)
#9. Add together the highest three numbers in the list from #7 and print the result.
sortlistadd = sortlist[1] + sortlist[2] + sortlist[3]
print(sortlistadd)

#10. Create a list with 5 names of other students in this class and print the list.
namelist = ["ethan", "gavin", "cruz", "max", "santi",]
print(namelist)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(namelist)
print(namelist)
#12. Print a random choice from the list of names from #10.
randomname = random.choice(namelist)
print(randomname)
