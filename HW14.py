#Name:Gavin Merrell
#Class: 5th Hour
#Assignment: HW14
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 1:
    print(i)
    i -=1
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
a = 1
while a <= 30:
    if a % 2 == 0:
        print (a)
    a += 1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
b =1
while b<=30:
    if b % 3 == 0:
        print (b)
    b += 1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
randomnumber = random.randint(1,6)
print(randomnumber)
while randomnumber <= 6:
    if randomnumber ==1:
        break
    print(randomnumber)
    randomnumber +=1

#5. Create a while loop that asks for a number input until the user inputs the number 0.
intnumber = int(input("Enter a number: "))

while intnumber > 0:
    if intnumber == 0:
        break
    intnumber = int(input("Enter a number: "))


