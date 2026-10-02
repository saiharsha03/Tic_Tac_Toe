# Tic Tac Toe

A two-player Tic Tac Toe game drawn with Python's `turtle` module.

Players take turns clicking a square. X is drawn in yellow and O in red. The game detects a win or a draw, shows the result, and starts a new round when you click again. Close the window to quit.

## Run it

```bash
python draw.py
```

`turtle` ships with Python, so there is nothing to install.

## How it works

`draw.py` draws the board with turtle, maps each click to one of the nine squares, records each player's squares, and checks them against the winning lines after every move.
