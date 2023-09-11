# Conway's Game of Life
A simple implementation of John Horton Conway's cellular automaton Game of Life. Game of Life is classified as a zero-player game which the future state and evolution is determined by the initial state of the trajectory. 

The code generates the initial pattern randomly which the populated proportion of the map could be defined initially (Default: 0.1 [%10]) as well as the screen and the block size. The next generation will be iterated abd mapped by analysing the current status of each cell.

# Rules
- Any live cell with fewer than two live neighbours dies (underpopulation).

- Any live cell with two or three live neighbours survives on to the next generation.

- Any live cell with more than three live neighbours dies (overpopulation).

- Any dead cell with exactly three live neighbours becomes a live cell (reproduction).

# Requirements
Python >3.6 and pygame
- pip install -r requirements.txt

# License
MIT
