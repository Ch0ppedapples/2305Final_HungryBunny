# import random
import pygame
import sys



# class to defin the the maze tiles and what they do (wall, passage, finish)
# class for making the maze
# class for the player movement and animation of the player 

class Player:
    def __init__(self, pos =(0,0), sprite_path= ''):
        self.pos =pygame.Vector2(pos)
        self.speed =24
        self.image = pygame.image.load(sprite_path).convert_alpha()
        

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


    

def main():
    pygame.init()

    clock = pygame.time.Clock()
    pygame.display.set_caption("Hungry Bunny!!")
    
    height = 900
    width = 700
    
    screen = pygame.display.set_mode((height,width), pygame.RESIZABLE)


    playerMove = Player(pos=(height//2, width//2),
                        sprite_path="stillbunny.png")

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