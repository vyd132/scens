import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])

def view():
    global screen
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen,model.color,[500,500,50,50])
    pygame.display.flip()