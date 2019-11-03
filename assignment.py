import sys
import datetime
from math import pi
#QUE 1
#Write a Python program to print the following string in a specific format
#(see the output).

#Twinkle, twinkle, little star,
#How I wonder what you are!
#Up above the world so high,
#Like a diamond in the sky.

#Twinkle, twinkle, little star,
#How I wonder what you are
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#QUE 2
#Write a Python program to get the Python version you are using
print("Python Version")
print(sys.version)
print("Version information")
print(sys.version_info)


#QUE 3  Write a Python program to display the current date and time.
dateetime = datetime.datetime.now()
print ("Current date and time : ")
print (dateetime.strftime("%Y-%m-%d %H:%M:%S"))


#QUE 4 Write a Python program which accepts the radius of a circle from the user
#and compute the area.


radius = float(input ("Input radius of the circle= "))
print ("The area of the circle " + str(radius) + " is: " + str(pi * radius**2))

#QUE 5 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between
First_name = input("Input your First Name : ")
Last_name = input("Input your Last Name : ")
print ( Last_name + " " + First_name)

#QUE 6 Write a python program which takes two inputs from user and print them
#addition
number1 = input("First number: ")
number2 = input("\nSecond number: ")


sum = int(number1) + int(number2)
print("Ans = "+str(sum))