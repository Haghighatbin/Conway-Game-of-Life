# Conway's Game of Life
A simple implementation of John Horton Conway's cellular automaton Game of Life. Game of Life is classified as a Game of Life is a zero-player game where the evolution of the system is entirely determined by its initial state. 

The code randomly generates the initial pattern. You can configure the population density (default: 0.1, or 10%), along with screen size and block size. Each subsequent generation is computed by analyzing the current state of each cell and applying Conway's rules.

# Rules
- Any live cell with fewer than two live neighbours dies (underpopulation).

- Any live cell with two or three live neighbours survives on to the next generation.

- Any live cell with more than three live neighbours dies (overpopulation).

- Any dead cell with exactly three live neighbours becomes a live cell (reproduction).

# Requirements and Run
Python >3.6 and pygame<br />
`pip install -r requirements.txt`
`python life.py`

# License
MIT
