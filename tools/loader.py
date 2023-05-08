

import os.path
import pygame

# Initialize pygame.font module and load the font file.
pygame.font.init()
FONT = os.path.join("res", "Moonrising.ttf")
FONT1 = os.path.join("res", "MoonrisingItalic.ttf")
FONT2 = os.path.join("res", "Asimov.otf")

# Load different sizes of the font.
head = pygame.font.Font(FONT1, 80)
large = pygame.font.Font(FONT1, 27)
medium = pygame.font.Font(FONT, 27)
small = pygame.font.Font(FONT2, 27)
vsmall = pygame.font.Font(FONT2, 17)

# Define RGB color constants for use.
BLACK = (255, 255, 255)
GREY = (180, 180, 180)
WHITE = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 20, 20)

# Define a few constants that contain loaded texts of numbers and chararters.
NUM = [vsmall.render(str(i), True, WHITE) for i in range(10)]
LNUM = [small.render(str(i), True, WHITE) for i in range(10)]
BLNUM = [small.render(str(i), True, BLACK) for i in range(10)]
SLASH = vsmall.render("/", True, WHITE)
COLON = vsmall.render(":", True, WHITE)

# This function displays a number in a position, very small sized text used.
def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM[int(i)], (pos[0] + (cnt * 9), pos[1]))

# This function displays a number in a position, Small sized text used.
def putLargeNum(win, num, pos, white=True):
    for cnt, i in enumerate(list(str(num))):
        if white:
            win.blit(LNUM[int(i)], (pos[0] + (cnt * 14), pos[1]))
        else:
            win.blit(BLNUM[int(i)], (pos[0] + (cnt * 14), pos[1]))

# This function displays the date and time in a position on the screen.
def putDT(win, DT, pos):
    var = DT.split()
    date = var[0].split("/")
    time = var[1].split(":")

    for cnt, num in enumerate(map(lambda x: format(int(x), "02"), date)):
        putNum(win, num, (pos[0] + 24 * cnt - 5, pos[1]))

    win.blit(SLASH, (pos[0] + 13, pos[1]))
    win.blit(SLASH, (pos[0] + 35, pos[1]))

    for cnt, num in enumerate(map(lambda x: format(int(x), "02"), time)):
        putNum(win, num, (pos[0] + 24 * cnt, pos[1] + 21))

    win.blit(COLON, (pos[0] + 20, pos[1] + 21))
    win.blit(COLON, (pos[0] + 44, pos[1] + 21))

# This splits a string at regular intervals of "index" characters
def splitstr(string, index=57):
    data = []
    while len(string) >= index:
        data.append(string[:index])
        string = string[index:]
    data.append(string)
    return data

# Defined important globals for loading background image .
BGSPRITE = pygame.image.load(os.path.join("res", "img", "background1.jpg"))
PSPRITE = pygame.image.load(os.path.join("res", "img", "piecesprite.png"))
BG1 = pygame.image.load(os.path.join("res", "img", "inbackgrnd1.jpg"))

# Load global image for back
BACK = pygame.image.load(os.path.join("res", "img", "back.png"))

class CHESS:
    PIECES = ({}, {})
    for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
        for side in range(2):
            PIECES[side][ptype] = PSPRITE.subsurface((i * 50, side * 50, 50, 50))

    CHECK = small.render("CHECK!", True, BLACK)
    STALEMATE = small.render("STALEMATE!", True, BLACK)
    CHECKMATE = small.render("CHECKMATE!", True, BLACK)
    LOST = small.render("LOST", True, BLACK)
    CHOOSE = small.render("CHOOSE:", True, BLACK)
    SAVE = small.render("Save Game", True, BLACK)
    UNDO = small.render("Undo", True, BLACK)

    MESSAGE = (
        small.render("Do you want to quit", True, WHITE),
        small.render("this game?", True, WHITE),
    )
    
    MESSAGE2 = (
        small.render("Game saved. Now do", True, WHITE),
        small.render("you want to quit?", True, WHITE),
    )

    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)
    MSG = vsmall.render("Game will be saved with ID", True, WHITE)
    SAVE_ERR = vsmall.render(" Limit Exeeded", True, WHITE)

    TURN = (
        small.render("Others turn", True, BLACK),
        small.render("Your turn", True, BLACK),
    )

    DRAW = small.render("Draw", True, BLACK)
    RESIGN = small.render("Quit", True, BLACK)
    
    TIMEUP = (
        vsmall.render("Time Up!", True, WHITE),
        vsmall.render("Technically the game is over, but you", True, WHITE),
        vsmall.render("can still continue if you wish to - :)", True, WHITE),
    )
    
    OK = small.render("Ok", True, WHITE)
    COL = small.render(":", True, BLACK)

