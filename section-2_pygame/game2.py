import pygame


def pygame_object_jump():
    """A simple pygame tutorial demonstrating object jumping.

    This script creates a window using pygame and draws a rectangle representing
    an object. The object can jump when the spacebar is pressed. The jump is 
    simulated by changing the object's vertical position based on a simple 
    physics model. The object falls back to the ground after reaching a certain 
    height.

    Controls:
        - Press SPACEBAR to make the object jump.

    Attributes:
        - v (int): Initial velocity of the object when jumping.
        - m (int): Multiplier used to simulate the object's jump and fall.
        - jumping (bool): Flag indicating whether the object is currently jumping.

    Functions:
        - pygame_object_jump(): Main function to run the pygame tutorial.
    """
    pygame.init()

    screen = pygame.display.set_mode([450, 450])
    pygame.display.set_caption("Object Jump Tutorial")
    playing = True

    x = 200
    y = 200

    width = 30
    height = 40 

    jumping = False

    v = 8
    m = 1

    while playing:
        screen.fill("purple")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False


        pygame.draw.rect(screen, (0, 255, 118), (x, y, 30, 30))
        
        key_pressed = pygame.key.get_pressed()

        if jumping == False:
            if key_pressed[pygame.K_SPACE]:
                jumping = True
        
        if (jumping == True):  # If the character is currently jumping
            F = ((1 / 2) * m * (v**2))  # Calculate the force applied during the jump
            y -= F  # Adjust the vertical position based on the force

            v = v - 1  # Decrease the velocity of the character

        if v < 0:  # If the velocity becomes negative
            m = -1  # Change the direction of movement

        if v == -9:  # If the velocity reaches a certain threshold
            jumping = False  # End the jump
            v = 7  # Reset the velocity for future jumps
            m = 1  # Reset the movement direction


        pygame.time.delay(60)

        pygame.display.update()
    
    pygame.quit()

pygame_object_jump()