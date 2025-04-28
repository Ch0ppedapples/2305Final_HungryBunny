# import random
import pygame




# class tho defin the the maze tiles and what they do (wall, passage, finish)
# class for making the maze
# class for the player movement and animation of the player 
# add to main function for it to work


class Tile:
    def __init__(self, x, y, thinkness):
        self.x, self.y = x, y
        self.thinkness =thinkness
        self.walls ={'top':True, 'right': True, 'bottom':True, 'left':True}
        self.visited =False

def main():
    pygame.init()
    pygame.display.set_caption("Hungry Bunny!!")
    
    

    resolution =(900,700)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        green = pygame.Color(124, 197, 118)
        screen.fill(green)


        pygame.display.flip()
        
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()