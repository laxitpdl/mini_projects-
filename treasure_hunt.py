#print("Welcome to roller-coaster")
#height = int(input("Enter your height in cm: "))

#if height >= 120:
#    print("Have fun! ")
    
#    age = int(input("Enter your age: "))
    
#    if age <= 12:
#        bill = 5
#        print("You are charged $5!")
        
#    elif age <=18:
 #       bill = 7
 #       print("You are charged $7")    
  #  else:
   #     bill = 14
    #    print ("You are charged $14!")    
    
    #photos = input ("Do you want to have a photo take? Type 'Y' for Yes and 'N' for No: ")
    #if photos == "Y" or "y":
     #   bill += 3
    
    #print (f"Your total bill is {bill}")     
#else:
 #   print("Sorry safety issue! ")
    
    


#modulo operator %     : remainder

# EVEN - ODD!
#number = int(input("Enter any whole number: "))
#even = number % 2. # if remainder = 0

#if even == 0:
#    print ("EVEN")
#else:
 #   print("ODD") 
    
    

#print ("Welcome to python pizza Deliveries! ")
#size = input ("What size pizza do you want? 'S' for small, 'M' for medium or 'L' for large: ")
#pineapple = input ("Do you want pineapple on your pizza? 'Y' for yes or 'N' for no: ")
#cheese = input ("Do you want extra cheese on your pizza? 'Y' for yes or 'N' for no: ")

#bill = 0

#if size == 's':
#    bill += 15
#elif size == 'm':
#    bill += 20
#elif size == 'l':
#    bill += 25
#else:
#    print ("Enter S, M or L: ")
       

#if pineapple == 'y':
 #   if size == 's':
  #      bill += 2
#    else:
   #     bill += 3    
        
#if cheese == 'y':
#    bill += 1
    
#print (f"Your total bill is ${bill}")    
        
 

# logical operators: and or not  

print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             |   _/ \_     <_o#\__/#o_>     _/ \_   |
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\.../.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`


''')
print("Hello, traveler are you lost! or are you in right place!\nWelcome to Treasure island!\nYour journey begins now be ready! ")
way = input ("Now you are standing on the cross road. Where do you want to go?\nType 'left' or 'right': ").lower()
if way == 'left':
    lake = input("You are safe! Now you've come to a lake. Far away in middle of the lake there is an island...\nType 'wait' to wait for a boat or 'swim' if you want to swim across!: " ).lower()
    if lake == 'wait':
        door = input ("Well done stranger! now you stand at the final door one of these door has fortune and other has death choose wisely! Type 'red' for red door, 'yellow' for yellow door and 'blue' for blue door!: ").lower()
        if door == 'yellow':
            print("You did it you found the treasure! ")
        elif door == 'red':
            print ("Dead! on lava.. GAME OVER!")
        elif door == 'blue':
            print ("Hunted by demons... GAME OVER!")
        else:
            print("Invalid option...")
    else: 
        print ("Bad idea you were eaten by hungry sharks!.. GAME OVER!")                
else:
    print("You are shot by smugglers! Try next time.. GAME OVER!")    
   


        
