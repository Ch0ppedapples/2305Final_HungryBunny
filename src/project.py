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
        self.maze = self.maze_map()

        
        

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
        return self.maze
        
    def draw(self, screen, size):
        
        for row in range(len(self.maze)):
            for column in range (len(self.maze[row])):
                x = column * size 
                y = row * size
                tile = self.images[self.maze[row][column]]
                screen.blit(tile,(x,y))

   
            

    


class Player:
    def __init__(self, pos =(0,0), sprite_path= '', maze =Maze.maze_map):
        self.size = 50
        self.pos =pygame.Vector2(pos)
        self.speed =24
        self.image = pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(),(self.size, self.size))
        self.maze = maze.maze_map() 
    


    def move(self, dir):
        if self.check_if_path(dir):
            # print(self.pos)
            # print('before...')
            new_pos = self.pos +dir * self.speed
            self.pos =new_pos
            # print(self.pos) 
            # print('after...')

          
    def check_if_path(self, dir):
        
        check_poss_pos =self.pos + dir
        row =int(check_poss_pos.y//self.size)
        column =int(check_poss_pos.x//self.size)
        if row < 0 or row >= 14:
             return False
        if column < 0 or column >= 18:
             return False
        print(self.maze[row][column])
        print('value before...')
        if row < 0 or row >= len(self.maze) or column < 0 or column >= len(self.maze[0]):
            return False
        
        maze_value = self.maze[row][column]
        print(maze_value)
        print('value after...')
        if maze_value >0:
            return True

    def draw(self, screen):
        screen.blit(self.image, self.pos)


    # def draw_goal(self, screen, winning_image):
    #     winning_image =pygame.image.load('Win_tilecard.png').convert()
    #     row = int(self.pos.y//self.size)
    #     column = int(self.pos.x//self.size)
    #     if self.maze[row][column] == 2:
    #         screen.blit( winning_image, (0,0))





def main():
    pygame.init()

    height = 900
    width = 700

    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((height,width), pygame.RESIZABLE)
    pygame.display.set_caption("Hungry Bunny!!")


      
    
    
    maze = Maze()
    jackalope = Player(pos=(0,0),sprite_path='stillbunny.png', maze =maze)
    
    

    running = True
    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            


            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                jackalope.move(pygame.Vector2(0,-1))
            if keys[pygame.K_DOWN]:
                jackalope.move(pygame.Vector2(0,1))
            if keys[pygame.K_LEFT]:
                jackalope.move(pygame.Vector2(-1,0))
            if keys[pygame.K_RIGHT]:
                jackalope.move(pygame.Vector2(1,0))

        for x in range(0, width, screen.get_width()):
            for y in range(0, height, screen.get_height()):
                screen.blit(screen,(x,y))
        # jackalope.check_win(screen)          
        maze.draw(screen, size=50)
        jackalope.draw(screen) 
        
        
        pygame.display.flip()
        clock.tick(24)
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()