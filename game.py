import pygame
import random
pygame.init()

#Creates screen
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

#loads images for game
player = pygame.image.load("player.jpg")
monster1 = pygame.image.load("monster.jpg")
monster2 = pygame.image.load("monster.jpg")
boss = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.jpg")

#sets height and width for boundry direction
player_height = player.get_height()
player_width = player.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()
boss_height = boss.get_height()
boss_width = boss.get_width()
mon1_height = monster1.get_height()
mon1_width = monster1.get_width()
mon2_height = monster2.get_height()
mon2_width = monster2.get_width()

#sets positions of player. Monsters, boss and prize start off screen
playerXPosition = 100
playerYPosition = 50
mon1XPosition = screen_width
mon1YPosition = random.randint(0 ,screen_height - mon1_height)
mon2XPosition = random.randint(0, screen_width - mon2_width)
mon2YPosition = screen_height
bossXPosition = screen_width
bossYPosition = random.randint(0, screen_height - boss_height)
prizeXPosition = random.randint(0, screen_width - prize_width)
prizeYPosition = screen_height

#checks if either up, down, left and right keys are pressed
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

while 1:
    #clears screen
    screen.fill(0)
    #displays player, monsters, boss and prize in their position
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(monster1, (mon1XPosition, mon1YPosition))
    screen.blit(monster2, (mon2XPosition, mon2YPosition))
    screen.blit(boss, (bossXPosition, bossYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    #updates screen
    pygame.display.flip()

    for event in pygame.event.get():
        #exits if user quits program
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #checks if user presses any of the keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        #checks if user lets go of any of the keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    #Player will move according to the keys pressed
    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition +=1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -=1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1

    #creates a bounding box around player
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    #creates a bounding box around mon1
    mon1Box = pygame.Rect(monster1.get_rect())
    mon1Box.top = mon1YPosition
    mon1Box.left = mon1XPosition

    #creates a bounding box around mon2
    mon2Box = pygame.Rect(monster2.get_rect())
    mon2Box.top = mon2YPosition
    mon2Box.left = mon2XPosition

    #creates a bounding box around boss
    bossBox = pygame.Rect(boss.get_rect())
    bossBox.top = bossYPosition
    bossBox.left= bossXPosition

    #creates a bounding box around prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    #Tests if the player collides with a monster or the boss, in which case prints "You lose!"
    if playerBox.colliderect(mon1Box) or playerBox.colliderect(mon2Box) or playerBox.colliderect(bossBox):
        print ("You lose!")
        pygame.quit()
        exit(0)

    #Tests if the player collides with prize, in which case prints "You win!"
    if playerBox.colliderect(prizeBox):
        print ("You win!")
        pygame.quit()
        exit(0)

    #Allows monsters, boss and prize to move
    mon1XPosition -= 0.5
    mon2YPosition -= 1
    bossXPosition -= 2
    prizeYPosition -= 0.4
    
            
            
                

