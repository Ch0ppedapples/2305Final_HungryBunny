# import random
import pygame
import sys



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


    # def player():
        # need a way to check tiles to determine if the player can go there or not

        # input key result in movement of the player + animation of player 

def main():
    pygame.init()

    clock = pygame.time.Clock()
    pygame.display.set_caption("Hungry Bunny!!")
    
    height = 900
    width = 700
    
    screen = pygame.display.set_mode((height,width), pygame.RESIZABLE)

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

          

        yellow = pygame.Color(255, 250, 179)
        screen.fill(yellow)


        pygame.display.flip()
        clock.tick(24)
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()