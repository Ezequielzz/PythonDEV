import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)  # Cor de fundo preta

# Configurações da animação
FONT_SIZE = 22
FONT_COLOR = (0, 255, 0)  # Cor do texto verde
FALLING_SPEED = 1  # Velocidade de queda dos caracteres

# Caracteres possíveis na tela
CHARACTERS = "!@#$%&*+|?/~01"

# Classe para representar um caractere caindo
class MatrixCharacter:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.font = font
        self.character = random.choice(CHARACTERS)
        self.speed = random.randint(1, 25)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        rendered_text = self.font.render(self.character, True, FONT_COLOR)
        screen.blit(rendered_text, (self.x, self.y))


# Inicializando a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Carregando a fonte
font = pygame.font.Font(None, FONT_SIZE)

# Lista de caracteres caindo
matrix_characters = [MatrixCharacter(x, random.randint(-1000, 0), font) for x in range(0, WIDTH, FONT_SIZE//22)]  # Aumenta a quantidade de caracteres

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenha e atualiza cada caractere
    for char in matrix_characters:
        char.update()
        char.draw(screen)

        # Resetando a posição do caractere quando ele alcança o fim da tela
        if char.y > HEIGHT:
            char.y = random.randint(-1000, 0)

    pygame.display.flip()
    clock.tick(30)

# Saindo do Pygame
pygame.quit()
