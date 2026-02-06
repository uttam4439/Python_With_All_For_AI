name = "Uttam Kumar"
print(name[0])
print(len(name))
print(name[-5:-1])

print(name.endswith("ar"))
print(name.endswith("ma"))

job = "advanced Associate Software Engineer"
print(job.capitalize()) #This prints the string first letter in capital.
print(job) 
""" Even just changing to capital in previous line it still print in small because it job.capitalize() create new 
string and make changes For making changes in the actual String you have assign the changes to the old ones like
job = job.capitalize() """

print(job.replace("Software", "AI")) # software word is replaced with AI
print(job.find("AI")) # This gives -1 because it can't find anything like that

print(job.count("nced")) # count the occurance of the substring

# Take User Input first name and print length

first_name = input("Enter your First Name :")
#first_name = print(len(input("Enter your First Name :")))
# print(len(first_name))

#Occurence of $ 
money = "$Dollar $Paypal $CreditCard $Debt $Youtube"
print(money.count("$"))

#Conditional Statement 
marks = int(input("Enter Student Marks : "))

if(marks >= 90):
    grade = "A"
elif(marks < 90 and marks >= 80):
    grade = "B"
elif(marks < 80 and marks >= 70):
    grade = "C"
else:
    grade = "D"

print(first_name , "got grade :" , grade)