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