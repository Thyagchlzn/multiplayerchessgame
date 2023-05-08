
import sys  
import pygame

import chess
import menus
from tools.loader import MAIN


# This is a non-important bit of code. Flush stdout - useful incase external
# programs are calling this application.
sys.stdout.flush()

# Some initialisation
pygame.init()
clock = pygame.time.Clock()

# Initialise display, set the caption and icon. Use SCALED if on pygame 2.
if pygame.version.vernum[0] >= 2:
    win = pygame.display.set_mode((500, 500), pygame.SCALED)
else:
    win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("CHESS")
pygame.display.set_icon(MAIN.ICON)

# Coordinates of buttons in rectangle notation.
sngl = (230, 140, 220, 40)
mult = (230, 200, 200, 40)
onln = (230, 260, 120, 40)
pref = (230, 320, 200, 40)


# This is the function that displays the main screen.
# "prefs" value is passed, prefs is a list of all the user settings
def showMain(prefs):
    
    global cnt, img

    # First, blit background image (based on the img variable)
    win.blit(MAIN.BG, (0, 0))

    
    # Now blit all the texts onto the screen one by one
    win.blit(MAIN.HEADING, (80, 20))
    pygame.draw.line(win, (255, 255, 255), (80, 100), (130, 100), 4)
    pygame.draw.line(win, (255, 255, 255), (165, 100), (340, 100), 4)
   
    win.blit(MAIN.BANNER,(230-10,130))
    win.blit(MAIN.BANNER,(230-10,190))
    win.blit(MAIN.BANNER,(230-5,250))
    win.blit(MAIN.BANNER,(230-10,310))
    
    
    
    
    win.blit(MAIN.SINGLE, sngl[:2])
    win.blit(MAIN.MULTI, mult[:2])
    win.blit(MAIN.ONLINE, onln[:2])
    
    win.blit(MAIN.PREF, pref[:2])
    
# Initialize a few more variables
cnt = 0
img = 0
run = True

# Load the settings of the player
prefs = menus.pref.load()


while run:
    # Start the game loop at 30fps, show the screen every time at first
    clock.tick(30)
    showMain(prefs)

    # We need to get the position of the mouse so that we can blit an image
    # on the text over which the mouse hovers
    x, y = pygame.mouse.get_pos()

    if sngl[0] < x < sum(sngl[::2]) and sngl[1] < y < sum(sngl[1::2]):
        win.blit(MAIN.SINGLE_H, sngl[:2])

    if mult[0] < x < sum(mult[::2]) and mult[1] < y < sum(mult[1::2]):
        win.blit(MAIN.MULTI_H, mult[:2])

    if onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
        win.blit(MAIN.ONLINE_H, onln[:2])

    if pref[0] < x < sum(pref[::2]) and pref[1] < y < sum(pref[1::2]):
        win.blit(MAIN.PREF_H, pref[:2])
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User has clicked somewhere, determine which button and
            # call a function to handle the game into a different window.
            x, y = event.pos

            if sngl[0] < x < sum(sngl[::2]) and sngl[1] < y < sum(sngl[1::2]):
                #sound.play_click(prefs)
                ret = menus.splayermenu(win)
                if ret == 0:
                    run = False
                elif ret != 1:
                    if ret[0]:
                        run = chess.mysingleplayer(win, ret[1], prefs)
                    else:
                        run = chess.singleplayer(win, ret[1], ret[2], prefs)

            elif mult[0] < x < sum(mult[::2]) and mult[1] < y < sum(mult[1::2]):
                #sound.play_click(prefs)
                ret = menus.timermenu(win, prefs)
                if ret == 0:
                    run = False
                elif ret != 1:
                    run = chess.multiplayer(win, ret[0], ret[1], prefs)

            elif onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
                #sound.play_click(prefs)
                ret = menus.onlinemenu(win)
                if ret == 0:
                    run = False
                elif ret != 1:
                    run = chess.online(win, ret[0], prefs, ret[1])
       
            elif pref[0] < x < sum(pref[::2]) and pref[1] < y < sum(pref[1::2]):
                #sound.play_click(prefs)
                run = menus.prefmenu(win)
                
                prefs = menus.pref.load()
                

    # Update the screen every frame
    pygame.display.flip()


pygame.quit()
