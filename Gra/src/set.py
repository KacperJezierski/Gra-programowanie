import pygame
from PIL import Image

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Cat Catcher 2.0 Deluxe Edition')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (241, 223, 245)

img_paths = ['images/chars/char1.png', 'images/chars/char2.png', 'images/chars/char3.png', 'images/chars/char4.png']
food_paths = ['images/items/fish.png', 'images/items/milk.png']
poison_paths = ['images/items/beer.png', 'images/items/chilli.png']
selected_img_index = 0

gif_path = 'images/yipee.gif'
gif = Image.open(gif_path)

font_name = pygame.font.match_font('comicsansms')

pygame.mixer.music.load("ost/background_music.mp3")
pygame.mixer.music.play(loops=-1)

poison_sound = pygame.mixer.Sound("ost/poison.ogg")
win_sound = pygame.mixer.Sound("ost/win.ogg")
lose_sound = pygame.mixer.Sound("ost/lose.ogg")
meow_sound = pygame.mixer.Sound("ost/meow.ogg")
yipee_sound = pygame.mixer.Sound("ost/yipee.ogg")

