# chesspy
Chesspy is part of a school project and involves the development of a chess game where two clients are synchronized through a server using sockets.

# Table of contents
- [Introduction](#chesspy)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)
- [Usage](#usage)

# Installation
To install and run this chess game project, you will need to follow the steps outlined below.

## Prerequisites
- Python 3.5 or higher installed on your computer

## Installation Steps
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
