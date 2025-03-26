
import pygame
import random
import sys


TICK_VALUE = 5
SCREEN_HEIGHT = 400
SCREEN_WEIGHT = 400
BLOCK_WEITGH = 10
BLOCK_HEIGHT = 10
INIT_POPULATION = 0.1

class GoLMapper:
    def __init__(self, scr_w:int=400, scr_h:int=400, blk_w:int=10, blk_h:int=10) -> None:
        self.scr_width = scr_w
        self.scr_height = scr_h
        self.blk_width = blk_w
        self.blk_height = blk_h
        self.surf = pygame.Surface((self.blk_width, self.blk_height))
        
    def get_random_coordinate(self):
        x_coord = random.randint(1, ((self.scr_width / self.blk_width) - 2)) * self.blk_width
        y_coord = random.randint(1, ((self.scr_height / self.blk_height) - 2)) * self.blk_height
        return x_coord, y_coord

    def get_total_cells(self) -> int:
        return (self.scr_width / self.blk_width) * (self.scr_height / self.blk_height)

    def place_random_cell(self) -> list:
        self.surf.fill((0, 0, 255), self.surf.get_rect().inflate(-1, -1))
        rect = self.surf.get_rect()
        coords = self.get_random_coordinate()
        screen.blit(self.surf, coords)
        return coords
    
    def cell_dies(self, coord:list) -> None:
        self.surf.fill((0, 0, 0))
        rect = self.surf.get_rect()
        screen.blit(self.surf, coord)
    
    def iterate(self, coords:list) -> None:
        screen.fill((0, 0, 0))
        self.surf.fill((0, 0, 250), self.surf.get_rect().inflate(-1, -1))

        rect = self.surf.get_rect()
        for coord in coords:
            screen.blit(self.surf, coord)

    def generate_init_map(self, portion:float=0.2) -> list:
        init_coords = []
        cells_to_place = int(self.get_total_cells() * portion)
        for _ in range(cells_to_place):
            coords = self.place_random_cell()
            init_coords.append(coords)
        return init_coords
    
    def faith(self, cells:int, blk_size:int=10) -> list:
        next_gen_lives = []
        for i in range(blk_size, (self.scr_width - (2 * blk_size)), blk_size):
            for j in range(blk_size, (self.scr_width - (2 * blk_size)), blk_size):
                live_neighbours = GoLMapper.count_live_neighbours((i, j), cells, blk_size)

                if (i, j) in cells:
                    if live_neighbours < 2:
                        gol_mapper.cell_dies((i, j))

                    elif live_neighbours in [2, 3]:
                        next_gen_lives.append((i, j))

                    else:
                        gol_mapper.cell_dies((i, j))

                if (i, j) not in cells and live_neighbours == 3:
                    next_gen_lives.append((i, j))

                else:
                    gol_mapper.cell_dies((i, j))
        return next_gen_lives
           
    @classmethod
    def count_live_neighbours(cls, coord:list, coords_list:list, blk_size:int=10):
        i, j = coord
        live_neighbours = sum(1 for m in range(-1, 2) for n in range(-1, 2)
                            if ((m * blk_size) + i, (n * blk_size) + j) in coords_list and ((m * blk_size) + i, (n * blk_size) + j) != (i, j))
        return live_neighbours


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life - Amin's Implementation")
    print('[CTRL-C to Abort]')
    
    screen = pygame.display.set_mode([SCREEN_WEIGHT, SCREEN_HEIGHT])
    gol_mapper = GoLMapper(SCREEN_WEIGHT, SCREEN_HEIGHT, BLOCK_WEITGH, BLOCK_HEIGHT)

    clock = pygame.time.Clock()

    init = True
    screen.fill((0, 0, 0))

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if init:
                live_cells = gol_mapper.generate_init_map(INIT_POPULATION)
                init = False
                pygame.display.flip()
                clock.tick(TICK_VALUE)
                
            next_gens = gol_mapper.faith(live_cells, BLOCK_WEITGH)
            gol_mapper.iterate(next_gens)
            live_cells = next_gens

            pygame.display.flip()
            clock.tick(TICK_VALUE)

        except KeyboardInterrupt:
            print('Aborted by user.')
            sys.exit(1)
        
        except Exception as e:
            print(e)

    pygame.quit()
