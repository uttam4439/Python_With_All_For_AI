i = 0
while i < 5:
    print("I am Learning Python" , i)
    i += 1


tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

idx = 0
for ele in tup:
    if(ele == 49):
        print("found at idx :" , idx)
        break
    print(ele)
    idx += 1
else:
    print("END")


for ele in list:
    print(ele)

# when we don't want anything inside loop
for j in range(5):
    pass

print("No issue if we print passing the loop")