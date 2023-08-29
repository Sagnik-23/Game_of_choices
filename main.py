# Creator: Unknown GoD
# Date: 01-07-2023
# Description - Text Based Choice game. The name of the game is "The Q Project"
import time
import pygame
def animate(sentence):
    words = sentence.split()
    for word in words:
        print(word, end=" ", flush=True)  # Print with a space as the separator and flush the output
        time.sleep(0.04)  # Delay 
def start_game():#1st paragraph
    name= input("What will be your charecter's name?\n>").capitalize()
    animate('''Recently a new type of alien is seen, and it is taking human forms and using this to camouflage themselves.
They possess deadly powers, and it has started killing people. To stop this alien invasion and to stop the worldwide panic situation the Government of USA has appointed a very secret role to four leaders who are the best in combat and skills and run different universities.''')
    print(end="\n")
    animate('''They chose special students and make their own army to fight with the monsters. The leaders are Marcus Nathan Jonathan Carter, Sezela Kato and William Rotfeld.''')
    print(end="\n")
    animate('''They were spread all over America and trying their best to find a solution for this.''')
    print(end="\n") 
    animate('''This whole project is named ‘THE Q-PROJECT.’\n''')
    time.sleep(1)
    print(name)
start_game()