import pygame
import sys
import subprocess
import os
pygame.init()

# fenetre
width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame")

# ressource
backround = pygame.image.load("assets/fond.png")
backround = pygame.transform.scale(backround , (width, height))

pygame.mixer.music.load("assets\musique_de_fond.mp3")
pygame.mixer.music.play(-1)

# couleurs
WHITE = (255, 255, 255)
TRANSLUCENT_BLUE = (0,80,200,180)
HOVER_BLUE = (0,140,155,220)
SHADOW = (0, 0, 0)

# police

FONT_TITLE = pygame.font.Font(None, 72)
FONT_BUTTON = pygame.font.Font(None, 36)

class Button:
    def __init__(self, text, center_y, action):
        self.text = text
        self.center_y = center_y
        self.action = action
        self.width, self.height = 320, 70
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (width//2, center_y)
    def draw(self, win, mouse_pos):
        is_hower = self.rect.collidepoint(mouse_pos)
        color = HOVER_BLUE if is_hower else TRANSLUCENT_BLUE
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, (0, 0, self.width, self.height), border_radius=16)
        win.blit(button_surface, self.rect)

        text_surf = FONT_BUTTON.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)

        shadow = FONT_BUTTON.render(self.text, True, SHADOW)
        win.blit(shadow, (text_rect.x+2, text_rect.y+2))
        win.blit(text_surf, text_rect)
    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]

# liste des bouttons

buttons = [
    Button("Nouvvelle Partie",  320, "new"),
    Button("Options",  400, "options"),
    Button("Quitter",  480, "quit")]

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.blit(backround, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    title = FONT_TITLE.render("Pygame Project", True, WHITE)
    shadow = FONT_TITLE.render("Pygame Project", True, SHADOW)
    screen.blit(shadow, (width//2 - title.get_width()//2 + 3, 103))
    screen.blit(title, (width//2 - title.get_width()//2, 100))

    for btn in buttons:
        btn.draw(screen, mouse_pos)
        if btn.is_clicked(mouse_pos, mouse_pressed):
            pygame.time.delay(200)
            if btn.action == "quit":
                running = False
            elif btn.action == "new":
                print("Nouvelle Partie")
                pygame.quit()
                chemin_game = os.path.join(os.path.dirname(__file__), "game.py")
                subprocess.run(["python", chemin_game])
                sys.exit()
            elif btn.action == "options":
                pygame.quit()
                chemin_options = os.path.join(os.path.dirname(__file__), "game_options.py")
                subprocess.run(["python", chemin_options])
                sys.exit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
print("fermeture de jeux")