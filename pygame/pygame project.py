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
TITLE = "My House"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SSNOW = (255, 250, 250)
YELLOW = (255, 255, 51)
ORANGE = (255, 125, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (107, 69, 9)
SBLUE = (0, 165, 219)
SGREEN = (0, 212, 106)
GREY = (128, 128, 128)
BBROWN = (139,119,101)
BLUEMOON = (51,161,201)

# Make Clouds
num_clouds = 10
clouds = []
for i in range (num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 100)
    speed = random.randrange(-5, -1)
    loc = [x, y, speed]
    clouds.append(loc)

''' Make snow '''
num_drops = 400
snow = []

for i in range(num_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    drop = [x, y, r, r, stop]
    snow.append(drop)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def snowman(x, y):
    pygame.draw.ellipse(screen, SBLUE, [x, y, 20, 20])
    pygame.draw.ellipse(screen, SBLUE, [x - 5, y + 15, 30, 30])
    pygame.draw.ellipse(screen, SBLUE, [x - 10, y + 30, 40, 40])

def draw_snowdrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, WHITE, rect)

    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] -= c[2]

        if c[0] > 800:
            c[0] = random.randrange(-800, -100)
            c[1] = random.randrange(-50, 100)

    for n in snow:
        n[1] += 2

        if n[1] >400:
            n[0] = random.randrange(0, 800)
            n[1] = random.randrange(0, 10)

    ''' move snow '''
    for r in snow:
        r[0] -= 1
        r[1] += 4

        if r[1] > r[4]:
            r[0] = random.randrange(0, 1000)
            r[1] = random.randrange(-100, 0)

    # Drawing code


    ''' sky '''
    screen.fill(SBLUE)


    ''' moon '''
    pygame.draw.ellipse(screen, BLACK, [575, 75, 100, 100])


    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    ''' grass '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    ''' house '''
    pygame.draw.rect(screen, RED, [300, 250, 200, 150])
    pygame.draw.polygon(screen, BLACK, [[250, 250], [400, 150], [550, 250]])
    pygame.draw.rect(screen, BLACK, [400, 300, 50, 100])

    '''tree'''
    pygame.draw.rect(screen, BBROWN, [100, 200, 50, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = ([x+5, y], [x+10, y + 5], [x+10, y+40], [x, y+40], [x, y+5])
        pygame.draw.polygon(screen, BROWN, post)

        pygame.draw.rect(screen, BROWN, [0, y+10, 900, 5])
        pygame.draw.rect(screen,BROWN, [0, y+30, 800, 5])


    ''' snow ''' 
    for r in snow:
        draw_snowdrop(r)

    '''snowman'''
    snowman(200, 450)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
