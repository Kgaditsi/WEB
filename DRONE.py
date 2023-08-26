import pygame
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Medication Delivery Drone")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Drone properties
drone_size = 20
drone_x = width // 2
drone_y = height - drone_size

# Medication drop-off point
dropoff_x = width // 3
dropoff_y = height // 4

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the drone
    pygame.draw.circle(screen, blue, (drone_x, drone_y), drone_size)

    # Draw the drop-off point
    pygame.draw.circle(screen, blue, (dropoff_x, dropoff_y), 10)

    # Move the drone towards the drop-off point
    if drone_y > dropoff_y:
        drone_y -= 1

    # Check if medication has been delivered
    if drone_y <= dropoff_y:
        time.sleep(1)  # Simulate medication drop
        print("Medication delivered!")
        running = False

    pygame.display.flip()

pygame.quit()