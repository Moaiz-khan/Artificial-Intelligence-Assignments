import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 600, 700

# Colors
BG_COLOR = (30, 30, 30)  # Back to black background  # White background
GRID_COLOR = (255, 255, 255)  # White grid  # Softer grid color  # Black grid for visibility
X_COLOR = (52, 152, 219)  # Blue
O_COLOR = (231, 76, 60)   # Red
TEXT_COLOR = (236, 240, 241)  # Light text for dark background  # Dark text for contrast  # White-ish

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe AI")

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 36)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 60)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 100)

X = "X"
O = "O"
EMPTY = None

user = None
board = ttt.initial_state()
ai_turn = False

def draw_board():
    screen.fill(BG_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, GRID_COLOR, (0, i * 200), (600, i * 200), 5)
        pygame.draw.line(screen, GRID_COLOR, (i * 200, 0), (i * 200, 600), 5)

def draw_moves():
    for i in range(3):
        for j in range(3):
            if board[i][j] != ttt.EMPTY:
                color = X_COLOR if board[i][j] == X else O_COLOR
                move = moveFont.render(board[i][j], True, color)
                moveRect = move.get_rect()
                moveRect.center = (j * 200 + 100, i * 200 + 100)
                screen.blit(move, moveRect)

def display_message(message):
    pygame.draw.rect(screen, BG_COLOR, (0, 600, 600, 100))
    text = mediumFont.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(width // 2, height - 50))
    screen.blit(text, text_rect)

def main():
    global user, board, ai_turn
    while True:
        draw_board()
        draw_moves()
        game_over = ttt.terminal(board)
        player_turn = ttt.player(board)

        if game_over:
            winner = ttt.winner(board)
            message = "Game Over: It's a Tie!" if winner is None else f"{winner} Wins!"
            display_message(message)
        elif user == player_turn:
            display_message(f"Your Turn ({user})")
        else:
            display_message("AI Thinking...")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row, col = y // 200, x // 200
                if board[row][col] == ttt.EMPTY and user == player_turn:
                    board = ttt.result(board, (row, col))
            
        if not game_over and user != player_turn:
            time.sleep(0.5)
            board = ttt.result(board, ttt.minimax(board))

if __name__ == "__main__":
    user = X  # Default to X starting
    main()
