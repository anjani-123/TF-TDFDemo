# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:46:29 2020

@author: Anjani Srivastava
"""
print("Welcome to The Grocery shop")
print("1. Rice    ------------------ Rs. 50/Kg")
print("2. Pulses  ------------------ Rs. 60/Kg")
print("3. Milk    ------------------ Rs. 40/Kg")
print("4. Ghee    ------------------ Rs. 80/Kg")
print("5. Bread   ------------------ Rs. 30/Kg")
name = input("Please enter your name")
mob_no = int(input("Please enter your mobile number"))
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
while True:
    ch = input("Do you want shopping\n Press y to proceed")
    if ch == 'y':
        choice = int(input("Please enter S.No. of item"))
        if choice == 1:
            print("You have selected Rice")
            rice_quan = 0
            rice_quan = int(input("Enter the amount of rice to be bought"))
            rice_cost = rice_quan * 50
            sum1 += rice_cost
        elif choice == 2:
            print("You have selected Pulses")
            pulses_quan = 0
            pulses_quan = int(input("Enter the amount of pulses you want"))
            pulses_cost = pulses_quan * 60
            sum2 += pulses_cost
        elif choice == 3:
            print("You have selected milk")
            milk_quan = 0
            milk_quan = int(input("Please enter the amount of milk you want"))
            milk_cost = milk_quan * 40
            sum3 += milk_cost
        elif choice == 4:
            print("You have selected Ghee")
            ghee_quan = 0
            ghee_quan = int(input("Please enter the amount of ghee you want"))
            ghee_cost = ghee_quan * 80
            sum4 += ghee_cost
        elif choice == 5:
            print("You have selected Bread")
            bread_quan = 0
            bread_quan = int(input("Please enter the amount of bread you want"))
            bread_cost = bread_quan * 30
            sum5 += bread_cost
        
        else:
            print("Invalid input!")
    if ch != 'y':
        break

sum = sum1+sum2+sum3+sum4+sum5
print("__________BILL GENERATED____________")
print("Name of the Customer ------ {}".format(name))
print("Mobile Number        ------ {}".format(mob_no))
print("         Items    |  Price Per Kg  |  Quantity |      Cost       |             ")
print("                  |                |           |                 |                ")
print("         Rice     |      Rs. 50    |     {}    |       {}        |             ".format(rice_quan,sum1))           
print("         Pulses   |      Rs. 60    |     {}    |       {}        |              ".format(pulses_quan,sum2))
print("         Milk     |      Rs. 40    |     {}    |       {}        |              ".format(milk_quan,sum3))
print("         Ghee     |      Rs. 80    |     {}    |       {}        |           ".format(ghee_quan,sum4))
print("         Bread    |      Rs. 30    |     {}    |       {}        |          ".format(bread_quan,sum5))
print("                  |                |           |                 |             ")
print("        TOTAL     |                |           |       {}        |                ".format(sum))
      
            

    
            
            

