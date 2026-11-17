#Name: Gavin Merrell
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library
import random
#2. print "Hello World!"
print ("hello world")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
#4. Add a and b together, then divide the sum by c. Print the result.
ab = a + b
abc = ab/c
print (ab,abc)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(abc))
if abc%2==0:
    print ("even")
else:
    print ("odd")
#6. Create a list of five different random integers between 1 and 10.
intlist = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
print (intlist)
#7. Print the 4th number in the list.
print(intlist[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
intlist.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
intlist.sort(reverse=True)
print (intlist[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
L =1
while L <= 100:
    print (L)
    L += 1
#11. Create a list containing the names of five other students in the classroom.
namelist = ["ethan", "gavin", "cruz", "helbear", "the machine the myth the legend Cruz ;pepper jack; Parkurst"]
#12. Create a for loop that individually prints out the names of each student in the list.
for name in namelist:
    print (name)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
M = 1
for m in range (1,100):
    print (m)
    M += 1
    if M % 10 == 0:
        break

#14. Free space. Do something creative. :)