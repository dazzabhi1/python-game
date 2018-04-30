import random

number = random.randint(1,10)
tries=0
win=False

uname= input("Hello, What is your username ?")

print("Hello", uname + ".",)

question=input("Would you like to play the game ? [Y/N]")
if question == "N":
    print("oh...okay")

elif question =="Y":
    while True:
    	guess=int(input("Have a guess..."))
    	tries = tries + 1
    	if guess == number :
   	    	break
    	elif guess > number:
   	        print("Guess lower......")
    	elif guess <  number:
   			print("Guess higher....")

    print("Congrats, you guessed  correctly.The number was indeed()" , number)
    print("it had taken you tries()",tries)

else:
	print("Worng input!")