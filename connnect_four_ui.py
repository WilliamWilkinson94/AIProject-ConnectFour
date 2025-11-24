import pygame
import sys
import search
from Connect_Four import ConnectFour

pygame.init()
WIDTH = 700
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four - A* Serach Bot")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

COLS = 7
ROWS = 6
CELL = WIDTH // COLS


def draw_board(board):
    WIN.fill(BLUE)

    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(WIN, BLUE, (c*CELL, r*CELL, CELL, CELL))
            pygame.draw.circle(
                WIN,
                WHITE if board[c][r] == "E" else (
                    RED if board[c][r] == "R" else YELLOW), (c*CELL + CELL // 2, r*CELL + CELL//2), CELL // 2-5
            )
    pygame.display.update()


def drop_piece(board, col, piece):
    board = [list(col_list) for col_list in board]

    for row in range(ROWS-1, -1, -1):
        if board[col][row] == "E":
            board[col][row] = piece
            return tuple(tuple(x) for x in (board))
    return None


def get_column_from_mouse(pos):
    x = pos[0]
    return x // CELL


def main():
    initial_board = tuple(tuple("E" for _ in range(ROWS)) for _ in range(COLS))
    game = ConnectFour((42, initial_board, 1))

    # player in yellow, bot red. Player goes first
    board = game.initial[1]
    turn = 1
    running = True

    draw_board(board)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # player move
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 1:
                col = get_column_from_mouse(pygame.mouse.get_pos())
                new_board = drop_piece(board, col, "Y")

                if new_board:
                    game = ConnectFour((game.initial[0]-1, new_board, 0))
                    board = new_board
                    turn = 0
                    draw_board(board)

                    terminal, winner = game.check_four_in_a_row(board)
                    if terminal:
                        print("Winner:", winner)
                        pygame.time.delay(2000)
                        running = False
            """
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                col = get_column_from_mouse(pygame.mouse.get_pos())
                new_board = drop_piece(board, col, "R")

                if new_board:
                    game = ConnectFour((game.initial[0]-1, new_board, 1))
                    board = new_board
                    turn = 1
                    draw_board(board)

                    terminal, winner = game.check_four_in_a_row(board)
                    if terminal:
                        print("Winner:", winner)
                        pygame.time.delay(2000)
                        running = False
            """
        # Bot Move
        if turn == 0:
            print("Bot thinking...")
            solution = search.astar_search(game)
            action = solution.solution()[0]
            new_board = drop_piece(board, action, "R")

            if new_board:
                game = ConnectFour((game.initial[0]-1, new_board, 1))
                board = new_board
                turn = 1
                draw_board(board)

                terminal, winner = game.check_four_in_a_row(board)
                if terminal:
                    print("Winner:", winner)
                    pygame.time.delay(2000)
                    running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
