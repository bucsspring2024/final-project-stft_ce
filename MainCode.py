import pygame
from pygame import mixer
from Character import Fighter

mixer.init()
pygame.init()

X= 900   # Screen Width
Y = 720   #Screen Height
intro_count = 5
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # Player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

# Set up display
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("CS110 Final assigment")

# Background image
bg_png = pygame.image.load("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/Screen Images/WP.png").convert_alpha()

# Ending Screen
victory_png = pygame.image.load("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/Screen Images/End.png").convert_alpha()

# Load music and sounds
pygame.mixer.music.load("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/Sound Effects/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_sd = pygame.mixer.Sound("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/Sound Effects/sword.wav")
sword_sd.set_volume(0.5)
magic_sd = pygame.mixer.Sound("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/Sound Effects/magic.wav")
magic_sd.set_volume(0.5)

# Define font
count_font = pygame.font.Font("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/tejaratchi/Tejartchi.ttf", 80)
score_font = pygame.font.Font("/Users/samlin/github-classroom/bucsspring2024/final-project-stft_ce/assets/tejaratchi/Tejartchi.ttf", 30)

# Character sprites
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

# Charcater variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# Spirite Sheet Values
WARRIOR_ANIMATION_STEPS = [4, 8, 2, 4, 4, 4, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]


# Function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_png, (X, Y))
    screen.blit(scaled_bg, (0, 0))

# Health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, (255, 255, 255), (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, (216, 36, 41), (x, y, 400, 30))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 400 * ratio, 30))

fighter_1 = Fighter(1, 200, 700, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_sd)
fighter_2 = Fighter(2, 1500, 700, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_sd)


# Set up clock
clock = pygame.time.Clock()

# Game loop
run = True
while run:
    clock.tick(60)

    # Draw background
    draw_bg()

    # Player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 1500, 20)
    draw_text("P1: " + str(score[0]), score_font, (173, 216, 230), 20, 60)
    draw_text("P2: " + str(score[1]), score_font, (216, 36, 41), 1500, 60)

    # Update countdown
    if intro_count <= 0:
        # Move fighters
        fighter_1.move(X, Y, screen, fighter_2, round_over)
        fighter_2.move(X, Y, screen, fighter_1, round_over)
    else:
        # Display count timer
        draw_text