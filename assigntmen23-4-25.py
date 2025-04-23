# Q1 Write a program that takes an integer input from the user and checks whether the number is odd or even.
a= int(input("enter a number "))
if(a%2==0):
    print("the number is even")
else:
    print("the number is odd")

# Q2 Write a program that takes three numbers as input and prints the largest of the three.
a = int(input("enter your values 1 "))
b = int(input("enter your values 2 "))
c = int(input("enter your values 3 "))
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
