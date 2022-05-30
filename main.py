import pygame
"""A simple sudoku puzzle generator and solver with backtracking. 
    Requires Pygame."""

pygame.font.init()

screenWidth = 501
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Sudoku Solver")

numFont = pygame.font.SysFont("comicsans", 40)
textFont = pygame.font.SysFont("comicsans", 20)

hoverColor = (255, 0, 0)
backgroundColor = (255, 255, 255)
fillColor = (220, 220, 220)
zeroColor = (0, 0, 0)

# Temporary manual board. Will work on board generation later
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
num = 0


# Give coordinates in terms of boxes
def updateCoords(pos):
    global x, y
    x = pos[0] // adj
    y = pos[1] // adj


# Highlight the current selected box
def highlightBox():
    for i in range(2):
        pygame.draw.line(screen, hoverColor, (x * adj - 3, (y + i) * adj), (x * adj + adj + 3, (y + i) * adj), 7)
        pygame.draw.line(screen, hoverColor, ((x + i) * adj, y * adj), ((x + i) * adj, y * adj + adj), 7)


# Update the visuals to the current board
def setBoard():
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                pygame.draw.rect(screen, fillColor, (row * adj, col * adj, adj + 1, adj + 1))
                numToPlace = numFont.render(str(board[row][col]), 1, (0, 0, 0))
                screen.blit(numToPlace, (row * adj + 15, col * adj))
    for i in range(10):
        thickness = 6 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0,), (0, i * adj), (500, i * adj), thickness)
        pygame.draw.line(screen, (0, 0, 0,), (i * adj, 0), (i * adj, 500), thickness)


# Set a number on the board
def setNum(num):
    numToPlace = numFont.render(str(num), 1, zeroColor)
    screen.blit(numToPlace, (x * adj + 15, y * adj + 15))


# Returns whether a placement is valid by Sudoku rules
def validPlacement(board, xIndex, yIndex, num):
    for i in range(9):
        if board[xIndex][i] == num or board[i][yIndex] == num:
            return False
    localX, localY = xIndex // 3, yIndex // 3
    for row in range(localX * 3, localX * 3 + 3):
        for col in range(localY * 3, localY * 3 + 3):
            if board[row][col] == num:
                return False
    return True


# Iterates through empty spaces and recursively tries all valid placements.
# Handles cells with no valid placements by backtracking
def solve(board, row, col):
    while board[row][col] != 0:
        if row < 8:
            row += 1
        elif row == 8 and col < 8:
            row = 0
            col += 1
        elif row == 8 and col == 8:
            return True
    pygame.event.pump()
    for val in range(1, 10):
        if validPlacement(board, row, col, val):
            board[row][col] = val

            global x, y
            x, y = row, col
            screen.fill(backgroundColor)
            setBoard()
            highlightBox()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(board, row, col) == 1:
                return True
            else:
                board[row][col] = 0
            screen.fill(backgroundColor)
            setBoard()
            highlightBox()
            pygame.display.update()
            pygame.time.delay(20)
    return False


# Throws an error for an invalid placement
def errorInvalid():
    text = numFont.render("Invalid Placement", 1, zeroColor)
    screen.blit(text, (20, 570))


# Throws an error for an incorrect board
def errorIncorrect():
    text = numFont.render("Incorrect", 1, zeroColor)
    screen.blit(text, (20, 570))


# Displays instructions under the board
def instructions():
    textReset = textFont.render("Press R to reset the board", 1, zeroColor)
    textClear = textFont.render("Press C to clear the board", 1, zeroColor)
    textSolve = textFont.render("Press Enter to auto-solve", 1, zeroColor)
    screen.blit(textReset, (20, 510))
    screen.blit(textClear, (20, 535))
    screen.blit(textSolve, (20, 560))


run = True
flag1 = 0
flag2 = 0
error = 0

# Main game loop
while run:
    screen.fill(backgroundColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            updateCoords(pos)
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    x -= 1
                    flag1 = 1
                case pygame.K_RIGHT:
                    x += 1
                    flag1 = 1
                case pygame.K_UP:
                    y -= 1
                    flag1 = 1
                case pygame.K_DOWN:
                    y += 1
                    flag1 = 1
                case pygame.K_1:
                    num = 1
                case pygame.K_2:
                    num = 2
                case pygame.K_3:
                    num = 3
                case pygame.K_4:
                    num = 4
                case pygame.K_5:
                    num = 5
                case pygame.K_6:
                    num = 6
                case pygame.K_7:
                    num = 7
                case pygame.K_8:
                    num = 8
                case pygame.K_9:
                    num = 9
                case pygame.K_RETURN:
                    flag2 = 1
                case pygame.K_r:
                    error = 0
                    flag2 = 0
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
                case pygame.K_c:
                    board = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
    if flag2 == 1:
        if not solve(board, 0, 0):
            error = 1
        flag2 = 0
    if num != 0:
        setNum(num)
        if validPlacement(board, int(x), int(y), num):
            board[int(x)][int(y)] = num
            flag1 = 0
        else:
            board[int(x)][int(y)] = 0
            errorInvalid()
        num = 0
    if error == 1:
        errorIncorrect()
    setBoard()
    if flag1 == 1:
        highlightBox()
    instructions()

    pygame.display.update()

pygame.quit()
