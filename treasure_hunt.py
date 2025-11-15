print("Welcome to roller-coaster")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("Have fun! ")
    
    age = int(input("Enter your age: "))
    
    if age <= 12:
        bill = 5
        print("You are charged $5!")
        
    elif age <=18:
        bill = 7
        print("You are charged $7")    
    else:
        bill = 14
        print ("You are charged $14!")    
    
    photos = input ("Do you want to have a photo take? Type 'Y' for Yes and 'N' for No: ")
    if photos == "Y" or "y":
        bill += 3
    
    print (f"Your total bill is {bill}")     
else:
    print("Sorry safety issue! ")
    
    


#modulo operator %     : remainder

# EVEN - ODD!
number = int(input("Enter any whole number: "))
even = number % 2. # if remainder = 0

if even == 0:
    print ("EVEN")
else:
    print("ODD")    
    
    
    
    
    


        
