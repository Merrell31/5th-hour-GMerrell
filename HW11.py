#Name:Gavin Merrell
#Class: 5th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
ThreeVar = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print(ThreeVar)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if ThreeVar[0] > ThreeVar[1] and ThreeVar[0] > ThreeVar[2]:
    print(ThreeVar[0])
    num = ThreeVar[0]
elif ThreeVar[1] > ThreeVar[2] and ThreeVar[1] > ThreeVar[0]:
    print(ThreeVar[1])
    num = ThreeVar[1]
else:
    print(ThreeVar[2])
    num = ThreeVar[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if (num % 2) == 0:
    print("num is divisable by 2")
    if (num % 3) == 0:
        print("num is divisable by 3")
    elif (num % 2,3) == 0:
        print("num is divisable by 2 and 3")
else:
    print("num is not divisible by 2 or 3")
