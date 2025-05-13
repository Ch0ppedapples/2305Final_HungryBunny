
import pygame
import sys
import moviepy.editor as mpy



        
   

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
        self.allowed_pos = [[0,0],[0,650],[50,0],[50,350],[50,650],[100,650],[100,600],[100,550],[100,500],[100,450],[100,350],
                        [100,200],[100,150],[100,100],[100,50],[100,0],[150,200],[150,350],[150,550],[200,550],[200,500],
                        [200,450],[200,400],[200,350],[200,300],[200,250],[200,200],[200,100],[200,50],[250,50],
                        [250,450],[300,650],[300,600],[300,450],[300,400],[300,350],[300,150],[300,100],[300,50],[350,50],
                        [350,150],[350,350],[350,600],[400,600],[400,550],[400,500],[400,450],[400,350],[400,300],
                        [400,250],[400,200],[400,150],[400,50],[450,0],[450,50],[450,350],[450,400],[450,450],[450,550],
                        [500,550],[500,350],[500,200],[500,0],[550,0],[550,150],[550,200],[550,250],[550,300],[550,350],
                        [550,500],[550,550],[550,600],[550,650],[600,650],[600,500],[600,150],[600,50],[650,50],
                        [650,150],[650,300],[650,350],[650,400],[700,600],[700,550],[700,500],[700,400],[700,300],
                        [700,150],[700,100],[700,50],[750,150],[750,200],[750,250],[750,300],[750,400],[750,500],
                        [750,600],[800,600],[800,500],[800,450],[800,400],[800,150],[800,100],[800,50],[850,50],
                        [850,500],[850,600], [850,650]] 
    


    def move(self, dir):
        new_pos =self.pos +dir * self.size
        if new_pos in self.allowed_pos:
         self.pos=self.pos+dir *self.size
        elif not self.pos in self.allowed_pos:
            return False
        if dir == pygame.Vector2(-1,0):
            self.image = pygame.transform.flip(self.image, True, False)
    

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        
    








def main():
    pygame.init()

    height = 900
    width = 700
    
    
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((height,width), pygame.RESIZABLE)
    pygame.display.set_caption("Hungry Bunny!!")

    maze = Maze()
    maze_map = maze.maze_map()
      
    
    win_tilecard_surface = pygame.image.load('Win_tilecard.png').convert()
    jackalope = Player(pos=(0,0),sprite_path='stillbunny.png', maze =maze)
    
    print(jackalope.pos)
    maze.draw(screen, size=50)
    jackalope.draw(screen) 
    
    won =False
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
            if (jackalope.pos) ==[850,650] :
                won = True
            if won:
                screen.blit( win_tilecard_surface, (0,0))
                pygame.display.flip()

            if not won:
                maze.draw(screen, size=50)
                jackalope.draw(screen)
            else:
                screen.blit(win_tilecard_surface, (0, 0))

       
       
            
        
        pygame.display.flip()
        clock.tick(24)
        
        if  pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()

if __name__ == "__main__":
    main()