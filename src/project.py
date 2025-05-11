# import random
import pygame
import sys
import glob
import os
import moviepy.editor as mpy




# class for the player movement and animation of the player 

      
#  if tile is >0 then the jackalope can move 
# if not the jackalope does not move 
#  elif tile == 2 
    # title card.draw(screen)

        
   

class Maze:
    def __init__(self):

        self.size = 50
        self.width = self.size * 18
        self.height = self.size* 14
        self.images ={0: pygame.image.load('greenTile.png').convert(), 1: pygame.image.load( 'tanTile.png').convert()
                      , 2:pygame.transform.scale(pygame.image.load('carrot_2.png').convert(), (self.size, self.size))}
        self.maze_map()

        
        

    def maze_map(self):

        self.maze =[[1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                    [0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1],
                    [0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                    [0,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0],
                    [0,0,1,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0],
                    [0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0],
                    [0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0],
                    [0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,0],
                    [0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1],
                    [0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0],
                    [0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1],
                    [1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,2]]
       
        
    def draw(self, screen, size):
        
        for row in range(len(self.maze)):
            for column in range (len(self.maze[row])):
                x = column * size 
                y = row * size
                tile = self.images[self.maze[row][column]]
                screen.blit(tile,(x,y))
            

    


class Player:
    def __init__(self, pos =(0,0), sprite_path= '', maze =None):
    
        self.pos =pygame.Vector2(pos)
        self.speed =24
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.maze = maze.maze_map()


    def move(self, dir):
        self.pos=self.pos+dir *self.speed
        
        
    # def check_if_path(self):

    
    
    def check_win(self, screen):
        print(self.pos)
        row= self.pos.y//50
        column = self.pos.x//50
        if row==14 and column == 18:
            screen.blit('win_titlecard', (0,0))


    def draw(self, screen):
        screen.blit(self.image, self.pos)





def main():
    pygame.init()

    height = 900
    width = 700

    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((height,width), pygame.RESIZABLE)
    pygame.display.set_caption("Hungry Bunny!!")


    bg_tan_tile = pygame.image.load('tanTile.png').convert()    
    # win_titlecard= pygame.image.load('Win_tilecard.png').convert()
    
    maze = Maze()
    jackalope = Player(pos=(0,0),sprite_path='stillbunnyresize.png', maze =maze)
    
    

    running = True
    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            


            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                jackalope.move(pygame.Vector2(0,-2))
            if keys[pygame.K_DOWN]:
                jackalope.move(pygame.Vector2(0,2))
            if keys[pygame.K_LEFT]:
                jackalope.move(pygame.Vector2(-2,0))
            if keys[pygame.K_RIGHT]:
                jackalope.move(pygame.Vector2(2,0))

        for x in range(0, width, bg_tan_tile.get_width()):
            for y in range(0, height, bg_tan_tile.get_height()):
                screen.blit(bg_tan_tile,(x,y))
        jackalope.check_win(screen)          
        maze.draw(screen, size=50)
        jackalope.draw(screen) 
        # screen.blit(win_titlecard, (0,0))
        
        pygame.display.flip()
        clock.tick(24)
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()