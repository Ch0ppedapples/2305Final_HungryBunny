# import random
import pygame


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


        green = (124, 197, 118)
        screen.fill(green)
        pygame.display.flip
        
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()