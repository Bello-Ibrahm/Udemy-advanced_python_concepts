# Pygame Tutorial

## Requirements:
Pygame library must be installed to run each script:
```
pip install pygame
```

# Important thing to note - Clock and Blit
In the [code](moveable_object.py), Clock and blit are both components of the Pygame library used for managing time and drawing graphics on the screen, respectively.

**Clock:**
`Clock` is a class provided by Pygame that helps regulate the frame rate of your game. It ensures that your game runs at a consistent speed across different devices by controlling how often the game loop executes.
Here's how it works:
- When you create a `Clock` object (`clock = pygame.time.Clock()`), it starts tracking time.
- The `tick` method of the `Clock` object (`dt = clock.tick(60) / 1000`) is then used inside the game loop to regulate the frame rate. It returns the time elapsed since the last call to tick in milliseconds. By dividing this value by `1000`, you get the time elapsed in seconds (`dt`), which can be used to make movements or animations consistent regardless of the frame rate.

**blit:**
`blit` is a method used to draw images, surfaces, or other objects onto the screen in Pygame. It's short for "block transfer" and it copies pixels from one surface to another. Here's how it's used in the code:
- `screen.blit(source, dest)` is used to draw the rectangle onto the screen. Here, `source` is the surface or object you want to draw (in this case, the red rectangle), and `dest` is the position where you want to draw it.
- In the [code](moveable_object.py), the rectangle is drawn using  `pygame.draw.rect`, which draws a rectangle directly onto the screen surface. So, `blit` isn't explicitly used for drawing the rectangle, but it's commonly used for drawing images or surfaces onto the screen in Pygame.

In summary, `Clock` helps regulate the frame rate of your game loop, ensuring smooth and consistent movement, while `blit` is a method used to draw images or surfaces onto the screen in Pygame, although in this specific code it's not used for drawing the rectangle.

# Setup
Each codes are wrapped into a function, to run each function uncomment the specify function call and run the script:
On windows
```
python filename.py
```