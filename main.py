import pygame,sys
from grid import Grid
from gridstack import GridStack, Cell
from position import Position
from myturn import *

dark_blue=(44,44,127)

pygame.init()
screen = pygame.display.set_mode((500, 620))

pygame.display.set_caption("Python Maze")

clock=pygame.time.Clock()

game_grid = Grid()
game_grid.Set(GridStack().get_grid())
game_grid.print_grid()

stop = False

def Run():
    global stop
    now = Position(-1,-1)
    dest = Position(-1,-1)
    for y,row in enumerate(game_grid.Map()):
        for x,item in enumerate(row):
            if item == Cell.PLAYER.value:
                now.x = x
                now.y = y
            elif item == Cell.DESTINATION.value:
                dest.x = x
                dest.y = y
    assert dest.x >= 0 and dest.y >= 0 and now.x >= 0 and now.y >= 0
    result, x, y = DoMove( game_grid.num_rows,
                   game_grid.num_cols,
                   game_grid.grid)
    if result == 1:
        if x != dest.x or y != dest.y:
            game_grid.grid[now.y][now.x] = Cell.PASS.value
            game_grid.grid[y][x] = Cell.PLAYER.value
            stop = False
            return
        else:
            game_grid.grid[now.y][now.x] = Cell.PASS.value
            game_grid.grid[y][x] = Cell.PLAYER.value

    stop = True
    return

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not stop:
        Run()

    #Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(2)

