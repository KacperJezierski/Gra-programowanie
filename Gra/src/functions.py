import pygame
from set import *
import os

def draw_text(text, color, surf, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def save_score(score):
    file_path = "data/best_scores.txt"
    needs_comma = os.path.getsize(file_path) > 0
    with open(file_path, "a") as file:
        if needs_comma:
            file.write(",")
        file.write(str(score))

def best_scores():
    with open("data/best_scores.txt", "r") as file:
        content = file.read()

    scores = list(filter(None, content.split(",")))
    scores = list(map(int, scores))
    scores.sort(reverse=True)
    top_scores = scores[:3]

    with open("data/best_scores.txt", "w") as file:
        file.write(",".join(map(str, top_scores)))

    return top_scores

def save_high_score(name):
    file_path = "data/best.txt"
    with open(file_path, "w") as file:
        file.write(name)

