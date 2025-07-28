import pygame
import pymunk
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)

def create_ball(pos):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 15))
    body.position = pos
    shape = pymunk.Circle(body, 15)
    shape.elasticity = 0.6
    space.add(body, shape)

def create_floor():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (50, 550), (750, 550), 5)
    shape.elasticity = 0.8
    space.add(body, shape)

create_floor()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_ball(pygame.mouse.get_pos())

    screen.fill((30, 30, 30))
    
    for shape in space.shapes:
        if isinstance(shape, pymunk.Circle):
            x, y = shape.body.position
            pygame.draw.circle(screen, (200, 50, 50), (int(x), int(y)), int(shape.radius))
        elif isinstance(shape, pymunk.Segment):
            p1 = shape.a
            p2 = shape.b
            pygame.draw.line(screen, (255, 255, 255), p1, p2, 5)

    space.step(1/60)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
