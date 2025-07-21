# BONK needs fixing !!!!!

import pygame
import sys
import os
# start pygame
pygame.init()


# Change to a specific directory
os.chdir("Pythongamelol/")

# Parameters for window size
width, height = 1200, 680

# Setting the window's size
screen = pygame.display.set_mode((width, height))

# Window name (yes)
pygame.display.set_caption("Fuck you")

running = True

collision_active = False

# Alright this is for the circle. Size, speed etc idk
x_circle = 300
y_circle = 200
speed_circle = 3
radius_circle = 30
flash_timer = 0
# Color
color_circle = 1
color_rect = 1

colory_rect = 45, 48, 77
colory_circle = 209, 132, 240
coloryy1 = 209, 132, 240
coloryy2 = 184, 224, 255
coloryy3 = 255, 236, 153
coloryy4 = 45, 48, 77

x_rect = 500
y_rect = 400
speed_rect = 3
size_rect = 60

# This is for the rectangle
clock = pygame.time.Clock() #the games clock or sum

# WRITE CODE IN HERE FOR THE WINDOW YESYES
while running:
    clock.tick(60) # FPS set to 60
    bonk_sound = pygame.mixer.Sound("bonk.wav")
    closest_x = max(x_rect, min(x_circle, x_rect + size_rect))
    closest_y = max(y_rect, min(y_circle, y_rect + size_rect))
    dx = x_circle - closest_x
    dy = y_circle - closest_y
    is_colliding = dx**2 + dy**2 < radius_circle**2

    if is_colliding and not collision_active:
        bonk_sound.play()
        collision_active = True
        flash_timer = 5
    
    if not is_colliding:
        collision_active = False

    if flash_timer > 0:
        draw_color_circle = (255,255,255)
        draw_color_rect = (255,255,255)
    else:
        draw_color_circle = colory_circle
        draw_color_rect = colory_rect

    if flash_timer > 0:
        flash_timer -= 1
    def draw_glowing_circle(surface, color, center, radius):
    # Glow layers
        glow_colors = [
            (*color, 30),
            (*color, 50),
            (*color, 80),
        ]
        sizes = [radius + 30, radius + 20, radius + 10]

        # Draw from outermost to innermost
        for glow_color, size in zip(glow_colors, sizes):
            glow_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, glow_color, (size, size), size)
            surface.blit(glow_surface, (center[0] - size, center[1] - size))

    # Actual circle (core)
        pygame.draw.circle(surface, color, center, radius)
       

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                color_circle = (color_circle % 4) + 1
                color_rect = (color_rect % 4) + 1

                print("The color_circle currrently is: " + str(color_circle) + "and the color_rect currently is: " + str(color_rect))

       
        if color_circle == 1:
            colory_circle = coloryy1
            colory_rect = coloryy4
        elif color_circle == 2:
            colory_circle = coloryy2
            colory_rect = coloryy3
        elif color_circle == 3:
            colory_circle = coloryy3
            colory_rect = coloryy2
        elif color_circle == 4:
            colory_circle = coloryy4
            colory_rect = coloryy1

     # Save current position before moving
    prev_x_circle = x_circle
    prev_y_circle = y_circle
    prev_x_rect = x_rect
    prev_y_rect = y_rect
        
    # For the ball lol yes yes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_circle -= speed_circle

    if keys[pygame.K_RIGHT]:
        x_circle += speed_circle
    
    if keys[pygame.K_UP]:
        y_circle -= speed_circle

    if keys[pygame.K_DOWN]:
        y_circle += speed_circle

    if keys[pygame.K_w]:
        y_rect -= speed_rect
    
    if keys[pygame.K_d]:
        x_rect += speed_rect
    if keys[pygame.K_a]:
        x_rect -= speed_rect
    if keys[pygame.K_s]:
        y_rect += speed_rect

    if keys[pygame.K_SPACE]:
        speed_circle = 6
        draw_glowing_circle(screen, draw_color_circle, (x_circle, y_circle), radius_circle)

    else:
        speed_circle = 3
        pygame.draw.circle(screen, draw_color_circle, (x_circle, y_circle), radius_circle)

    if keys[pygame.K_j]:
        if size_rect < 360:
            size_rect += 1
        else:
            size_rect = size_rect
    if keys[pygame.K_f]:
        if size_rect > 60:
            size_rect -= 1
        else:
            size_rect = size_rect
    # Border
    x_circle = max(radius_circle, min(width - radius_circle, x_circle))
    y_circle = max(radius_circle, min(height - radius_circle, y_circle))



    
    x_rect = max(0, min(width - size_rect, x_rect))
    y_rect = max(0, min(height - size_rect, y_rect))

    # BACKGROUND
    screen.fill((30,30, 30))




    if dx**2 + dy**2 < radius_circle**2:
        # Collision happened → revert to previous position
        x_circle = prev_x_circle
        y_circle = prev_y_circle
        # Rect object for collision detection
        rect_obj = pygame.Rect(x_rect, y_rect, size_rect, size_rect)
        
    # After moving the rect

    # Closest point on the circle to the rect center
    circle_center = (x_circle, y_circle)
    rect_center_x = x_rect + size_rect / 2
    rect_center_y = y_rect + size_rect / 2

    # Find closest point on circle to rect
    dxrect = circle_center[0] - rect_center_x
    dyrect = circle_center[1] - rect_center_y
    distance_squared = dxrect**2 + dyrect**2

    # Minimum distance = circle radius + half of rect size
    min_distance = radius_circle + size_rect / 2

    if distance_squared < min_distance**2:
        # Collision → revert rect move
        x_rect = prev_x_rect
        y_rect = prev_y_rect

    
    # The fucking ball..
 
    pygame.draw.rect(screen, draw_color_rect, pygame.Rect(x_rect, y_rect, size_rect, size_rect))
    # Update Frame
    pygame.display.flip()

pygame.quit()
sys.exit()