# CLI Tic Tac Toe

A simple, interactive Command Line Interface (CLI) implementation of the classic Tic Tac Toe game written in Python. This game allows two players to play against each other on the same terminal.

**Disclaimer:** *This code is yet to be improved fully.* It currently serves as a functional foundational script.

## Features

* **Two-Player Mode:** Designed for two human players sharing the same terminal.

* **Randomized Starts:** The game fairly selects either 'X' or 'O' to make the first move using Python's `random` module.

* **Real-time Win and Draw Detection:** The system automatically checks for horizontal, vertical, and diagonal win conditions, as well as gridlock (draw) scenarios after every turn.

* **Basic Input Validation:** Ensures players select valid rows and columns within the 1-3 range and prevents overwriting an already occupied cell.

## Prerequisites

To run this game, you must have Python installed on your system (Python 3.x is recommended). No additional external libraries or dependencies are required.

## Installation & Usage

1. Clone or download the repository to your local machine.

2. Ensure you have the game file saved as `Tic_Tac_Toe.py`.

3. Open your terminal or command prompt.

4. Navigate to the directory where the file is located.

5. Run the game using the following command:

```
python Tic_Tac_Toe.py


```

## How to Play

1. Upon starting the game, the terminal will announce which player ('X' or 'O') gets to go first.

2. The current state of the 3x3 board will be displayed.

3. When prompted, enter the **row** number (1, 2, or 3) and press Enter.

4. Next, enter the **column** number (1, 2, or 3) and press Enter.

5. The board will update with your move.

6. Players alternate turns until someone wins or the board fills up, resulting in a draw.