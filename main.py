#Choose Your Own Adventure: "The Office" Party Edition

#Do you love the hit TV show 'The Office?' Have you ever wondered what it would be like to join one of their classic office parties?  Well, the PPC (Party Planning Committee) is excited to bring the party to you!  You can choose from attending an office Christmas party, a Halloween party, and/or a birthday party.  If you're  not feeling like partying, you can always pick to sell paper too. Enjoy!

import time 

##Introduction and gathering the user's name as a global variable:
print("You have just been transfered to the Scranton Branch of Dunder Mifflin!")
print("")
time.sleep(1.5)

name = input("Michael Scott: Ah! Welcome to Scranton.  What is your name? ")
print("")
name = name.title()

##Defining functions and a dictionary to be used in run_program function later: 
office_costumes = {
      "Gabe": "Lady Gaga",
      "Michael": "MacGruber",
      "Kelly": "Snooki",
      "Oscar": "a Rational Consumer",
      "Angela": "a Penguin",
      "Jim": "Popeye",
      "Pam": "Olive Oyl",
    }

def delayed_dots(n):
  dots = 0
  while dots < n:
    print(".")
    time.sleep(.3)
    dots = dots + 1

def intro():
  print(f"Michael Scott: Ah. I knew that, {name}!  I am Michael Scott, and I am your leader.")
  print("")
  print("As it turns out, you picked the right day to join because there is going to be a party! And you know... there ain't no party like a Scranton party 'cause a Scranton party don't stop!")
  print("")
  print("Want to know the best PART(y)? You get to pick what we're celebrating!  You can choose between...")
  print("")

def ghosts():
  print("")
  print("  __/ \__________")
  print(" (:o   __________")
  print("    \ / ")
  print("")
  time.sleep(.5)
  print("      __/ \__________")
  print("     (:)   __________")
  print("        \ / ")
  print("")
  time.sleep(.5)
  print("          __/ \__________")
  print("         (:x   __________")
  print("            \ / ")
  time.sleep(.5)
  print("")

### To print Dictionary key:value pairs, use a for loop to traverse through the key:value pairs, and use print statement to print them. dict.items() returns the iterator for the key:value pairs and returns key, value during each iteration. -https://pythonexamples.org/python-print-dictionary/#3 ### 
def print_costume_list(office_costumes):
  for i, (key,value) in enumerate(office_costumes.items()):
    print(i, "- ", key, "as", value)

