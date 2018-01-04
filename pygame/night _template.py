# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make snow and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 51)
ORANGE = (255, 125, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (107, 69, 9)
SBLUE = (0, 165, 219)
SGREEN = (0, 212, 106)
GREY = (128, 128, 128)

'''make snow'''
snow = []
for i in range(200):
    x = random.randrange(0,800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    snow.append([x, y, r, r])

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])


    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code


    ''' sky '''
    screen.fill(SBLUE)



    ''' snow '''
    for s in snow:
        pygame.draw.ellipse(screen, WHITE, s)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])


    ''' clouds '''
    draw_cloud(20, 90)
    draw_cloud(150, 25)
    draw_cloud(350, 95)
    draw_cloud(450, 45)
    draw_cloud(600, 100)


    ''' grass '''
    pygame.draw.rect(screen, SGREEN, [0, 400, 800, 200])

    ''' house '''
    pygame.draw.rect(screen, RED, [300, 250, 200, 150])
    pygame.draw.polygon(screen, BROWN, [[250, 250], [400, 150], [550, 250]])
    pygame.draw.rect(screen, BLACK, [400, 300, 50, 100])

    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = ([x+5, y], [x+10, y + 5], [x+10, y+40], [x, y+40], [x, y+5])
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 900, 5])
    pygame.draw.rect(screen,WHITE, [0, y+30, 800, 5])

    '''snowman'''


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
