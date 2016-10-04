###Age_Calculus is a free program written python
##This is Age Calculus version 1.1 by Priyes Bamne
##This versions also calculates Month and date which is not available in previous Age -Calculus V1.0
import datetime
import math
priyes = datetime.datetime.now()
##Getting input from use and displaying error if date/month/year are invalid
def AgeCalculus(month, day, year):

    if (user_month > 12 or user_month < 1):
        print("Enter a valid month")
    
    elif (priyes.month < user_month):

        month = 12 + (priyes.month - user_month)
        year = priyes.year - user_year - 1

        if (priyes.day <= user_day):
            day = user_day - priyes.day

        elif (priyes.day >= user_day):
            day = priyes.day - user_day

        else:
            print("Enter a valid date")

    elif(priyes.month >= user_month): 

        if (priyes.month == user_month):

            if priyes.day >= user_day:
                month = 0
                year = priyes.year - user_year

            else:
                month = 11
                year = priyes.year - user_year - 1

        else:
            month = priyes.month - user_month
            year = priyes.year - user_year

        if (user_day > 31 or user_day < 1):
            print("Enter a valid date")

        elif (priyes.day < user_day):
            day = 30 - (user_day - priyes.day)

        elif (priyes.day >= user_day):
            day = priyes.day - user_day

    print("Your current age is",year," years,",month," month and",day," days.")         
               

user_month = int(input("Enter the month: "))
user_day = int(input("Enter the day: "))
user_year = int(input("Enter the year: "))

AgeCalculus(0, 0, 0)


##FOSS PRACTICAL 
##This is an open project
##Do contribute

       
