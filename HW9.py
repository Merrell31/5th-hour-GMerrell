#Name:Gavin Merrell
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dictionary1 = {
        "name" : "Gavin",
        "dob" : [6,9,2009],
        "age" : "17"
}
#3. Print the keys of the dictionary from #2.
print(dictionary1.keys())
#4. Print the values of the dictionary from #2
print(dictionary1.values())
#5. Print one of the three numbers from the list by itself
print(dictionary1["dob"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dictionary1.update({"grade" : 12})
#7. Print the entire dictionary from #2 with the updated key and value.
print(dictionary1)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
nesteddictionary = {
       "person1" :{
        "name" : "ethan",
        "grade" : 12,
        "5th hr" : "computer science",
       },
        "person2" :{
        "name" : "cruz",
        "grade" : 9,
        "5th hr" : "computer science"
        },
        "person3" :{
            "name" : "helber",
            "grade" : 12,
            "5th hr" : "computer science"
    }}
print(nesteddictionary)
#9. Print the names of all three classmates on the same line.
print(nesteddictionary["person1"]["name"],nesteddictionary["person2"]["name"],nesteddictionary["person3"]["name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
nesteddictionary.pop("person3")
print(nesteddictionary)