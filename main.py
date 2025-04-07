import pygame
from random import randint

pygame.init()

LITELBLUE = (51, 204, 255)
RED = (251, 54, 1)

back = (51, 204, 255)
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Flopa game')
window.fill(back)

fps = pygame.time.Clock()

class Hitbox():
    def __init__(self, x, y, width, height):
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(window, back, self.hitbox)

class Sprite(Hitbox):
    def __init__(self, x, y, width, height, speed, filename):
        Hitbox.__init__(self, x, y, width, height)
        self.speed = speed
        self.image = pygame.image.load(filename) #створення картинки

    def show(self):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

person = Sprite(400, 400, 72, 86,  7, "taziceii.png")

flag_right = False
flag_left = False 

pelmens = []

for i in range(3):
    pelmen = Sprite(randint(0,450), 0, 43, 54, randint(3, 6), "pelmen_good.png")
    pelmens.append(pelmen)
 
count = 0
skip = 0

font_style = pygame.font.SysFont("Fonty Python", 36)
collected = font_style.render(str(count), True, RED)
collected_text = font_style.render("Зібрано:", True, RED)
skipped = font_style.render(str(skip), True, RED)
skipped_text = font_style.render("Пропущено:", True, RED)

lose = font_style.render("YOU LOSE", True, RED)
win = font_style.render("YOU WIN", True, RED)

game = True
while game:
    window.fill(back)
    person.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                flag_right = True
            if event.key == pygame.K_LEFT:
                flag_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                flag_right = False
            if event.key == pygame.K_LEFT:
                flag_left = False
   
    for pelmen in pelmens:
        pelmen.hitbox.y += pelmen.speed

    if person.hitbox.x > 0 and person.hitbox.x < 428:
        if flag_right:
            person.image = pygame.image.load("taziceii.png")
            person.hitbox.x += person.speed
        if flag_left:
            person.image = pygame.image.load("tazice-leftt.png")
            person.hitbox.x -= person.speed 

    if skip == 10:
        window.blit(lose, (250, 250))
        game = False
        pygame.time.delay(10000)
    
    if count == 20:
        window.blit(win, (250, 250))
        game = False        
        pygame.time.delay(10000)

    for pelmen in pelmens:
        if person.hitbox.colliderect(pelmen.hitbox):
            pelmens.remove(pelmen)
            count += 1
            pelmen_new = Sprite(randint(0,450), 0, 43, 54, randint(1, 4), "pelmen_good.png")
            pelmens.append(pelmen_new)

    for pelmen in pelmens:
        if pelmen.hitbox.y > 500:
            pelmens.remove(pelmen)
            skip += 1
            pelmen_new = Sprite(randint(0,450), 0, 43, 54, randint(1, 4), "pelmen_good.png")
            pelmens.append(pelmen_new)

    for pelmen in pelmens:
        pelmen.show()  

        
    collected = font_style.render(str(count), True, RED)
    skipped = font_style.render(str(skip), True, RED)

    window.blit(collected, (110, 0))
    window.blit(collected_text, (0, 0))
    window.blit(skipped, (150, 30))
    window.blit(skipped_text, (0, 30))



    pygame.display.update()
    fps.tick(40)

