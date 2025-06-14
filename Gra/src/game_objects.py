import pygame
import random
from set import *

class Player:
    def __init__(self, img_selected=None):
        if img_selected:
            self.image = pygame.transform.scale(img_selected, (100, 100))
        else:
            default_img_path = img_paths[0]
            default_img = pygame.image.load(default_img_path)
            self.image = pygame.transform.scale(default_img, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 490
        self.speed = 7
        self.lives = 9

    def tick(self, keys):
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

    def draw(self):
        window.blit(self.image, self.rect.topleft)

class Food:
    def __init__(self):
        self.image = pygame.image.load(random.choice(food_paths))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 900 - self.image.get_width())
        self.rect.y = -self.image.get_height()
        self.base_speed = 3
        self.speed = self.base_speed * Food.global_speed_multiplier
        self.spawn_rate = max(Food.base_spawn_rate - Food.spawn_rate_decrement * (Food.global_speed_multiplier - 1), Food.minimum_spawn_rate)
        self.time_since_last_spawn = 0
        Food.instances.append(self)

    def fall(self):
        self.rect.y += self.speed

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def reset_position(self):
        self.image = pygame.image.load(random.choice(food_paths))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = random.randint(0, 900 - self.image.get_width())
        self.rect.y = -self.image.get_height()
        self.base_speed = 3
        self.speed = self.base_speed * Food.global_speed_multiplier

    def should_spawn(self, delta_time):
        self.time_since_last_spawn += delta_time
        if self.time_since_last_spawn >= self.spawn_rate:
            self.time_since_last_spawn = 0
            return True
        return False

    @classmethod
    def increase_speed(cls):
        cls.global_speed_multiplier += 0.4
        cls.spawn_count += 1
        for instance in cls.instances:
            instance.speed = instance.base_speed * cls.global_speed_multiplier
            instance.spawn_rate = max(cls.base_spawn_rate - cls.spawn_rate_decrement * (cls.global_speed_multiplier - 1), cls.minimum_spawn_rate)

    @classmethod
    def reset_class_variables(cls):
        cls.global_speed_multiplier = 1
        cls.base_spawn_rate = 1000
        cls.spawn_rate_decrement = 100
        cls.minimum_spawn_rate = 100
        cls.spawn_count = 1
        for instance in cls.instances:
            instance.speed = instance.base_speed * cls.global_speed_multiplier
            instance.spawn_rate = max(cls.base_spawn_rate - cls.spawn_rate_decrement * (cls.global_speed_multiplier - 1), cls.minimum_spawn_rate)

Food.instances = []

class Poison:
    def __init__(self):
        self.image = pygame.image.load(random.choice(poison_paths))
        self.image = pygame.transform.scale(self.image, (25, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.image.get_width())
        self.rect.y = -self.image.get_height()
        self.base_speed = 3
        self.speed = self.base_speed * Poison.global_speed_multiplier
        self.spawn_rate = max(Food.base_spawn_rate - Food.spawn_rate_decrement * (Food.global_speed_multiplier - 1), Food.minimum_spawn_rate)
        self.time_since_last_spawn = 0
        Poison.instances.append(self)

    def fall(self):
        self.rect.y += self.speed

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def reset_position(self):
        self.image = pygame.image.load(random.choice(poison_paths))
        self.image = pygame.transform.scale(self.image, (25, 60))
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.image.get_width())
        self.rect.y = -self.image.get_height()
        self.base_speed = 3
        self.speed = self.base_speed * Poison.global_speed_multiplier

    def should_spawn(self, delta_time):
        self.time_since_last_spawn += delta_time
        if self.time_since_last_spawn >= self.spawn_rate:
            self.time_since_last_spawn = 0
            return True
        return False
    
    @classmethod
    def increase_speed(cls):
        cls.global_speed_multiplier += 0.4
        cls.spawn_count += 1
        for instance in cls.instances:
            instance.speed = instance.base_speed * cls.global_speed_multiplier
            instance.spawn_rate = max(cls.base_spawn_rate - cls.spawn_rate_decrement * (cls.global_speed_multiplier - 1), cls.minimum_spawn_rate)

    @classmethod
    def reset_class_variables(cls):
        cls.global_speed_multiplier = 1
        cls.base_spawn_rate = 900
        cls.spawn_rate_decrement = 100
        cls.minimum_spawn_rate = 100
        cls.spawn_count = 1
        for instance in cls.instances:
            instance.speed = instance.base_speed * cls.global_speed_multiplier
            instance.spawn_rate = max(cls.base_spawn_rate - cls.spawn_rate_decrement * (cls.global_speed_multiplier - 1), cls.minimum_spawn_rate)

Poison.instances = []