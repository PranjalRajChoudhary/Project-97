import random;

guess = random.randint(1,9)
chance = 5

while 0<chance<=5:
 number = int(input("Enter a number from 1 to 9"))

 if(guess==number):
    print("Yes! You are correct")
    chance = 5
    break

 elif(guess!=number):
    print("Try one more time")
    chance = chance - 1


if(chance == 0):
    print("Oops!, you lose, number is", number)




   

