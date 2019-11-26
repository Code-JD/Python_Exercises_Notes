# import sys 
# import random

# ans = True

# while ans:
#     question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
    
#     answers = random.randint(1,8)
    
#     if question == "":
#         sys.exit()
    
#     elif answers == 1:
#         print("It is certain")
    
#     elif answers == 2:
#         print("Outlook good")
    
#     elif answers == 3:
#         print("You may rely on it")
    
#     elif answers == 4:
#         print("Ask again later")
    
#     elif answers == 5:
#         print("Concentrate and ask again")
    
#     elif answers == 6:
#         print("Reply hazy, try again")
    
#     elif answers == 7:
#         print("My reply is no")
    
#     elif answers == 8:
#         print("My sources say no")

# import random
# import sys
# def magic_8ball():
#     x = raw_input("What is your question? enter to quit. ")
# Eightball_list = ["It is certain", "Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
# if x==" ":
#     print("exiting...")
# else:
#     print(random.choice(Eightball_list))
# magic_8ball()

# ans = True

# while ans:
#     question = input("Ask the magic 8 ball a question: (press enter to quit) ")

# answers = random.randint(1,8)

# if question == "":
#     sys.exit()

# elif answers == 1:
#     print "It is certain"

# elif answers == 2:
#     print ("Outlook good")

# elif answers == 3:
#     print ("You may rely on it")

# import sys

# import random

# ans = True

# while ans:

#     question = input("Ask the magic 8 ball a question: (press enter to quit) ")

# answers = random.randit(1,8)

# if question ==(""):

#     sys.exit()

# elif answers == 1:

#     print("It is certain")

# elif answers == 2:

#     print("outlook good")

# elif answers == 3:

#     print("You may rely on it")

# elif answers == 4:

#     print("Ask again later")

# elif answers == 5:

#     print("Concentrate and try again")

# elif answers == 6:

#     print("Reply hazy, try again")

# elif answers == 7:

#     print("My reply is no")

# elif answers == 8:

#     print("My sources say no")


# import random
# import sys
# play_again = 'yes'

# while play_again == 'yes':
#     str(input("Welcome to the Magic 8-Ball. Enter your question: ")).lower()
    
    
#     response = random.randint(0,20)
    
#     if response == 1:
#         print("Not just no, hell no!")
#     elif response == 2:
#         print("Sure thing.")
#     elif response == 3:
#         print("Don't count on it.")
#     elif response == 4:
#         print("Maybe not.")
#     elif response == 5:
#         print("Count on it.")
#     elif response == 6:
#         print("The Universe says maybe.")
#     elif response == 7:
#         print("I don't see why not.")
#     elif response == 8:
#         print("The future looks good for you.")
#     elif response == 9:
#         print("That's for sure.")
#     elif response == 10:
#         print("Maybe.")
#     elif response == 11:
#         print("There's a chance.")
#     elif response == 12:
#         print("Certainly!")
#     elif response == 13:
#         print("Keep doing what you're doing and it'll happen.")
#     elif response == 14:
#         print("Not over my dead 8 Ball.")
#     elif response == 15:
#         print("No.")
#     elif response == 16:
#         print("Yes.")
#     elif response == 17:
#         print("All depends on if you've been good for Santa this year.")
#     elif response == 18:
#         print("Not in this lifetime.")
#     elif response == 19:
#         print("Someday, but not today.")
#     elif response == 20:
#         print("Right after you hit the lottery.")
#     else:
#         print("Not a valid question!")

#     play_again = str(input("Would you like to ask a question? yes/no ")).lower()
#     if play_again == 'no':
#         print("Goodbye! Thanks for playing!")
#         sys.exit()
#-----------------------------------------------------------

import sys
import random

ans = True

while ans:
    question = input("Ask the Magic 8 ball a question (press enter to quit) ")

    answers = random.randint(1, 9)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("It is certian")
    
    elif answers == 2:
        print("Outlook is good")

    elif answers == 3:
        print("You may rely on it")

    elif answers == 4:
        print("Never")

    elif answers == 5:
        print("Not likely")

    elif answers == 6:
        print("Ask again later")

    elif answers == 7:
        print("I think you are onto something, but ask again")

    elif answers == 8:
        print("Not happening this year, maybe next year")

    elif answers == 9:
        print("Better off sticking to your day job")