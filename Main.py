import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Game')

# Load background image
background = pygame.image.load('background.jpg')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Load car images
red_car = pygame.image.load('red_car.png')
blue_car = pygame.image.load('blue_car.png')

# Set up the red car
red_car_width = 50
red_car_height = 80
red_car_x = (width - red_car_width) // 2
red_car_y = height - red_car_height - 10

# Set up the blue cars (as list of surfaces and positions)
blue_cars = []
for _ in range(5):
    blue_car_x = random.randint(0, width - 50)  # random position for the x
    blue_car_y = random.randint(-height, 0)    # random position for the y (off-screen)
    blue_cars.append([blue_car, blue_car_x, blue_car_y])  # Store the surface and position

# Set up the score
score = 0
font = pygame.font.SysFont(None, 35)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the red car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and red_car_x > 0:
        red_car_x -= 5
    if keys[pygame.K_RIGHT] and red_car_x < width - red_car_width:
        red_car_x += 5

    # Move the blue cars
    for blue_car_data in blue_cars:
        blue_car_data[2] += 5  # Move the blue car downwards
        if blue_car_data[2] > height:  # If blue car goes off screen
            blue_car_data[1] = random.randint(0, width - 50)  # Reset x position
            blue_car_data[2] = random.randint(-height, 0)  # Reset y position
            score += 1

    # Check for collisions
    for blue_car_data in blue_cars:
        if (red_car_x < blue_car_data[1] + 50 and
            red_car_x + red_car_width > blue_car_data[1] and
            red_car_y < blue_car_data[2] + 80 and
            red_car_y + red_car_height > blue_car_data[2]):
            running = False

    # Draw everything
    window.blit(background, (0, 0))
    window.blit(red_car, (red_car_x, red_car_y))
    for blue_car_data in blue_cars:
        window.blit(blue_car_data[0], (blue_car_data[1], blue_car_data[2]))  # Draw blue cars
    draw_text('Score: ' + str(score), font, white, window, 10, 10)
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
