import pygame
import sys
import os

def ButtonClick(mousePos, btnSize, btnPos):
    if btnPos[0] <= mousePos[0] <= btnPos[0] + btnSize[0] and \
        btnPos[1] <= mousePos[1] <= btnPos[1] + btnSize[1]:
        return True
    else:
        return False
            

def Home(screen,assets):
    state = 'HOME'
    screen.fill(white)
    btn_0 = pygame.transform.scale(assets[0], (300,100))
    screen.blit(btn_0, (320-150,180))
    screen.blit(btn_0, (320-150,300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ButtonClick(event.pos, (300,100), (320-150,180)): # first button
                print(1)
            if ButtonClick(event.pos, (300,100), (320-150,300)): # second button
                print(2)
    
    
    return state



# initialization
print('Initialization')
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
white = (255,255,255)
black = (0,0,0)

# load assets
assets = {}
assets_path = 'assets'
assets_list = os.listdir(assets_path)
for asset_name in assets_list:
    i = int(os.path.splitext(asset_name)[0])
    assets[i] = pygame.image.load(assets_path + '/' + asset_name)

clock = pygame.time.Clock()
state = "HOME"


# mainLoop
print('Main loop')
while True:
    clock.tick(60)
    
    if state == 'HOME':
        state = Home(screen, assets)
    
    pygame.display.flip()
        
