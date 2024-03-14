'''
# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is a square are not

length = int(input())
breadth = int(input)
if length==breadth:
    print("its a square")
else:
    print("its not square")


# ! Eg:4
# Python program to check whether the given integer is multiple of both  5 and 7

n=int(input("enter the number:"))
if n%5==0 and n%7==0:
    prin("yes")
else:
    print("no")


# ! Eg:5
# write a progrm to accept the cost price of bike and display the road tax to be paid
# according to the following criteria:

price = int(input("enter the price:"))
amount=0
if price>=100000:
    discount = 100000*(6/100)
    value=price-discount
    amount=value*(15/100)
    total = value+amount
else:
    tax=price*(5/100)
    total=price+tax
    print("the onroad cost of bike is:",total)

#   ! Eg:1
a=7
b=9
c=7

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")


A School has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.


mark = int(input("Enter mark:")
if mark>=80 and mark<=180:
    print("A")
elif mark>=60 and mark<=80:
    print("B")
elif mark>=50 and mark<=60:
    print("c")
elif mark>40 and mark<=50:
    print("D")
else:
    print("Fail")


# ! Eg:6
# ! accent the age of 4 people and display the oldest one
 a=9
 b=6
 if a>b:
     print("A")
else:
    print("B")
#? --> using shorthand if else
# Rules
# 1) Statement inside the if condition have to be represent at first
# 2) elif cannot be used in short hand if else
# 3)always it have to end with else

print("A") is a>b else print("B")

# 1 code to check the given char is vowel or consonent
char = input("Enter the char:")
if char=="a" or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("is a vowel")
else:
    print("its a consonent")

# or

strl = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")

# ! shothand if else
char = input("Enter the char:")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")

#! ---> elif ladder using short hand if else
# Eg:1
# ? Find greatest among 3 variable using short hand if else
a=8
b=5
c=9

print("A is greater") if a>b and a>c else print("B is greater")
if b>a and b>c else print("C is greater")

# ! ---> looping

#looping can be implemented using
# for loop
# while loop

# --> for loop
# ? for loop is used for iteration, if we known the number of times the loop have to return
# ? It is used to iterate the iterables eg(string,list, tuple,etc)

# to do --> syntax for loop

for syntax in C
for(i=0:i<10:i++){
    printf("hello")
}

# ! for syntax python
for userdefined_variable in range(start,end,step):
    statement
    statement
    statement

   # ? Eg:1
   # to print the value from 1 to 10 using for loop

   # for i in range (0, 10): #(n , n-1)
   #     # print(1)
   #     #print("hello")
   

#  --> method:3
'''
for val in range (1,10+1):
    print(f"7 * {val}={val*7}")
'''
# ?Eg:5
# break --> used to teerminate the loop

for val in range(1, 10):
#   if val ==6:
#      break
#    print(val)

                  
                  







   




   










 














 
