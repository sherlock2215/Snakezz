# Snakezz 🐍

A professional Python implementation of the classic Snake game using Pygame. Features clean, modular code and proper software architecture.

![Python Badge](https://img.shields.io/badge/Python-3.8%252B-blue)  
![Pygame Badge](https://img.shields.io/badge/Pygame-2.5.1-green)

---

## Features
- 🎮 Classic Snake gameplay with smooth controls
- 🏗️ Modular, object-oriented design
- ⚙️ Centralized configuration system
- 🍎 Visual apple assets with fallback rendering
- 📊 Score tracking
- 🎯 Collision detection (walls & self)

---

## Installation

### Clone the repository
```bash
git clone https://github.com/sherlock2215/Snakezz.git
cd Snakezz
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## How to Play

### Run the game:
```bash
python src/main.py
```

### Controls:
- Use **Arrow Keys** to control the snake direction
- Eat the red apples to grow and score points
- Avoid hitting walls and yourself
- Press **SPACE** to restart after game over

---

## Project Structure
```
Snakezz/
├── src/                 # Source code
│   ├── main.py         # Game entry point
│   ├── game.py         # Main game class
│   ├── snake.py        # Snake character class
│   ├── food.py         # Food/apple class
│   └── config.py       # Game configuration
├── assets/             # Game assets
│   └── images/         # Image files
├── requirements.txt    # Python dependencies
└── README.md           # This file
```


## Code Quality
- Formatted with **Black** for consistent code style
- Modular design following **separation of concerns**
- Comprehensive documentation with **docstrings**
- Error handling for asset loading
- Clean class architecture

---

## Development
This project demonstrates:
- Object-oriented programming principles
- Game development with Pygame
- Professional code organization
- Collision detection algorithms
- Game state management

---

## License
This project is open source and available under the **MIT License**.
