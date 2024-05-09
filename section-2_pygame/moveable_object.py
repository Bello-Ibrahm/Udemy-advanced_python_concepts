import pygame
import sys


def pygame_movable_rectangle():
    """
    Initializes Pygame and creates a movable rectangle in a window.
    """
    pygame.init()

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Movable Object Tutorial")

    BLACK = (0, 0, 0)  # Define color black

    rectangle_X = SCREEN_WIDTH // 2  # Initial X position of the rectangle
    rectangle_Y = SCREEN_HEIGHT // 2  # Initial Y position of the rectangle

    rectangle_width = 30  # Width of the rectangle
    rectangle_height = 30  # Height of the rectangle

    clock = pygame.time.Clock()  # Create a Clock object to control the frame rate
    dt = 0  # Time delta, time passed since last frame
    SPEED = 200  # Speed at which object moves

    while True:  # Main game loop
        screen.fill(BLACK)  # Fill the screen with black color

        for event in pygame.event.get():  # Check for events
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the program

        keys = pygame.key.get_pressed()  # Get the keys currently pressed

        if keys[pygame.K_LEFT] and rectangle_X > 0:  # If left arrow key is pressed and rectangle is not at the left edge
            rectangle_X -= SPEED * dt  # Move the rectangle left
        if keys[pygame.K_RIGHT] and rectangle_X < SCREEN_WIDTH - rectangle_width:  # If right arrow key is pressed and rectangle is not at the right edge
            rectangle_X += SPEED * dt  # Move the rectangle right
        if keys[pygame.K_UP] and rectangle_Y > 0:  # If up arrow key is pressed and rectangle is not at the top edge
            rectangle_Y -= SPEED * dt  # Move the rectangle up
        if keys[pygame.K_DOWN] and rectangle_Y < SCREEN_HEIGHT - rectangle_height:  # If down arrow key is pressed and rectangle is not at the bottom edge
            rectangle_Y += SPEED * dt  # Move the rectangle down
        
        pygame.draw.rect(screen, (255, 0, 0), (rectangle_X, rectangle_Y, rectangle_width, rectangle_height))  # Draw the rectangle
        pygame.display.update()  # Update the display
        dt = clock.tick(60) / 1000  # Control the frame rate and calculate time delta

pygame_movable_rectangle()

def pygame_movable_circle_with_mouse():
    """
    """
    pygame.init()

    # Set up the window
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 400
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption("Movable Circle Tutorial")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    # Circle properties
    circle_radius = 30
    circle_color = BLUE

    # Circle position
    circle_x = WINDOW_WIDTH // 2
    circle_y = WINDOW_HEIGHT // 2

    # Variable for mouse dragging
    is_dragging = False
    offset_x = 0
    offset_y = 0

    # Main loop
    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if circle_x - circle_radius < mouse_x < circle_x + circle_radius and \
                       circle_y - circle_radius < mouse_y < circle_y + circle_radius:
                       is_dragging = True
                       offset_x = mouse_x - circle_x
                       offset_y = mouse_y - circle_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if is_dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Ensure circle stays within window boundaries
                    circle_x = min(max(mouse_x - offset_x, circle_radius), WINDOW_WIDTH - circle_radius)
                    circle_y = min(max(mouse_y - offset_y,  circle_radius), WINDOW_HEIGHT - circle_radius)

        # Draw the circle
        pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
        
        # Update te display
        pygame.display.update()
    
# pygame_movable_circle_with_mouse()