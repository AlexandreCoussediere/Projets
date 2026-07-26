import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# fenetre
width, height = 720, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame")

# constants

CELL_SIZE = 24
GRID_SIZE = width // CELL_SIZE
FPS = 10

# couleur

SNAKE_COLOR = (0, 100, 0)
BACKROUND_COLOR = (114, 239, 145)
APPLE_COLOR = (255, 0, 0)
BORDER_COLOR = (165, 42, 42)
SCORE_COLOR = (0, 0, 0)

# police

font = pygame.font.Font(None, 36)

# ===== CLASSES =====

class Snake:
    def __init__(self):
        self.positions = [(5, 5), (4, 5), (3, 5)]
        self.direction = (0, 1)
        self.grow = False


    def move(self):
        head_x, head_y = self.positions[0]
        delta_x, delta_y = self.direction
        new_head = (head_x + delta_x, head_y + delta_y)

        if (new_head in self.positions or not(1 <= new_head[0] < GRID_SIZE - 1 and 1 <= new_head[1] < GRID_SIZE - 1)):
            return False

        self.positions.insert(0, new_head)

        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False

        return True


    def change_direction(self, direction):
        current_x, current_y = self.direction
        opposite_direction = (-current_x, -current_y)

        if direction != opposite_direction:
            self.direction = direction


    def grow_snake(self):
        self.grow = True


    def draw(self, surface):
        for x, y in self.positions:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, SNAKE_COLOR, rect)

        # add eyes to the snake
        head_x, head_y = self.positions[0]
        eye1 = pygame.Rect(head_x * CELL_SIZE + 8, head_y * CELL_SIZE + 8, 5, 5)
        eye2 = pygame.Rect(head_x * CELL_SIZE + 17, head_y * CELL_SIZE + 8, 5, 5)
        pygame.draw.rect(surface, (0, 0, 0), eye1)
        pygame.draw.rect(surface, (0, 0, 0), eye2)

class Apple:
    def __init__(self, snake):
        self.position = self.random_position(snake)


    def random_position(self, snake):
        while True:
            x = random.randint(1, GRID_SIZE - 2)
            y = random.randint(1, GRID_SIZE - 2)
            position = (x, y)
            if position not in snake.positions:
                return position


    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, APPLE_COLOR, rect)

# fonctions pour le jeux

def draw_backround(surface):
    surface.fill(BACKROUND_COLOR)


def draw_border(surface):
    pygame.draw.rect(surface, BORDER_COLOR, pygame.Rect(0, 0, width, height), CELL_SIZE)


def display_score(surface, score):
    text = font.render(f"Score : {score}", True, SCORE_COLOR)
    surface.blit(text, (10, 10))


def game_over_screen(surface, score):
    draw_backround(surface)
    game_over_text = font.render("GAME OVER", True, SCORE_COLOR)
    score_text = font.render(f"Score : {score}", True, SCORE_COLOR)
    restart_text = font.render("Press space to Restart", True, SCORE_COLOR)
    surface.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2 + 50))
    surface.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2))
    surface.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 - restart_text.get_height() // 2 - 50))


def victory_screen(surface, score):
    draw_backround(surface)
    victory_text = font.render("GAME OVER", True, SCORE_COLOR)
    score_text = font.render(f"Score : {score}", True, SCORE_COLOR)
    restart_text = font.render("Press space to Restart", True, SCORE_COLOR)
    surface.blit(victory_text, (width // 2 - victory_text.get_width() // 2, height // 2 - victory_text.get_height() // 2 + 50))
    surface.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2))
    surface.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 - restart_text.get_height() // 2 - 50))


def main():

    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple(snake)
    score = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
                elif event.key == pygame.K_SPACE:
                    if not running:
                        main()

        if not snake.move():
            game_over_screen(screen, score)
            pygame.display.flip()
            running = False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            main()

        if snake.positions[0] == apple.position:
            snake.grow_snake()
            apple = Apple(snake)
            score += 1

        draw_backround(screen)
        draw_border(screen)
        snake.draw(screen)
        apple.draw(screen)
        display_score(screen, score)
        pygame.display.flip()
        clock.tick(FPS)

        # check victory
        if len(snake.positions) == (GRID_SIZE - 2) * (GRID_SIZE - 2):
            victory_screen(screen, score)
            pygame.display.flip()
            running = False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        main()

# run the game

main()