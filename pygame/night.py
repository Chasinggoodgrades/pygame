# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


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


''' Make stars '''
stars = []
for i in range(400):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for s in stars:
        s[1] += 2

        if s[1] >400:
            s[0] = random.randrange(0, 800)
            s[1] = random.randrange(0, 10)
    
    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])
    
    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, SBLUE, s)

    ''' moon '''
    pygame.draw.ellipse(screen, GREY, [575, 75, 100, 100])



    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
