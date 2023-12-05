import pygame
from random import randint
from pathlib import Path
from typing import Tuple

WIDTH = 800
HEIGHT = 600

gift_countdown = 2500
gift_interval = 100
GIFT_COUNT = 10

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_image = str(Path.cwd() / "elf_stand.png")
        self.surf = pygame.image.load(player_image).convert_alpha()
        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):
        self.rect.center = pos

class Gift(pygame.sprite.Sprite):
    def __init__(self):
        super(Gift, self).__init__()
        gift_image = str(Path.cwd() / "gift.png")
        self.surf = pygame.image.load(gift_image).convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                randint(10, WIDTH - 10),
                randint(10, HEIGHT - 10),
            )
        )

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

# Inicialização do mixer para áudio
pygame.mixer.init()
# Carregar a música de fundo
pygame.mixer.music.load('C:/Users/Aluno/Documents/GitHub/Elf-gifts/Rockin.wav')
# Reproduzir a música de fundo indefinidamente (-1 para loop)
pygame.mixer.music.play(-1)

ADDGIFT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGIFT, gift_countdown)
gift_list = pygame.sprite.Group()
pontos = 0
gift_pickup_sound = pygame.mixer.Sound(str(Path.cwd() / "gift_pickup.wav"))
player = Player()
player.update(pygame.mouse.get_pos())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDGIFT:
            new_gift = Gift()
            gift_list.add(new_gift)
            if len(gift_list) < 3:
                gift_countdown -= gift_interval
            if gift_countdown < 100:
                gift_countdown = 100
            pygame.time.set_timer(ADDGIFT, 0)
            pygame.time.set_timer(ADDGIFT, gift_countdown)

    player.update(pygame.mouse.get_pos())
    gifts_collected = pygame.sprite.spritecollide(
        sprite=player, group=gift_list, dokill=True
    )
    for gift in gifts_collected:
        pontos += 10
        gift_pickup_sound.play()

    if len(gift_list) >= GIFT_COUNT:
        running = False

    # Remova a seção que preenche o fundo com uma cor específica

    # Desenhe seu próprio plano de fundo aqui
    # Carregue sua imagem de fundo personalizada
    background_image = pygame.image.load('background.png')
    # Dimensione a imagem para caber na tela
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    # Coloque a imagem de fundo na tela
    screen.blit(background_image, (0, 0))

    for gift in gift_list:
        screen.blit(gift.surf, gift.rect)

    screen.blit(player.surf, player.rect)

    pontos_font = pygame.font.SysFont("any_font", 50)
    pontos_block = pontos_font.render(f"Pontos: {pontos}", False, (255, 0, 0))
    screen.blit(pontos_block, (50, HEIGHT - 50))

    pygame.display.flip()
    clock.tick(30)

print(f"Game over! Final pontos: {pontos}")
pygame.mouse.set_visible(True)
pygame.quit()

#By: Max Muller
