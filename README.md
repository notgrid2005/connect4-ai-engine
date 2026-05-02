# 🎮 Connect4 AI Engine

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

An AI-powered Connect4 game using **Minimax with Alpha-Beta Pruning**.

## Features
- Full game logic with win/draw detection
- AI opponent with configurable search depth
- Heuristic board evaluation (center control, threat detection)
- Alpha-beta pruning for efficient search
- Terminal-based gameplay

## Quick Start
```bash
pip install numpy
python main.py
```

## How the AI Works
1. **Minimax** explores all possible future game states
2. **Alpha-Beta Pruning** eliminates branches that can't affect the outcome
3. **Heuristic Evaluation** scores board positions based on piece alignment and center control

## Project Structure
```
connect4-ai-engine/
├── game/
│   ├── __init__.py
│   ├── board.py    # Board representation & win detection
│   └── ai.py       # Minimax + Alpha-Beta + Evaluation
├── main.py          # Terminal gameplay
└── README.md
```
