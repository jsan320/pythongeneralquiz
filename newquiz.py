print ("welcome to my program")

playing = input("wanna play a quiz? ")

if playing.lower() != "yes":            # if playing doesnt equal "yes" the program will close itself after printing a message

    print ("Ok, see ya later mate")
    quit()
    
print ("lets play then")



print ("which one is the capital city of the UK? ")

print ("a) Berlin")
print ("b) London")
print ("c) Gujrat")
answer = input ()             # this line is the moment in which the user is expected to write some input for the software to work with

if answer.lower() == "b":
    print ("You're right, obviously")

else:                                  # if the answer doesnt equal "b" the program will print a small text and close itself.
    print ("Incorrect")  

    quit()


print ("which one is the capital city of France? ")

print ("a) Birmingham")
print ("b) London")
print ("c) Paris")
answer = input ()

if answer.lower() == "c":
    print ("You're right, obviously")

else: 
    print ("You're wrong, but sometimes is okay")

    quit ()

# this quiz has been made in Manchester

print ("which one is the capital city of Belgium? ")

print ("a) Brussels")
print ("b) New York")
print ("c) Moscow")
answer = input ()

if answer.lower() == "a":                     # the .lower() filters the users input and makes it all lowercase even if the user typed it in uppercase of both but the answer still needs to be right
    print ("You're right, well done!")

else: 
    print ("You're wrong, get out")           # I like cakes

    quit()
