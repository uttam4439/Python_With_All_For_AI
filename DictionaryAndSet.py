# Nested Dictionary
Student = { "name" : "Uttam Kumar" ,
           "Subject_Marks" : 
           {"Phy" : 68 ,
            "Chem" : 70 ,
            "Maths" : 80}
}

print(Student)
print(Student["Subject_Marks"])
print(Student["Subject_Marks"]["Chem"])

print(Student.keys()) #Return all the Keys
print(Student.values()) #Return all the Values

print(Student.items()) # return all key-value as tuples

print(Student["name"]) # --> Gives Error when the given parameter is not present -> Safe when you want the data any how 
print(Student.get("name")) # --> Gives None when the given parameter is not present in the dictionary -> Use in production where Optional case 

print(list(Student.values()))
print(list(Student.items())) # --> save in any variable and use it as a list

Student.update({"Grade" : "O"})

new_dict = {"city"  : "delhi" , "Ph. no" : 9753124680}
Student.update(new_dict) # If you update the existing key it only overwrite the respective key value not add new
print(Student)

""" Set 
 It is the collection of unordered items  , all items are unique and immutable (can't add list and dict)
 means sets are mutable like you add and remove in sets but not change the element value to new (Unhashable Value)"""

Unique_set = {1,2,3,4,2,2,2,"Hello",'C' , "World" , "World"}

print(Unique_set)
print(len(Unique_set))

# empty_set = {}  it will give dictionary 
# to make empty set 
empty_set = set()

empty_set.add(1)
empty_set.add(2)

stup = (1,2,3) # Tuples can also be added
empty_set.add(stup)
empty_set.remove(2)
empty_set.clear()

print(empty_set)
print(type(empty_set))

dummy_set = {"Python" , "Hello" , "Uttam" , "Rahul" , "Java" , "Python", " Uttam"}

print(dummy_set.pop()) # removes any random value

#Union and InterSection 
set1 = {1,2,3,4}
set2 = {2,4,7,9}

print(set1.union(set2)) # combine unique value and return new set
print(set1.intersection(set2)) # combine common vlaue and return new set

#Make original dictionary

dict = {
    "table" : ["a piece of furniture" , "list of fact and figures"] ,
    "cat" : "a small animal"
}
print(dict)

count_classroom = {"python","java","python","java","python","java","C++","python","javascript","python","C++","C","C"}
print(len(count_classroom))

marks = {}
marks1 = int(input("Enter Phy Marks :"))
marks.update({"phy" : marks1})
marks2 = int(input("Enter Chem Marks :"))
marks.update({"chem" : marks2})
marks3 = int(input("Enter Maths Marks :"))
marks.update({"Maths" : marks3})

print(marks)