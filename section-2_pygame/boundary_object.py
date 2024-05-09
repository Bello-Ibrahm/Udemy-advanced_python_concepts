import pygame
import random


def pygame_boundary_object():
    """
    Initialize Pygame and add boundaries to an object's movement.
    """
    pygame.init()  # Initialize Pygame

    width = 700  # Define the width of the display window
    height = 550  # Define the height of the display window

    screen = pygame.display.set_mode([width, height])  # Create the display window
    pygame.display.set_caption("Adding Boundaries to Object")  # Set the window title

    red = (255, 0, 0)  # Define the color red
    
    ball_X = width / 2 - 12  # Initial X position of the ball
    ball_Y = height / 2 - 12  # Initial Y position of the ball
    
    ball_XMove = 0.5 * random.choice((1, -1))  # Initial movement in X direction
    ball_YMove = 0.5  # Initial movement in Y direction

    ball_Pixel = 25  # Radius of the ball

    playing = True  # Initialize the playing flag as True
    while playing:  # Main game loop
        screen.fill(red)  # Fill the screen with red color

        for event in pygame.event.get():  # Check for events
            if event.type == pygame.QUIT:  # If the user closes the window
                playing = False  # Set the playing flag to False to exit the loop

        # Check for collision with boundaries and change direction if necessary
        if ball_X + ball_Pixel >= width or ball_X <= 0:
            ball_XMove *= -1
        if ball_Y + ball_Pixel >= height or ball_Y <= 0:
            ball_YMove *= -1

        ball_X += ball_XMove  # Update the X position of the ball
        ball_Y += ball_YMove  # Update the Y position of the ball

        # Draw the ball on the screen
        ballImg = pygame.draw.circle(screen, (0, 0, 255), (int(ball_X), int(ball_Y)), 10)

        pygame.display.update()  # Update the display

    pygame.quit()  # Quit Pygame when the loop ends


pygame_boundary_object()