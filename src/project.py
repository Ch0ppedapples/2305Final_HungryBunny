# import random
import pygame
import sys
from PIL import Image
import glob
import os
import moviepy.editor as mpy



# class to defin the the maze tiles and what they do (wall, passage, finish)
# class for making the maze
# class for the player movement and animation of the player 

      

# class Maze:
    
#     def __init__(self):

#        self.tile_maze = [[1,1,0,1,0,0,0,0,0,1,1,1,0,0],
#                         [0,1,0,1,1,1,1,0,0,0,0,1,0,0],
#                         [0,1,0,0,0,0,1,0,1,0,0,1,0,0],
#                         [1,1,1,1,0,0,1,0,1,0,1,1,0,0],
#                         [0,0,0,1,0,0,1,1,1,0,1,0,0,0],
#                         [0,0,0,1,0,0,1,0,1,0,1,1,1,1],
#                         [0,1,1,1,1,0,1,0,1,0,1,0,0,1],
#                         [0,1,0,0,0,0,1,0,1,1,1,0,1,1],
#                         [0,1,0,1,1,1,1,0,0,1,0,0,0,0],
#                         [1,1,0,1,0,0,1,0,1,1,1,1,1,1],
#                         [1,1,1,1,0,1,1,0,1,1,1,0,0,2]]

       
    
        


    # def draw():
        # refernce to the tile method using 0 and 1 

class Player:
    def __init__(self, pos =(0,0), sprite_path= ''):
        self.pos =pygame.Vector2(pos)
        self.speed =24
        self.image = pygame.image.load(sprite_path).convert_alpha()


    def move(self, dir):
        self.pos=self.pos+dir *self.speed

    def draw(self, screen):
        screen.blit(self.image, self.pos)

class Animate:
    def __init__(self, folderpath, imgseq, fps= 24):
        self.folderpath = (r'C:\Users\Audrey\OneDrive\Desktop\Programming\Final_bunnyGame\2305Final_bunnyGame\src\bunnyAnim')
        self.imgseq =glob.glob(os.path.join( folderpath,'*.png'))
        imgseq.sort()
        self.clip = mpy.ImageSequenceClip(imgseq, fps)

def main():
    pygame.init()

    height = 900
    width = 700

    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((height,width), pygame.RESIZABLE)
    pygame.display.set_caption("Hungry Bunny!!")


    bg_tan_tile = pygame.image.load('tanTile.png').convert()    

    playerMove = Player(pos=(50,50),sprite_path= Animate)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                playerMove.move(pygame.Vector2(0,-2))
            if keys[pygame.K_DOWN]:
                playerMove.move(pygame.Vector2(0,2))
            if keys[pygame.K_LEFT]:
                playerMove.move(pygame.Vector2(-2,0))
            if keys[pygame.K_RIGHT]:
                playerMove.move(pygame.Vector2(2,0))

        for x in range(0, width, bg_tan_tile.get_width()):
            for y in range(0, height, bg_tan_tile.get_height()):
                screen.blit(bg_tan_tile,(x,y))
        playerMove.draw(screen)               

        
        pygame.display.flip()
        clock.tick(24)
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()