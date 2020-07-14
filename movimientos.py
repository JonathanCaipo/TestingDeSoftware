#simulacion una parte
import pygame, random
pygame.init()
screen = pygame.display.set_mode([440,440])
leave = False


clock = pygame.time.Clock()

class Head():
    def __init__(self):
        self.location = [random.randint(4,10) * 20,random.randint(4,10) * 20]
        self.directions = ["up","right","down", "left"]
        self.direction = random.randint(0,3)
        return
        

    def move(self):
        turned = False
        for event in pygame.event.get():
            if event == pygame.QUIT: leave = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    leave == True
                elif event.key == pygame.K_UP and self.direction != 2 and not turned:
                    self.direction = 0
                    turned = True
                elif event.key == pygame.K_DOWN and self.direction != 0 and not turned:
                    self.direction = 2
                    turned = True
                elif event.key == pygame.K_RIGHT and self.direction != 3 and not turned:
                    self.direction = 1
                    turned = True
                elif event.key == pygame.K_LEFT and self.direction != 1 and not turned:
                     self.direction = 3
                     turned = True
        if self.direction == 0:
            self.location[1] -= 20
        if self.direction == 1:
            self.location[0] += 20
        if self.direction == 2:
            self.location[1] += 20
        if self.direction == 3:
            self.location[0] -= 20

        if head.location[0] < 0:
            head.location[0] = 420
        if head.location[0] > 420:
            head.location[0] = 0
        if head.location[1] < 0:
            head.location[1] = 420
        if head.location[1] > 420:
            head.location[1] = 0

        return
