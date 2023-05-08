
import pygame

from tools.loader import TIMER, BACK,GREY, putLargeNum,BG1
from tools.utils import rounded_rect

# This shows the screen
def showScreen(win, sel, sel2):
    win.fill((255, 255, 255))
    win.blit(BG1,(0,0))
    
    win.blit(TIMER.HEAD, (100, 7))
    win.blit(BACK, (460, 0))

    
    pygame.draw.rect(win, GREY, (110, 270, 60, 25))    
   
    for cnt, i in enumerate(TIMER.TEXT):
        y = 75 + cnt * 18
        win.blit(i, (20, y))
        
    for i in range(6):
        pygame.draw.rect(win, (255, 255, 255), (110 + 40*i, 200, 28, 23), 3)
        
        
    pygame.draw.rect(win, (50, 100, 150), (110 + 40*sel, 200, 28, 23), 3) 
       
    pygame.display.update()

# This is the main function, called from main menu
def main(win, load):
    
    
    sel = sel2 = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, sel, sel2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    return 1
                
                if 110 < x < 170 and 270 < y < 295:
                    if sel == 0:
                        temp = (30 * 60 * 1000,)*2
                    if sel == 1:
                        temp = (15 * 60 * 1000,)*2
                    if sel == 2:
                        temp = (10 * 60 * 1000,)*2
                    if sel == 3:
                        temp = (5 * 60 * 1000,)*2
                    if sel == 4:
                        temp = (3 * 60 * 1000,)*2
                    if sel == 5:
                        temp = (1 * 60 * 1000,)*2
                    return sel2, temp
                
                for i in range(6):
                    if 110 + 40*i < x < 138 + 40*i and 200 < y < 223:
                        sel = i
                        break
                        
                
