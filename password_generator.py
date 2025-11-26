#student_scores = [150,160,120,234,456,765,234,543,654,789,987,98]
#total = sum(student_scores)
#max = 0 
#for score in student_scores:
#    if score> max:
#        max = score
    
#print (max)    


#for number in range(1,101):
#    if number %3 ==0 and number %5 ==0:
 #       print("FIZZBUZZ")   
 #   elif number % 3==0:
 #       print("FIZZ")
 #   elif number %5 ==0:
  #      print ("BUZZ")
  #  else:
  #      print(number)        
 

import random

letters = [
 'a','b','c','d','e','f','g','h','i','j','k','l','m',
 'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

symbols = [
'@', '#', '$', '%', '^', '&', '*', '(', ')',
'-', '_', '+', '=', '{', '}', '[', ']', '|',
'\\', '/', '<', '>', '~', '.', ',', '?', '!', ':', ';'
]



digits = ['0','1','2','3','4','5','6','7','8','9']
password = "" #[]

print("This is a password generator! ")

no_letters= int(input("How many letters you want in your passwords?: "))
no_symbols= int(input("How many symbols do you want?: "))
no_digits = int (input("Enter how many number digits you want?: "))

for i in range(no_letters):
      password += random.choice(letters)
      #password.append(random.choice[letters])
      
for i in range (no_symbols) :
    password += random.choice(symbols) 
    
for i in range (no_digits):
    password += random.choice(digits)  
    
#print(password)    
#password = random.shuffle(password)   
          
print(f'Your secured password is:- "{password}"')

#for char in password:
#.   password+=char
#print(password)