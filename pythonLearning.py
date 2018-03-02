# num1 = 21
# num2 = 30
# sum = num1 + num2
# print(sum)

# myName = "adam"
# print("Hello my name is " + myName)

# myArray = ["apple","banana","milk","bread"]
# print(myArray[2])
# del myArray[3]
# print(myArray)
# myArray.append("Snacks")
# print(myArray)

# myDictionary = {"Adam":23,"Bob":25,"John":34}
# print(myDictionary["Bob"])

# TUPLES

# tuple1 = ("Maths",123,"Cat")
# # cant append or delete. only reuse the variable name and reinitialise the variable with different value
# print(tuple1[1])
# print(tuple1[1:3])
# del tuple1

# myArray = ["apple","banana","milk","bread"]

# for i in myArray:
#     print(i)

#simple prime number generator

# for i in range(0,30):
#     j = 2
#     counter =0
#     while j< i:
#         if i%j == 0:
#             counter =   1
#             j = j + 1
#         else:
#             j = j+1
#     if counter == 0:
#         print(str(i) + " Is a prime number")

#     else: counter = 0        

#functions
def myLoop():
    for i in range(0,10):
        print(i)
       

myLoop()
