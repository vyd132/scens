import pygame,model

event_type=pygame.event.custom_type()


def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
            model.number+=1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            model.display='first'
