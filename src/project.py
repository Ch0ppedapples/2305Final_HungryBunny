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
        self.maze = maze.maze_map() if maze else[]
        


    def move(self, dir):
        if self.check_if_path(dir):
            self.pos=+ dir *self.size
        
    def check_if_path(self, dir):
        check_poss_pos =self.pos + dir
        row =int(check_poss_pos.x//50)
        column =int(check_poss_pos.y//50)
        if row < 0 or row >= 14:
             return False
        if column < 0 or column >= 18:
             return False
        print(self.maze[row][column]) 
        if self.maze[row][column] == 1 or self.maze[row][column] == 2:
                    return True
        elif (self.maze[row][column]) ==0:
                    return False
        
          
         
    
    # def check_win(self, screen):
    #     row= self.pos.y//50
    #     column = self.pos.x//50
    #     win_titlecard = pygame.image.load('Win_tilecard.png').convert()
    #     if row==13 and column == 17:
    #         screen.blit(win_titlecard,(0,0))
    #     print(f"Player is at row {row}, column {column}")


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

        for x in range(0, width, bg_tan_tile.get_width()):
            for y in range(0, height, bg_tan_tile.get_height()):
                screen.blit(bg_tan_tile,(x,y))
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