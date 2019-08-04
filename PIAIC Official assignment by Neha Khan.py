
# coding: utf-8

# ## 1. Calculate Area of a Circle

# #### Write a Python program which accepts the radius of a circle from the user and compute the area.
# ###### Program Console Sample Output 1:
# ###### Input Radius: 0.5
# ###### Area of Circle with radius 0.5 is 0.7853981634

# In[9]:


radius=float(input("Enter the radius of the circle"))
area=3.142 * radius**2
print(f"Area of circle with radius {radius} is {area}")


# ## 2. Check Number either positive, negative or zero

# #### Write a Python program to check if a number is positive, negative or zero
# ###### Program Console Sample Output 1:
# ###### Enter Number: -1
# ##### Negative Number Entered
# ###### Program Console Sample Output 2:
# ##### Integer: 3
# ##### Positive Number Entered
# ###### Program Console Sample Output 3:
# ##### Integer: 0
# ###### Zero Entered

# In[3]:


num = int(input("Enter any number"))
if num == 0 :
    print("number is zero")
elif num > 0:
    print("num is positive")
else:
    print("num is negative")


# ## 3. Divisibility Check of two numbers

# #### Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# ##### Program Console Sample Output 1:
# ###### Enter numerator: 4
# ###### Enter Denominator: 2
# ##### Number 4 is Completely divisible by 2
# ###### Program Console Sample Output 2:
# ##### Enter numerator: 7
# 
# ##### Enter Denominator: 4
# ###### Number 7 is not Completely divisible by 4

# In[9]:


num1=int(input("Enter the numerator"))
num2=int(input("Enter the denominator"))
if num1%num2==0:
    print(f"number {num1} is completely divisible by {num2}")
else:
     print(f"number {num1} is not completely divisible by {num2}")


# In[10]:


num1=int(input("Enter the numerator"))
num2=int(input("Enter the denominator"))
if num1%num2==0:
    print(f"number {num1} is completely divisible by {num2}")
else:
     print(f"number {num1} is not completely divisible by {num2}")


# ## 4. Calculate Volume of a sphere

# ##### Write a Python program to get the volume of a sphere, please take the radius as input from user

# ##### Program Console Output:
# ##### Enter Radius of Sphere: 1
# ###### Volume of the Sphere with Radius 1 is 4.18

# In[3]:


radius=float(input("Enter the radius of the sphere: "))
volume=1.33*3.142*radius**3
print(f"volume of sphere with radius {radius} is {volume}")


# ## 5. Copy string n times
# #### Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# ##### Program Console Output:
# ##### Enter String: Hi
# ###### How many copies of String you need: 4
# ###### 4 Copies of Hi are HiHiHiHi

# In[9]:


string=input("Enter a string: ")
n=int(input("How many of copies of string you want?: "))
if n>0:
    print(f"{n} copies of string {string} are : {string*n}")
else:
        print("Invalid")


# ## 6. Check if number is Even or Odd
# ### Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
# #### Program Console Output 1:
# ##### Enter Number: 4
# ###### 4 is Even
# #### Program Console Output 2:
# ##### Enter Number: 9
# ###### 9 is Odd

# In[2]:


#for even num
num=int(input("Enter any num: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# In[4]:


#for odd num
num=int(input("Enter any num: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# ## 7. Vowel Tester
# ### Write a Python program to test whether a passed letter is a vowel or not
# #### Program Console Output 1:
# ##### Enter a character: A
# ###### Letter A is Vowel
# #### Program Console Output 2:
# ##### Enter a character: e
# ###### Letter e is Vowel
# #### Program Console Output 2:
# ##### Enter a character: N
# ###### Letter N is not Vowel

# In[7]:


vowels=['a','e','i','o','u']
letter=input("Enter a sound: ")
if letter in vowels :
    print(f"{letter} is vowel")
else:
    print(f"{letter} is not a vowel")


# ## 8. Triangle area
# ### Write a Python program that will accept the base and height of a triangle and compute the area
# ###### Reference:
# https://www.mathgoodies.com/lessons/vol1/area_triangle

# In[4]:


#Area of triangle
base=float(input("Enter the base"))
height=float(input("Enter the height"))
area=1/2*base*height
print(f"Area of triangle is {area}")


# ## 9. Calculate Interest
# ### Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# #### Program Console Sample 1:
# ##### Please enter principal amount: 10000
# ###### Please Enter Rate of interest in %: 0.1
# ###### Enter number of years for investment: 5
# ###### After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1

# ## 10. Euclidean distance
# ### write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# #### Program Console Sample 1:
# ###### Enter Co-ordinate for x1: 2
# ###### Enter Co-ordinate for x2: 4
# ###### Enter Co-ordinate for y1: 4
# ###### Enter Co-ordinate for y2: 4
# ###### Distance between points (2, 4) and (4, 4) is 2

# ###### Reference:
# https://en.wikipedia.org/wiki/Euclidean_distance

# In[11]:


x1=int(input("Enter Co-ordinate for x1: "))
x2=int(input("Enter Co-ordinate for x2: "))
y1=int(input("Enter Co-ordinate for y1: "))
y2=int(input("Enter Co-ordinate for y2: "))
import math
print(f"(x1,y1))=({x1},{y1}")
print(f"(x2,y2))=({x2},{y2}")
distance_formula = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
distance_formula = round(distance_formula,2)
print(f"The Distance Between Points ({x1},{y1}) and ({x2},{y2}) are: {distance_formula}")



# ## 11. Feet to Centimeter Converter
# ### Write a Python program to convert height in feet to centimetres.
# ##### Program Console Sample 1:
# ###### Enter Height in Feet: 5
# ###### There are 152.4 Cm in 5 ft
# ###### Reference:
# https://www.rapidtables.com/convert/length/feet-to-cm.html

# In[12]:


feet=int(input("Enter height in feet"))
cm=feet*30.48
print(f"There are {cm} cm in {feet} ft")


# ## 12. BMI Calculator
# ### Write a Python program to calculate body mass index
# ##### Program Console Sample 1:
# ###### Enter Height in Cm: 180
# ###### Enter Weight in Kg: 75
# ###### Your BMI is 23.15

# In[14]:


import math
height=int(input("Enter height in cm:"))
weight=int(input("Enter weight in kg:"))
BMI=(weight/(math.pow(height*0.012,2)))
BMI= round(BMI,2)
print(f"Your bmi is:{BMI}")


# ## 13. Sum of n Positive Integers
# ### Write a python program to sum of the first n positive integers
# #### Program Console Sample 1:
# ###### Enter value of n: 5
# ###### Sum of n Positive integers till 5 is 15

# In[18]:


num=0
value=int(input("Enter the value of n: "))
for i in range(value+1):
    num+=i
    print(f"sum of n positive integers till {value} is {num}")


# ## 14. Digits Sum of a Number
# ### Write a Python program to calculate the sum of the digits in an integer
# #### Program Console Sample 1:
# ##### Enter a number: 15
# ###### Sum of 1 + 5 is 6
# #### Program Console Sample 2:
# ##### Enter a number: 1234
# ###### Sum of 1 + 2 + 3 + 4 is 10

# In[8]:


n=input("Enter any num ")
sum=0
for s in n:
    sum+=int(s)
print(f"The sum of num is:",sum)

