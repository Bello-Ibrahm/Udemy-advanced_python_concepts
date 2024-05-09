import pygame
import random

def pygame_snow_particle():
    """
    Initialize Pygame and display snow particles on the screen.
    """
    pygame.init()  # Initialize Pygame

    SIZE = [400, 400]  # Define the size of the display window

    screen = pygame.display.set_mode(SIZE)  # Create the display window
    pygame.display.set_caption("Snow Particles Display")  # Set the window title

    white = (255, 255, 255)  # Define the color white
    black = (0, 0, 0)  # Define the color black
    
    snowParticles = []  # Create an empty list to store snow particle positions

    for i in range(100):  # Generate 100 random snow particle positions
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)

        snowParticles.append([x, y])  # Add the position to the list
    
    clock = pygame.time.Clock()  # Create a Clock object to control the frame rate
    
    playing = False  # Initialize the playing flag as False
    while not playing:  # Main game loop
        screen.fill(black)  # Fill the screen with black color

        for event in pygame.event.get():  # Check for events
            if event.type == pygame.QUIT:  # If the user closes the window
                playing = True  # Set the playing flag to True to exit the loop

        for j in range(len(snowParticles)):  # Loop through each snow particle
            pygame.draw.circle(screen, white, snowParticles[j], 2)  # Draw the snow particle
            snowParticles[j][1] += 1  # Move the snow particle down

            if snowParticles[j][1] > 400:  # If the snow particle reaches the bottom of the screen
                y = random.randrange(-50, -10)  # Generate a random y-coordinate above the screen
                snowParticles[j][1] = y  # Reset the y-coordinate of the snow particle
                x = random.randrange(0, 400)  # Generate a random x-coordinate within the screen
                snowParticles[j][0] = x  # Reset the x-coordinate of the snow particle
        
        pygame.display.flip()  # Update the display
        # clock.tick(20) / 1000 
        clock.tick(20)  # Control the frame rate

    pygame.quit()  # Quit Pygame when the loop ends


pygame_snow_particle()