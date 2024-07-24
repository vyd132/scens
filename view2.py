import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
font=pygame.font.SysFont('arial',30)

def view():
    global screen
    screen.fill([0, 0, 0])
    number=font.render(str(model.number),True,model.color)
    screen.blit(number,[500,500,20,20])
    pygame.display.flip()