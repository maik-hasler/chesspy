# chesspy
Chesspy is a chess game developed as part of a school project. It involves the development of a multiplayer chess game where two clients are synchronized through a server using sockets. The game logic is based on inheritance, with a base Piece class and individual inherited classes for each type of chess piece. Each inherited class has specific methods for calculating valid moves based on the rules of chess. These methods are then called by the main game logic to check whether a move is valid.

When the server is started, it waits for two clients to connect, assigns each a player index, and creates a new game in the SQLite database. The initial chess board state is then rendered with the two clients and sent to them as bytes using pickle. The clients use the Pygame library to render the chess board to the user interface and allow the user to select and move pieces.

When a client moves a piece, the user interface sends the move to the server as bytes, which deserializes the move back into a Python object. The server then verifies that the move is valid by calling the appropriate method in the piece's inherited class. If the move is valid, the server applies it to the chess board state and saves the move to the SQLite database.

After applying the move, the server synchronizes the updated chess board state with both clients by sending the board state and the index of the current player to each client as bytes using pickle. The client then renders the updated chess board to the user interface, and the game continues until one player is in checkmate or the game is otherwise ended.

# Table of contents
- [Introduction](#chesspy)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation steps](#installation-steps)
- [Usage](#usage)

# Installation
To install and run this chess game project, you will need to follow the steps outlined below.

## Prerequisites
- Python 3.5 or higher installed on your computer
- Requirements listed in the `requirements.txt`

## Installation steps
1. Clone the repository:
```
https://github.com/maik-hasler/chesspy
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

# Usage
To use this chess game project, you will need to follow the steps outlined below.

1. First, you need to start a server instance. The server is responsible for synchronizing the chessboard with the connected clients. You can start the server using the following command:
```
python server.py
```
2. Once the server is up and running, you need to start two client instances that will connect to the server. You can start the clients using the following command:
```
python client.py
```
After starting the clients, they will connect to the server and wait for the other client to join. Once both clients have joined, the game will start, and they can begin playing.
