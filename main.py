import pygame
import random
import sys

# ──────── Config ──────── #
WIDTH, HEIGHT = 720, 480
CELL = 20
GRID_W, GRID_H = WIDTH // CELL, HEIGHT // CELL

SNAKE_COLOR = (255, 255, 0)
APPLE_COLOR = (220, 40, 40)
SHADOW = (150, 150, 150, 60)
BG_COLOR = (230, 240, 255)
FONT_NAME = "freesansbold.ttf"

SPEED_OPTIONS = {1: 8, 2: 15, 3: 25}

# ──────── Setup ──────── #
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake in the Grass")
clock = pygame.time.Clock()
bg_image = pygame.image.load("image1.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# ──────── Helpers ──────── #
def draw_cell(surface, color, pos, radius=6):
    x, y = pos[0] * CELL, pos[1] * CELL
    rect = pygame.Rect(x, y, CELL, CELL)
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def random_cell(exclude):
    while True:
        cell = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
        if cell not in exclude:
            return cell

def render_text(text, size, color):
    font = pygame.font.Font(FONT_NAME, size)
    return font.render(text, True, color)

def draw_apple(pos):
    px = (pos[0] * CELL + CELL // 2, pos[1] * CELL + CELL // 2)
    shadow = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
    pygame.draw.circle(shadow, SHADOW, (CELL//2, CELL//2 + 3), CELL//2)
    screen.blit(shadow, shadow.get_rect(center=px))
    pygame.draw.circle(screen, APPLE_COLOR, px, CELL // 2)

def ask_for_speed():
    screen.fill(BG_COLOR)
    title = render_text("Select Speed", 50, (0, 100, 200))
    opt1 = render_text("1: Slow", 30, (0, 80, 0))
    opt2 = render_text("2: Medium", 30, (160, 100, 0))
    opt3 = render_text("3: Fast", 30, (200, 0, 0))

    screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))
    screen.blit(opt1, opt1.get_rect(center=(WIDTH//2, HEIGHT//4 + 60)))
    screen.blit(opt2, opt2.get_rect(center=(WIDTH//2, HEIGHT//4 + 100)))
    screen.blit(opt3, opt3.get_rect(center=(WIDTH//2, HEIGHT//4 + 140)))
    pygame.display.flip()

    speed = None
    while speed is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode in ['1', '2', '3']:
                    speed = SPEED_OPTIONS[int(event.unicode)]
    return speed

# ──────── Game Start ──────── #
snake_speed = ask_for_speed()
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)
apple = random_cell(set(snake))
score = 0
paused = False

# ──────── Game Loop ──────── #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_q:
                running = False

    if paused:
        pause_msg = render_text("PAUSED (Press P to resume)", 30, (255, 255, 255))
        screen.blit(pause_msg, pause_msg.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        clock.tick(5)
        continue

    # Movement
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if new_head[0] < 0 or new_head[0] >= GRID_W or new_head[1] < 0 or new_head[1] >= GRID_H or new_head in snake:
        break  # Game over

    snake.insert(0, new_head)

    if new_head == apple:
        score += 10
        apple = random_cell(set(snake))
    else:
        snake.pop()

    # Drawing
    screen.blit(bg_image, (0, 0))
    draw_apple(apple)
    for cell in snake:
        draw_cell(screen, SNAKE_COLOR, cell)
    score_surf = render_text(f"Score: {score}", 24, (255, 255, 255))
    screen.blit(score_surf, (10, 10))
    pygame.display.update()
    clock.tick(snake_speed)

# ──────── Game Over ──────── #
screen.fill(BG_COLOR)
over = render_text("GAME OVER", 64, APPLE_COLOR)
final = render_text(f"Final score: {score}", 32, (50, 50, 50))
info = render_text("Press any key to quit", 24, (80, 80, 80))
screen.blit(over,  over.get_rect(center=(WIDTH//2, HEIGHT//3)))
screen.blit(final, final.get_rect(center=(WIDTH//2, HEIGHT//3 + 70)))
screen.blit(info,  info.get_rect(center=(WIDTH//2, HEIGHT//3 + 120)))
pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type in (pygame.KEYDOWN, pygame.QUIT):
            waiting = False
pygame.quit()