class MAIN:
    HEADING = head.render("Chess.py", True, BLACK)
    VERSION = vsmall.render("Version 3.2", True, BLACK)
    ICON = pygame.image.load(os.path.join("res", "img", "icons.png"))
    BANNER = pygame.image.load(os.path.join("res", "img", "682.png"))
    pygame.transform.scale(BANNER,(230,55))
    
    BG=BGSPRITE
    SINGLE = medium.render("Single", True, BLACK)
    MULTI = medium.render("Multi", True, BLACK)
    ONLINE = medium.render("Online", True, BLACK)
    
    PREF = medium.render("Setting", True, BLACK)
    

    SINGLE_H = medium.render("Single", True, GREY)
    MULTI_H = medium.render("Multi", True, GREY)
    ONLINE_H = medium.render("Online", True, GREY)
    
    PREF_H = medium.render("Setting", True, GREY)
    

class PREF:
    HEAD = large.render("Settings", True, WHITE)

    
    FLIP = medium.render("Flip screen", True, WHITE)
    CLOCK = medium.render("Show Timer", True, WHITE)
    SLIDESHOW = medium.render("Slideshow", True, WHITE)
    MOVE = medium.render("Moves", True, WHITE)
    UNDO = medium.render("Allow undo", True, WHITE)

    COLON = medium.render(":", True, WHITE)

    TRUE = medium.render("True", True, WHITE)
    FALSE = medium.render("False", True, WHITE)
    
    BSAVE = medium.render("Save", True, WHITE)
    
    PROMPT = (
        vsmall.render("Are you sure you want to leave?", True, WHITE),
        vsmall.render("Any changes will not be saved.", True, WHITE),
    )

    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)

class ONLINE:
    ERR = (
        vsmall.render("Attempting to connect to server..", True, WHITE),
        vsmall.render("[ERR 1] Couldn't find the server..", True, WHITE),
        vsmall.render("[ERR 2] Versions are incompatible..", True, WHITE),
        vsmall.render("[ERR 3] Server is full (max = 10)..", True, WHITE),
        vsmall.render("[ERR 4] The server is locked...", True, WHITE),
        vsmall.render("[ERR 5] Unknown error occured...", True, WHITE),
        vsmall.render("You got disconnected from server..", True, WHITE),
    )
    GOBACK = vsmall.render("Go Back", True, WHITE)
        
    EMPTY = small.render("No one's online, you are alone.", True, WHITE)

    LOBBY = large.render("Online Lobby", True, WHITE)
    LIST = medium.render("List of Players", True, WHITE)
    PLAYER = small.render("Player", True, WHITE)
    DOT = small.render(".", True, WHITE)

    ACTIVE = small.render("ACTIVE", True, GREEN)
    BUSY = small.render("BUSY", True, RED)
    REQ = small.render("Send Request", True, WHITE)
    YOUARE = medium.render("You Are", True, WHITE)
    
    ERRCONN = vsmall.render("Unable to connect to that player..", True, WHITE)

    REFRESH = pygame.image.load(os.path.join("res", "img", "refresh.png"))

    REQUEST1 = (
        vsmall.render("Please wait for the other player to", True, WHITE),
        vsmall.render("accept your request. Game will begin", True, WHITE),
        vsmall.render("shortly. You will play as white", True, WHITE),
    )
    REQUEST2 = (
        vsmall.render("Player", True, WHITE),
        vsmall.render("wants to play with you.", True, WHITE),
        vsmall.render("Accept to play. You will play as black", True, WHITE),
    )

    DRAW1 = (
        vsmall.render("Sent a request to your opponent for", True, WHITE),
        vsmall.render("draw, wait for reply.", True, WHITE),
    )

    DRAW2 = (
        vsmall.render("Your opponent is requesting for a", True, WHITE),
        vsmall.render("draw, please reply.", True, WHITE),
    )
    
    POPUP = {
        "quit": vsmall.render("Opponent got disconnected", True, WHITE),
        "resign": vsmall.render("The opponent has resigned", True, WHITE),
        "draw": vsmall.render("A draw has been agreed", True, WHITE),
        "end": vsmall.render("Game ended, opponent left", True, WHITE),
        "abandon": vsmall.render("Opponent abandoned match", True, WHITE),
    }

    NO = small.render("NO", True, WHITE)
    OK = small.render("OK", True, WHITE)

class ONLINEMENU:
    HEAD = large.render("Online", True, WHITE)
    with open(os.path.join("res", "texts", "online.txt")) as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    CONNECT = small.render("Connect", True, WHITE)

class SINGLE:
    HEAD = large.render("Singleplayer", True, WHITE)
    SELECT = pygame.image.load(os.path.join("res", "img", "select.jpg"))
    CHOOSE = small.render("Choose:", True, WHITE)
    START = small.render("Start Game", True, WHITE)
    
    
    with open(os.path.join("res", "texts", "single1.txt")) as f:
        PARA1 = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]
    OK = vsmall.render("Ok", True, WHITE)
    NOTNOW = vsmall.render("Not Now", True, WHITE)
 
class TIMER:
    HEAD = large.render("Timer Menu", True, WHITE)
    
    YES = small.render("Yes", True, WHITE)
    NO = small.render("No", True, WHITE)
    
    PROMPT = vsmall.render("Do you want to set timer?", True, WHITE)

    with open(os.path.join("res", "texts", "timer.txt"), "r") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]
    

pygame.font.quit()
