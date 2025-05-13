# 2305Final_HungryBunny
final project for 2305 programming for digital art.



## Demo
Demo Video: <https://youtu.be/4fQgdaSN0L8>

## GitHub Repository
GitHub Repo: <https://github.com/Ch0ppedapples/2305Final_HungryBunny>

## Description
 This project, I created a maze game using a tile method to create the images of the maze.
I drew my own character, the Jackalope, and the carrot that represents the finishing line
and the winning title card, which read "yaay!! food!!". The way the tiles are represented
is by a dictionary which defines what the numbers represent 0,1, and 2. 0, which are the green tiles or the walls in the dictionary. I also went ahead and assigned all the PNG files that will represent the numbers when drawn on the screen. 1 is the tan tile or the path. 2 is the carpet or the finished line. The actual map of the maze
was created with lists inside a list. Which then gets iterated through to then be drawn.
    The player is represented as the Jackalope. I use pygame.Vector2 to calculate the movement corresponding to the inputs of the arrow keys.
In the Player call of the move method, I used dir because I was using pygame.Vector. Also, when calculating the player's movement, I used self.size so
that the player would only move the distance on one single tile. Another thing I did in the move method was I used pygame.transform.flip so that the image of the
player would flip to look like it's going in the right direction you want to go, since the default position of the player was facing to the right.
    The main thing I struggled with in this project was setting up the boundary of the walls so the player wouldn't be allowed to go in the green area. The bug I was
having was that although I had set up a check_if_path method that should be correct based on me going around and around with CS50.ai and being stumped on the problem of why the values of the tile that I assigned where getting changed somewhere in my code. The very inconvenient solution I came up with was to list all the path tiles in a list and create an if statement to only let the player go on those tiles. The reason I did this was to prioritize the game actually working.
For the finish line create the carrort I ended up adding it to the main function. By creating a varibale won thats equal to false intill you get to the winning tile!
I used multiple if and else statements since i also needed to stop the maze and jackalope from being drawn.
    Overall, I'm pleased with how it came out, even though it didn't turn out exactly how I planned. This class was my first time coding, so this was really tough for me
But I enjoyed the class and this final project!


