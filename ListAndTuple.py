marks = [50,42,38.50,47.25,21.75] # List use [ ] <-- this brackets 
print(len(marks))
print(type(marks))

""" List is mutable means You can access any element in it and change it to new value 
List can Store any kind of data type in single variable """

student = ["Uttam" , 9753124680 , 22 , "Patna" , "M"]
print(student)

student.append("AASE")
print(student)

marks = [11,9,8,5,12,10,-2]
print(marks)
# marks.sort() --> print(marks) || print(marks.sort()) return None
print(sorted(marks))

marks.sort(reverse=True)
print(marks)

print(list(reversed(marks))) # Take each value from the reverse iterator and put it into a list

marks.reverse()
print(marks)

marks.insert(3,7) #insert(at index , what element)
print(marks)

fruits = ["Banana" , "Litchi" , "Apple" , "Pomegranate"]
print(sorted(fruits))
fruits.sort(reverse=True)
print(fruits)

fruits.remove("Apple") # whatever given that first element removed
print(fruits)

fruits.pop(2) # removes at that index 
print(fruits)

""" Tuples 
 It is Immutable like String """

tup = (12,13,21,20,19,15,12,11,12,12)
print(type(tup))

# tup[3] = 29 it is not possible 

print(len(tup))
print(tup[5])

tup1 = (1,) # this is valid if only one single element is there because if you don't give comma python think int element written in bracket

print(tup.count(12))
print(tup.index(21))

# Ask user 3 movie and collect it in list
movie = []
movie.append(input("Enter 1st Movie : "))
movie.append(input("Enter 2nd Movie : "))
movie.append(input("Enter 3rd Movie : "))

print(movie)

# is given list palindrome ?
l1 = [1,2,3,2,1]

l2 = l1.copy()
l2.reverse()

if(l1 == l2):
    print("Palindrome")
else:
    print("Not Palindrome")

# count A
tup2 = ("C","D","A","A","B","B","A")
print(tup2.count("A"))

ltup2 = list(tup2)
ltup2.sort()
print(ltup2)