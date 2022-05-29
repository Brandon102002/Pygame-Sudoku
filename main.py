import pygame

pygame.font.init()

screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("Sudoku Solver")
img = pygame.image.load('background.jpg')
pygame.display.set_icon(img)

pygame.quit()    