def user_choice():
  while True:
    print("PARTY CHOICES:")
    print("A: A birthday party")
    print("B: A Halloween party")
    print("C: A Christmas party")
    print("D: No party for me. I just want to sell paper and be left alone...")
    print("")
    party_type = input("What will you choose? (Type A, B, C, or D): ")
    party_type = party_type.upper()
    print("")

  # #IF the user chooses a BIRTHDAY PARTY...
    if party_type == "A":
      print(f"Let's celebrate this birthday Scranton style, {name}!")
      print("")
      time.sleep(.75)
      print("Uh oh...")
      time.sleep(1)
      
      delayed_dots(5)
  
      print("It seems that the usual Party Planning Committee is sitting this one out, and Michael has left DWIGHT and JIM in charge to plan your birthday celebration!")
      time.sleep(3)
      delayed_dots(5)
  
      print("You walk into the conference room and see brown and gray balloons that are only slightly filled up hanging from the ceiling, and there is a sign on the wall that reads:")
      print("IT IS YOUR BIRTHDAY.")
      time.sleep(4)
      delayed_dots(5)
  
      print("Next, Dwight and Jim bring out a cake with one Chicklet in the middle. What’s the theme you may be wondering?  Well… that’s the fun part, Jim says. The Chicklet is either a pillow or a TV, and you get to pick if you want to take a nap or watch TV.")
      print("")
  
      while True:
        birthday_choice = input("Would you rather take a nap or watch TV? (Type Nap or TV): ")
        birthday_choice = birthday_choice.title()
  
        if birthday_choice == "Nap":
          print("")
          print("***Enjoy some sweet birthday dreams while napping underneath the table in the conference room!***")
          print("")
          time.sleep(1.5)
  
          sleep_z = 0
          while sleep_z < 5:
            print("Zzz")
            time.sleep(.5)
            sleep_z = sleep_z + 1
  
          print("")
          print("We hope you enjoyed your birthday at Dunder Mifflin!")
          print("")
          print("What would you like to do now?")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  
          break
  
        elif birthday_choice == "Tv":
          print("")
          show_choice = input("Have fun watching TV! We hear there's this really cool show called The Office... What show are you going to watch?: ")
          show_choice = show_choice.title()
          print("")
          print(f"Enjoy watching {show_choice}!")
          print("")
          time.sleep(2)
          print("We hope you enjoyed your birthday at Dunder Mifflin!")
          print("")
          print("What would you like to do now?")
          break
  
        else:
          print("")
          print("Invalid response. Please respond with either Nap or TV.")
          
  #IF the user chooses a HALLOWEEN PARTY...
    elif party_type == "B":
      ghosts()
      print("Boo! It’s Halloween, and the office is hosting a costume contest! Pam has scored the best prize this year… the one and only Scranton/Wilkes-Barre Coupon Book worth over $15,000 in savings!")
      print("")

      user_costume = input("What's your costume going to be for the contest? ")
      office_costumes[name] = user_costume

      delayed_dots(5)
      print("Here are the costumes in the contest: ")
      print("")
      print_costume_list(office_costumes)
      print("")

      while True: 
        contest_winner = input("Out of the following contestants, who do you think has the best costume?  (Respond with a contestant's name--and you CANNOT vote for yourself!): ")
        contest_winner = contest_winner.title()
        print("")
    
        if contest_winner == "Oscar":
          print("The office staff agrees with you, and Oscar won the contest!")
          print("")
          break
      
        elif (contest_winner == "Gabe") or (contest_winner == "Michael") or (contest_winner == "Kelly") or (contest_winner == "Angela") or (contest_winner == "Jim") or (contest_winner == "Pam"):
          print(f"The votes are in, and while {contest_winner} did have a great costume, Oscar won the costume contest and the Scranton coupon book!")
          print("")
          break
      
        else:
          print("Invalid Response. Please respond with a contestant's name.")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          
      time.sleep(1.5)
      delayed_dots(4)
      print("We hope you enjoyed celebrating Halloween at Dunder Mifflin!")
      time.sleep(1)
      print("")
      print("What would you like to do now?")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #IF the user chooses a CHRISTMAS PARTY...
    elif party_type == "C":
      print(
        "It’s Christmas-time in Scranton, PA, and the office employees are playing Secret Santa!"
      )
      time.sleep(2)
      delayed_dots(3)
      print("Everything is going great until Michael gets a homemade oven mitt that he doesn’t like, and he changes the game to Yankee Swap...")
      time.sleep(3)
      delayed_dots(3)
      print("In Yankee Swap, you either get to pick a new gift or trade gifts with someone else.")
      time.sleep(2)
      delayed_dots(3)
      print("Here are the gifts so far:")
      print("     A: A homemade oven mitt")
      print("     B: A teapot")
      print("     C: A video iPod")
      print("     D: A poster with babies playing jazz")
      print("     E: Paintball pellets and lessons from Dwight")
      print("")
  
      while True:
        user_gift = input(
          "Would you like to open a new gift (type F), or would you like to steal someone else's gift? (Respond with A, B, C, D, or E that matches the above gift you'd like to steal): "
        )
        user_gift = user_gift.upper()
        if user_gift == "A":
          print("")
          print(
            "Have fun baking lots of yummy cookies with your new homemade oven mitt knit by Phyllis!"
          )
          break
        elif user_gift == "B":
          print("")
          print(
            "Nice choice! Pro-tip... the teapot can also be used as a Netipot!")
          print("")
          time.sleep(2)
          print(
            "When you go to open it up though, you find inside a funny picture of Jim as a kid and a hot sauce packet... Turns out this gift was an inside joke for Pam!"
          )
          break
        elif user_gift == "C":
          print("")
          print(
            "Of course... the video iPod is worth like $400! Why would you not choose it? Enjoy!"
          )
          break
        elif user_gift == "D":
          print("")
          print("The poster of babies playing jazz music.  Cute! You and Angela will probably be or already are great friends... do you like cats too?")
          break
        elif user_gift == "E":
          print("")
          print("Nice choice!  The next day, you receive a text from Dwight that reads: 'Mandatory paintball. Parking lot.  Noon today.'  We hope you're ready for this!")
          break
        elif user_gift == "F":
          print("")
          print("Wahoo! Exciting... you unwrap the gift, and it's a custom nameplate for Kelly's desk... ")
          time.sleep(1.5)
          print("Stanley says that he got it for Kelly... there is a general sense of resentment towards Michael in the office for switching Secret Santa to Yankee Swap.  Alas... you're now the new owner of a Kelly nameplate!")
          break
        else:
          print("Invalid input.  Please respond with A, B, C, D, E, or F.")
          print("")

      print("")
      time.sleep(3)
      print("We hope you enjoyed celebrating Christmas at Dunder Mifflin!")
      time.sleep(1)
      print("")
      print("What would you like to do now?")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif party_type == "D":
      print("Have fun selling paper. We'll see you on the flippity flip!")
      break
  
    #IF the user types anything else
    else:
      print("Invalid response. Please respond with A, B, C, or D.")
      print("")
  

def play_game():
  intro()
  user_choice()

play_game()



      