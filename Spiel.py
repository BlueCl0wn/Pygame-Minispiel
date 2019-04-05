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

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)




man = player(300, 410, 64, 64)
# Aktualisiert das Fenster und sorgt für Bewegunsanimation
def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# Mainloop
run = True
bullets = []
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x <= 852 and bullet.x >= 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE]:
        if man.right:
            facing = 1
        else:
            facing = -1
        if len(bullets) <= 5:
            bullets.append(projectile(man.x + man.width//2, man.y + man.height//2, 5,(0, 0, 0), facing))
    if keys[pygame.K_LEFT]:
        man.x -= man.vel
        if man.x < -16:
            man.x += (-16 - man.x)
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT]:
        man.x += man.vel
        if man.x > (sizex - 48):
            man.x += ((sizex - 48) - man.x)
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                 neg = -1
            man.y -= (man.jumpCount ** 2) * 0.3 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
