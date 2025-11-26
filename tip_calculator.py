#print(type(1))
#print(type(True))

#a = "123" # string
#b = int(a) # integer 
#print(type(b))


#name = input("enter your name: ") #str
#length = len (name) #int
#print ("Length in your name " , length)
#print ("Length in your name " + str(length)) #TypeError: can only concatenate str (not "int") to str

#round(3.9) = 4 
#or,
#round(number, 2) = rounds the number to 2 deciimal or reduce
#+=1 adds 1 -=1 substracts 1

#f- string:
#score = 0 # int
#print(f"your score is = {score}") #string and int 

print ("Welcome to a tip calculator.....")
bill = float(input("Enter the total bill: ") )
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
total = bill* tip/100 + bill
people = int(input("Enter how many people to split the bill? " ))
final = total/people 
final_amount = round(final, 2)
print(f"Your total bill with tip would be: {final_amount}")
