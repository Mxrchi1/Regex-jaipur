# Q1 Write a program that takes an integer input from the user and checks whether the number is odd or even.
a= int(input("enter a number "))
if(a%2==0):
    print("the number is even")
else:
    print("the number is odd")

# Q2 Write a program that takes three numbers as input and prints the largest of the three.
a = int(input("enter your values for a "))
b = int(input("enter your values for b "))
c = int(input("enter your values for c "))
if (a>b and a>c ):
    print("a is greater")
elif (b>a and b>c ):
    print("b is greater")
elif (c>a and c>b ):
    print("c is greater")

# Q3 Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
year= int(input("enter your number "))
if(year%4==0):
    if(year%100 !=0 or year%400==0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")

''' Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
on the following criteria:
>= 90: Grade A
>= 80: Grade B
>= 70: Grade C
>= 60: Grade D
< 60: Grade F'''
precentage=int(input("enter your  percentage"))
if(precentage>=90 ):
    print("your Grade is A")
if(precentage>=80 and precentage<90):
    print("your Grade is B")
if(precentage>=70 and precentage<80):
    print("your Grade is C")
if(precentage>=60 and precentage<70):
    print("your Grade is D")
if(precentage<60):
    print("your Grade is F")

# Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.
character = input("Enter your character: ")

if character in "aeiou":
    print("This is a vowel")
else:
    print("It's a consonant")

# Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.).
day= int(input("enter day of week"))
if(day==1):
    print("its Monday ")
elif(day==2):
    print("its Tueday ")
elif(day==3):
    print("its wednesday ")
elif(day==4):
    print("its thursday ")
elif(day==5):
    print("its Friday ")
elif(day==6):
    print("its saturday ")
elif(day==7):
    print("its sunday ")
else:
    print("inavlid day of week")
# Q8 Write a program that checks if a username and password entered by the user match the pre-set values username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print "Login Failed".

username= input("enter  your username ")
password= input("enter your password ")

if(username=="admin" and password=="1234"):
    print("Login success!")
else:
    print("Login failed ")    

# Q7 Write a program that takes a number as input and checks whether it is positive, negative, or zero.

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

''' Q11 Write a program that calculates the discount for a product based on its price:
If price is greater than 1000, discount is 10%
If price is between 500 and 1000, discount is 5%
Otherwise, no discount
Print the final price after applying the discount.'''
price = float(input("Enter the price of the product: "))
if price > 1000:
    discount = price * 0.10  
elif price >= 500 and price <= 1000:
    discount = price * 0.05  
else:
    discount = 0  
final_price = price - discount
print("Final price after discount is:", final_price)

''' Q14 Write a program that categorizes a given age into different groups:
Infant (0-1 year)
Toddler (2-4 years)
Child (5-12 years)
Teenager (13-19 years)
Adult (20-59 years)
Senior (60 years and above)'''
age = int(input("Enter the age: "))

if age >= 0 and age <= 1:
    print("Infant")
elif age >= 2 and age <= 4:
    print("Toddler")
elif age >= 5 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")
else:
    print("Invalid age")

