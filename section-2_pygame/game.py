import pygame


def pygame_display_circle():

    pygame.init()

    window = pygame.display.set_mode([400, 400])

    pygame.display.set_caption('Display cirlce')

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        window.fill((255, 255, 255))
        
        pygame.draw.circle(window, (0, 0, 255), (200, 200), 90)

        pygame.display.flip()

    pygame.quit()

# pygame_display_circle()

def pygame_display_image(path):
    if path:
        pygame.init()

        window = pygame.display.set_mode([400, 400])

        pygame.display.set_caption('Image Display Tutorial')

        # image = pygame.image.load(r'img_bg.jpg')
        image = pygame.image.load(path)

        playing = True

        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False

            window.fill((255, 255, 255))
            window.blit(image, (0, 0))

            pygame.display.update()

        pygame.quit()
    else:
        print("Please provide path to the image")

# pygame_display_image('img_bg.jpg')

def pygame_display_text():

    pygame.init()

    window = pygame.display.set_mode([400, 400])

    pygame.display.set_caption('Display text')

    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render('Tutorials', True, (0, 255, 0), (0, 0, 128))

    textRect = text.get_rect()
    textRect.center = (400 // 2, 400 // 2)

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        window.fill((255, 255, 255))
        window.blit(text, textRect)

        pygame.display.update()

    pygame.quit()

# pygame_display_text()

def pygame_draw_on_key_pressed():

    pygame.init()

    window = pygame.display.set_mode([550, 550])

    pygame.display.set_caption('Key press listenner')
    # Test run
    # playing = True

    # while playing:
    #     event = pygame.event.wait()
    #     if event.type == pygame.QUIT:
    #         break

    #     if event.type in (pygame.KEYUP, pygame.KEYDOWN):
    #         key_name = pygame.key.name(event.key)
    #         key_name = key_name.upper()

    #         if event.type == pygame.KEYDOWN:
    #             print(u"{} Key pressed".format(key_name))
    #         elif event.type == pygame.KEYUP:
    #             print(u"{} Key released".format(key_name))
    
    done = False
    is_blue = True

    x = 30
    y = 30

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1

        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)
        pygame.draw.rect(window, color, pygame.Rect(x, y, 60, 60))
        pygame.display.flip()
    
    pygame.quit()

# pygame_draw_on_key_pressed()

def pygame_draw_shape():

    pygame.init()

    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    black = (0, 0, 0)
    red = (255, 0, 0)

    window = pygame.display.set_mode([500, 500])
    
    pygame.display.set_caption('Drawing Shapes')
    
    window.fill(white)

    pygame.draw.polygon(window, blue, [(146, 0), (291, 106), (236, 277), (56, 277), (0, 106)])

    pygame.draw.line(window, green, (65, 350), (120, 350), 4)

    pygame.draw.circle(window, red, (350, 50), 20, 0)

    pygame.draw.ellipse(window, black, (300, 250, 40, 80), 3)
    
    pygame.draw.rect(window, green, (150, 300, 100, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
    
    pygame.quit()

# pygame_draw_shape()

def move_object():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((127, 128, 205))

        pygame.draw.circle(screen, "red", player_pos, 20)

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP] and player_pos.y > 23:
        if keys[pygame.K_UP] and player_pos.y > 0 - dt:
            player_pos.y -= 300 * dt
        # if keys[pygame.K_DOWN] and player_pos.y < 478:
        if keys[pygame.K_DOWN] and player_pos.y < 500 - dt:
            player_pos.y += 300 * dt
        if keys[pygame.K_LEFT] and player_pos.x > 23:
            player_pos.x -= 300 * dt
        if keys[pygame.K_RIGHT] and player_pos.x < 478:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

# move_object()