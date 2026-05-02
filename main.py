#!/usr/bin/env python3
"""Connect4 - Play against the AI in the terminal."""
from game.board import Board, PLAYER, AI
from game.ai import get_ai_move


def play():
    board = Board()
    print("Connect4 - You are X, AI is O")
    print("Enter column number (0-6) to drop a piece.\n")
    print(board)

    current = PLAYER
    while True:
        if current == PLAYER:
            try:
                col = int(input("\nYour move (0-6): "))
            except (ValueError, EOFError):
                print("Invalid input.")
                continue
            if not board.is_valid(col):
                print("Column full or invalid. Try again.")
                continue
            board.drop_piece(col, PLAYER)
        else:
            print("\nAI is thinking...")
            col = get_ai_move(board, depth=5)
            board.drop_piece(col, AI)
            print(f"AI plays column {col}")

        print()
        print(board)

        if board.check_win(current):
            winner = "You win!" if current == PLAYER else "AI wins!"
            print(f"\n🎉 {winner}")
            break
        if board.is_full():
            print("\n🤝 It's a draw!")
            break

        current = AI if current == PLAYER else PLAYER


if __name__ == "__main__":
    play()
