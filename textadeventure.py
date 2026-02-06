print("hello adventurer")
print("welcome to the world  of text adventures")
hascup = False
def game_over():
    print("Wrong choice.")
    print("Game over.")
    exit()
def game_won():
    print("hurray you made all the right choices")
    print("you win and this time a game over your happy to see")
    exit()

print("You wake up in a room.")

print("What do you do?")
print("1)examine your surroundings")
print("2) look for an exit")

choice = input("Enter 1 or 2: ")

if choice == "1":
    print("you see a door and a table with some cups and a bottle")
elif choice == "2":
    print("you look around but slip on a banana peel falling to your death")
    game_over()
else:
    print("You freeze and do nothing."
          )
    


print("What do you do?")
print("1)go toward the door")
print("2)go toward the bottle and cups")

choice = input("Enter 1 or 2: ")

if choice == "1":
    print("you go toward the door. it is locked")
elif choice == "2":
    print("you go toward the bottle and cups. O wait I meant bottles and feroicious ducks which attack you ")
    game_over()
else:     
    print("You freeze and do nothing.")
    game_over()

    
    
    
    print("What do you do?")
print("1)look for a key")
print("2)try and force the door")
print("3)go toward the cups and bottles")

choice = input("Enter 1 or 2 or 3: ")

if choice == "1":
    print("you bend over but realize that gojo is behind you")
    game_over()
elif choice == "2":
    print(" you push agaist the door but it gives way stabbing you with the handle")
    game_over()
elif choice == "3":
    print("you go toward the bottles and cup.The key is the bottle")
else:     
    print("You freeze and do nothing.")
    game_over()



    print("What do you do?")
print("1)pour liquid in the cups")
print("2)pour it out on the floor")
print("3)pour liquid on the door")

choice = input("Enter 1 or 2 or 3: ")

if choice == "1":
    print("you pour it into the cups not realizing they react with each other making poisin gas")
    game_over()
elif choice == "2":
    print(" there is a drain on the floor and the key slip through. you sit they knowing your only chance of escape slip through your fingers ")
    game_over()
elif choice == "3":
    print("the liquid turn out to be acid and melt the door down")
else:     
    print("You freeze and do nothing.")
    game_over()
      
      
    print("What do you do?")
print("1)go through the door")
print("2)go and collect the cups")
print("3)look around the room for more loot")

choice = input("Enter 1 or 2 or 3: ")

if choice == "1":
    print("your shoes disslive from the acid as the rest of the body since it did not dry up")
    game_over()
elif choice == "2":
    print("you collect cup before leaving the room")
    game_over()
elif choice == "3":
    print("you look around but forget about the banana peel form earleir")
    game_over()
else:     
    print("You freeze and do nothing.")
    game_over()
    
    
    print("What do you do?")
print("1)examine next room")
print("2)take a leak")
print("3)go back and rest")
print("4)examine the cup you just took")

choice = input("Enter 1 or 2 or 3 or 4: ")

if choice == "1":
    print("you examine the room you see mutiple pillar with a deep pit and a door on the other side")
elif choice == "2":
    print("you take a leak into the deep pit")
elif choice == "3":
    print("you go back and take a nap")
elif choice == "4":
    print("you examine the cup and realize you can make a bridge from them")
    hascup=True
else:     
    print("well well well we know what happens now")
    game_over()

if hascup == True:
    print("you cross the pit with the cups")
    print("what do you do next")
    print("1)try and pickup the cups for later")
    print("2)go to the next door")
    print("choose 1 or 2")
    choice = input("Enter 1 or 2 ")
    if choice == "1":
        print("you try to pick up the cups but trap yourself. don't know what you were thinking")
    elif choice == "2":
      hascup=False
    





