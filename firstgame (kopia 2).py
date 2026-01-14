import pygame
import random

pygame.init()
displayWidth = 1000
displayHeight = 800
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Kupans Spel")

font = pygame.font.SysFont(None, 50)
fontSmall = pygame.font.SysFont(None, 35)


vel = 20
color = (0, 0, 255)
hits = 0
kant = 20
spawnEvent = pygame.USEREVENT + 1

class PlayItem:
      def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
      
      def render(self):
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

            
      
      
gubbe = PlayItem(50, 50, 40, 50)

mango = PlayItem(400, 500, 5, 5)


def renderCharacter():
      gubbe.render() 
       

def characterMovement(keys, play_item):
      

      if keys[pygame.K_LEFT]:
            play_item.x -= vel
      if keys[pygame.K_RIGHT]:
            play_item.x += vel
      if keys[pygame.K_UP]:
            play_item.y -= vel
      if keys[pygame.K_DOWN]:
            play_item.y += vel
      
      hitEdges(play_item)

def characterSize(keys, play_item):
    
      if keys[pygame.K_e]:
            play_item.width = play_item.width + 1
            play_item.height = play_item.height + 1
            
      if keys[pygame.K_q]:
            play_item.width = play_item.width - 1
            play_item.height = play_item.height - 1
        
def characterSpeed(keys):
      global vel
      if keys[pygame.K_a]:
            vel = vel - 1 
      
      if keys[pygame.K_d]:
            vel = vel + 1

def characterColor(keys):
      global color
      if keys[pygame.K_1]:
            color = (255, 255, 255)

      if keys[pygame.K_2]:
            color = (0, 0, 255)

      if keys[pygame.K_3]:
            color = (255, 0, 0)
      
      if keys[pygame.K_4]:
            color = (0, 255, 0)



def hitEdges(play_item):
    
      
      if play_item.x < kant:
            play_item.x = kant

      if play_item.y < kant: 
            play_item.y = kant
      
      if play_item.x > displayWidth - (kant + play_item.width):
            play_item.x = displayWidth - (kant + play_item.width)
            
      if play_item.y > displayHeight - (kant * 4 + play_item.height):
            play_item.y = displayHeight - (kant * 4 + play_item.height)
            
      
     
            
      



def renderTextCenter(text, x, y, font):
      textSurface = font.render(text, True, (255, 255, 255))
      textRect = textSurface.get_rect(center=(x, y))
      screen.blit(textSurface, textRect)


def renderMango():
      pygame.draw.circle(screen, (200, 180, 0), (mango.x, mango.y), (5))  


def render():
      screen.fill((0, 0, 0))

      renderCharacter()
      renderMango()

      renderTextCenter(f"Mangohits: {hits}", 500, 780, font)
      renderTextCenter(f"X: {gubbe.x}, Y: {gubbe.y}", 900, 750, fontSmall)
      renderTextCenter(f"Speed: {vel}", 75, 750, fontSmall)
      
      


def gameField():
      pygame.draw.rect(screen, (255, 255, 255), (kant, kant, displayWidth - kant * 2, displayHeight - kant * 5), width = 2)
      pygame.display.update()
      
def mangoHits():
      if mango.x < gubbe.x:
            return False
      if mango.y < gubbe.y:
            return False
      if mango.x > gubbe.x + gubbe.width:
            return False
      if mango.y > gubbe.y + gubbe.height:
            return False
      return True


pygame.time.set_timer(spawnEvent, 2000)



run = True
while run: 
      pygame.time.delay(25)
      keys = pygame.key.get_pressed()
      spawnEvent
      
      

      gameField()
      characterMovement(keys, gubbe)
      
      characterSize(keys, gubbe)
     
      characterSpeed(keys)
      characterColor(keys)
      
      

      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 run = False
            if event.type == spawnEvent:
                  mango.x = random.randint(kant, displayWidth - kant) 
                  mango.y = random.randint(kant, displayHeight - kant * 4)

      if mangoHits():
            hits += 1
            mango.x = 10000

      render()

      

pygame.quit()






