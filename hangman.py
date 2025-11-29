import random

words = ["abra", "kaoe", "gusdhhu"]

guess = random.choice(words)
print(guess)

new_guess = len(guess)

holder = ""
for i in range(new_guess):
    holder+="_"
print(holder)

display = ""
user = input("Guess a letter: ").lower()
for i in guess:
   if user == i:
       display+= i
   else:
       display += "_"
       
print(display)       
    

