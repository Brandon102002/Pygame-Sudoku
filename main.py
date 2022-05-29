import pygame

"""A simple sudoku puzzle generator and solver with backtracking. 
    Requires Pygame."""

pygame.font.init()

screenWidth = 500
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Sudoku Solver")

numFont = pygame.font.get_fonts()
hoverColor = (255, 0, 0)
backgroundColor = (255, 255, 255)
fillColor = (0, 153, 153)

# Temp manual board. Will generate later
board = [
    [0, 0, 9, 8, 0, 7, 2, 5, 0],
    [0, 8, 0, 0, 0, 0, 7, 3, 0],
    [0, 0, 0, 5, 0, 3, 0, 6, 8],
    [8, 0, 0, 1, 0, 0, 4, 7, 9],
    [5, 9, 0, 3, 8, 4, 0, 0, 6],
    [0, 0, 0, 7, 9, 0, 0, 8, 5],
    [0, 7, 6, 4, 5, 0, 8, 0, 2],
    [0, 0, 0, 6, 0, 8, 5, 9, 0],
    [0, 0, 0, 0, 7, 1, 0, 4, 0]
]

x = 0
y = 0
# Adjustment for coordinates of 9 cells
adj = screenWidth / 9
val = 0


def updateCoords(pos):
    global x, y
    x = pos[0] // adj
    y = pos[1] // adj


def highlightBox():
    for i in range(2):
        pygame.draw.line(screen, hoverColor, (x * adj - 3, (y + i) * adj), (x * adj + adj + 3, (y + i) * adj), 7)
        pygame.draw.line(screen, hoverColor, ((x + i) * adj, y * adj), ((x + i) * adj, y * adj + adj), 7)


def setBoard():
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                pygame.draw.rect(screen, fillColor, (row * adj, col * adj, adj + 1, adj + 1))
                numToPlace = numFont.render(str(board[row][col]), 1, (0, 0, 0))
                screen.blit(numToPlace, (row * adj + 15, col * adj + 15))
    for i in range(10):
        i


def setNum(num):
    numToPlace = numFont.render(str(num), 1, (0, 0, 0))
    screen.blit(numToPlace, (x * adj + 15, y * adj + 15))


def validPlacement(board, xIndex, yIndex, num):
    for i in range(9):
        if board[xIndex][i] == num or board[i][yIndex] == num:
            return False
    localX = xIndex // 3
    localY = yIndex // 3
    for row in range(localX * 3, localX * 3 + 3):
        for col in range(localY * 3, localY * 3 + 3):
            if board[row][col] == num:
                return False
    return True


#def solve(board, )


run = True

while run:
    screen.fill(backgroundColor)

    for event in pygame.event.get():
        if event.type == pygame.quit():
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:


    pygame.display.update()

pygame.quit()
