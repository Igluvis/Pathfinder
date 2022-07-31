import pygame
from core.utils.grid import Grid
from core.pygame.visualize import draw
from core.pygame.misc import get_node, algo_clock
from core.pathfinder.a_star import a_star
from core.pathfinder.breadth_first import breadth_first
from core.mazebuilder.binary_maze import binary_maze
from core.mazebuilder.sidewinder import sidewinder

clock = pygame.time.Clock()

def main(win, width, height, rows, cols):
    '''
    main pygame loop
        win: pygame.window
        width: width of window
        height: height of window
    '''
    # fps
    fps = 60
    gear = 2  # gear translator for fps : 0 = 30, 1 = 60, 2 = 120

    # create grid
    grid = Grid(rows, cols)

    # functional nodes
    start = None
    end = None
    
    # run loop
    run = True
    waiting = True

    while run:
        # update screen
        draw(win, grid, width, height, rows, cols)
        clock.tick(fps)

        for event in pygame.event.get():
            # Escape
            if event.type == pygame.QUIT:
                run = False

            if waiting:
                # Mouse
                # left mouse: set wall node
                if pygame.mouse.get_pressed()[0]:
                    node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                    if not node.get_start() and not node.get_end():
                        node.set_wall()

                # right mouse: set walk node
                if pygame.mouse.get_pressed()[2]:
                    node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                    if not node.get_start() and not node.get_end():
                        node.set_walkable()

                # Keyboard
                if event.type == pygame.KEYDOWN:
                    # Q: set Start node
                    if event.key == pygame.K_q:
                        if start:
                            start.set_walkable()
                        node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                        node.set_start()
                        start = node

                    # E: set End node
                    if event.key == pygame.K_e:
                        if end:
                            end.set_walkable()
                        node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                        node.set_end()
                        end = node

                    # Space: start pathfinding visualizer
                    if event.key == pygame.K_SPACE and start and end:
                        a_star(
                            lambda: draw(win, grid, width, height, rows, cols),
                            lambda: clock.tick(algo_clock(gear)),
                            start=start,
                            end=end,
                            grid=grid
                        )
                        waiting = False

                    # M: start mazebuilder
                    if event.key == pygame.K_m and start and end:
                        grid.cleanup()
                        sidewinder(
                            lambda: draw(win, grid, width, height, rows, cols),
                            lambda: clock.tick(algo_clock(gear)),
                            start=start,
                            end=end,
                            grid=grid
                        )
                    
                    # R: Reset
                    if event.key == pygame.K_r:
                        start = None
                        end = None
                        grid.make_blank()
            
            # not waiting
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    grid.cleanup()
                    waiting = True


    pygame.quit()