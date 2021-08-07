print("welcome to my general knowledge quiz ")

playing = input("do you want to play? ")

if playing.lower() != "yes":   # .lower() makes all the input lowercase, also .upper() makes all the input uppercase
        quit()
print("okay lets play!")
score = 0
answer = input("how long is a decade? ")

if answer.lower() == "10 years":   
 print("Correct!")
 score += 1
else:
 print("Incorrect!")
        
answer = input("which country is the most populated? ")

if answer.lower() == "china":   
 print("Correct!")
 score += 1
else:
 print("Incorrect!")


answer = input("which company made the iphone? ")

if answer.lower() == "apple":
 print("Correct!")
 score += 1
else:
 print("Incorrect!")
 

answer = input("Which language are we speaking? ")

if answer.lower() == "english":
 print("Correct!")
 score += 1
else:
 print("Incorrect!")

        
answer = input("which is the biggest country in the world? ")

if answer.lower() == "russia":
 print("Correct!")
 score += 1
else:
 print("Incorrect!")


 print("You got " + str(score) + " questions correct!")
 print("You got " + str((score/5) * 100) + " % of the questions right!")               
