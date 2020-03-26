# iport packages
import pygame, random
from pygame.locals import*

# init game
pygame.init()

#initialize game
screen_info = pygame.display.Info()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)

#initialize clock
clock = pygame.time.Clock()

#initialize a background color
color = (128, 0, 0)

def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display.flip()


if __name__ == "__main__":
  main()