# Simple Chess Game

This project is a chess game developed using Python and Pygame. It provides a graphical interface where players can interactively move chess pieces on an 8x8 board. The game supports basic chess mechanics, including piece selection, movement highlighting, and capturing opponent pieces, offering an engaging experience for chess enthusiasts and those interested in game development with Pygame.

![image](https://github.com/user-attachments/assets/11e98566-e67d-4b93-8678-5e9821b23ac4)

## Features

- **Interactive Chessboard**: An 8x8 grid representing the chessboard with alternating colored squares for clear visualization.
- **Piece Movement**: Supports movement for all standard chess pieces including Pawns, Knights, Bishops, Rooks, Queens, and Kings with basic movement rules.
- **Visual Indicators**: Highlights possible moves for selected pieces, providing visual feedback to enhance gameplay.
- **Piece Capturing**: Allows players to capture opponent pieces by moving their pieces to occupied squares.
- **Dynamic Scaling**: Automatically scales piece images to fit the board resolution for optimal display quality.

## Requirements

- **Python 3.x**
- **Pygame**: Install via pip with `pip install pygame`

## Game Controls

- **Mouse Click**:
  - **Left Click** on a piece to select it.
  - **Left Click** on a highlighted square to move the selected piece to that position.

## Project Structure

- **main.py**: The main script that initializes the game, handles the game loop, rendering, and user interactions.
- **images/**: Directory containing all the chess piece images used in the game, organized by piece type and color.
- **map Initialization**: Sets up the initial positions of all chess pieces on the board.

## Game Mechanics

- **Piece Selection**: Click on a piece to select it. The game highlights all possible moves based on the selected piece's movement rules.
- **Movement Rules**: Each piece follows standard chess movement rules:
  - **Pawn**: Moves forward one square, with the option to move two squares from its starting position. Captures diagonally.
  - **Knight**: Moves in an L-shape: two squares in one direction and then one square perpendicular.
  - **Bishop**: Moves diagonally any number of squares.
  - **Rook**: Moves horizontally or vertically any number of squares.
  - **Queen**: Combines the movement of the rook and bishop.
  - **King**: Moves one square in any direction.
- **Capturing**: Moving a piece to a square occupied by an opponent's piece captures it, removing it from the board.

## Customization

You can modify various settings and parameters to enhance or alter the experience:

- **Screen Resolution**: Adjust the `resolution` variable to change the size of the game window.
- **Piece Images**: Replace or update images in the `images/` directory to customize the appearance of chess pieces.
- **Initial Setup**: Modify the `map` initialization section to change the starting positions of the pieces or create custom board setups.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0).

### Additional Note on Commercial Use
**Commercial use of this software or any derived works is prohibited without prior written permission from the original author.** For commercial licensing inquiries, please contact loan.tremoulet.breton@gmail.com.
