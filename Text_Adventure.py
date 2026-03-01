This is a text-driven adventure game. Players will choose a weapon and 
and choose form different possible paths to arrive at one of three endings"""

"""weapon_selection = ["sword", "stick", "knife", "fists"]

#Begin adventure

print("Hello, traveler! What, may I ask, is your name? ")
player_choose_name = input("Enter your name, please... ")
player_name = player_choose_name.lower()

print(f"Hello, " + str(player_choose_name) + "!")
print("It seems we have no time to waste, I'm afraid. ")
print("****DANGER APPROACHES****") #Need to figure out how to loop this message so it flashes like a warnng!
print("Danger seems to be heading this way. You should choose a weapon! ")
print("Which of these weapons will you choose, " + player_choose_name + "?")
print(weapon_selection)

player_weapon_choice = input("Choose one...").lower()
if player_weapon_choice == "sword":
  print("A reliable choice, the sword! ")
elif player_weapon_choice == "stick":
  print("You must have skills that many do not possess...")
elif player_weapon_choice == "knife":
  print("Making things personal, aren't we?")
elif player_weapon_choice == "fists":
  print("Hopefully they will catch them if you throw them.")
else:
  print("You must choose one of the given weapons.")
  print(weapon_selection)
  player_weapon_choice = input("Choose one...").lower() #How do I create a for loop if player chooses wrong?

