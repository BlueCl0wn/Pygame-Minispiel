import pygame

pygame.init()


sizex = 852
sizey = 480
win = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption("First Window")

# Öffnet die Bilder für die Bewegungsanimation
walkRight = [pygame.image.load('IMG/R1.png'), pygame.image.load('IMG/R2.png'), pygame.image.load('IMG/R3.png'), pygame.image.load('IMG/R4.png'), pygame.image.load('IMG/R5.png'), pygame.image.load('IMG/R6.png'), pygame.image.load('IMG/R7.png'), pygame.image.load('IMG/R8.png'), pygame.image.load('IMG/R9.png')]
walkLeft = [pygame.image.load('IMG/L1.png'), pygame.image.load('IMG/L2.png'), pygame.image.load('IMG/L3.png'), pygame.image.load('IMG/L4.png'), pygame.image.load('IMG/L5.png'), pygame.image.load('IMG/L6.png'), pygame.image.load('IMG/L7.png'), pygame.image.load('IMG/L8.png'), pygame.image.load('IMG/L9.png')]
bg = pygame.image.load('IMG/bg.jpg')
char = pygame.image.load('IMG/standing.png')

clock = pygame.time.Clock()

x = 200
y = 370
width = 64
height = 64
vel = 5

left = False
right = False
walkCount = 0

isJump = False
jumpCount = 10

# Aktualisiert das Fenster und sorgt für Bewegunsanimation
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()

# Mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if x < -16:
            x += (-16 - x)
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        x += vel
        if x > (sizex - 48):
            x += ((sizex - 48) - x)
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        # if keys[pygame.K_UP]:
        #     y -= vel
        #     if y < 0:
        #         y += (0 - y)
        # if keys[pygame.K_DOWN]:
        #     y += vel
        #     if y > (852 - height):
        #         y += ((852 - height) - y)
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                 neg = -1
            y -= (jumpCount ** 2) * 0.3 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
