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