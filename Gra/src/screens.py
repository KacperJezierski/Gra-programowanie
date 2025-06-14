import pygame
import sys
from set import *
from functions import *
from game_objects import Player, Food, Poison
from PIL import ImageSequence

def rules():
    in_rules = True
    while in_rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meow_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                meow_sound.play()
                if back_button.collidepoint(event.pos):
                    in_rules = False

        window.fill(PINK)
        draw_text("Rules", BLACK, window, 74, 450, 100)
        draw_text('Try to catch as many fishes and milk as you can.', BLACK, window, 40, 450, 230)
        draw_text('Avoid beer and chili peppers.', BLACK, window, 40, 450, 280)
        draw_text('You have 9 lives. When you catch a beer', BLACK, window, 40, 450, 330)
        draw_text('or chili, you lose one life.', BLACK, window, 40, 450, 380)

        back_button = pygame.Rect(330, 500, 240, 50)
        pygame.draw.rect(window, BLACK, back_button)
        draw_text("Back to Menu", PINK, window, 30, 450, 500)

        pygame.display.update()

def settings():
    in_settings = True
    local_selected_img_index = selected_img_index
    while in_settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meow_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                meow_sound.play()
                if back_button.collidepoint(event.pos):
                    in_settings = False
                for i, img_button in enumerate(img_buttons):
                    if img_button["rect"].collidepoint(event.pos):
                        local_selected_img_index = i
                        for button in img_buttons:
                            button["color"] = WHITE
                        img_buttons[local_selected_img_index]["color"] = BLACK

        window.fill(PINK)
        draw_text("Settings", BLACK, window, 74, 450, 100)
        draw_text("Choose your character:", BLACK, window, 30, 450, 200)

        back_button = pygame.Rect(330, 500, 240, 50)
        pygame.draw.rect(window, BLACK, back_button)
        draw_text("Back to Menu", PINK, window, 30, 450, 500)

        img_buttons = []
        for i, img_path in enumerate(img_paths):
            img = pygame.image.load(img_path)
            resized_img = pygame.transform.scale(img, (150, 150))
            image_button_rect = resized_img.get_rect(topleft=(80 + i * 200, 300))
            color = BLACK if i == local_selected_img_index else WHITE
            pygame.draw.rect(window, color, image_button_rect)
            window.blit(resized_img, image_button_rect)
            img_buttons.append({"rect": image_button_rect, "color": color})

        pygame.display.update()

    return local_selected_img_index

def about():
    in_about = True
    while in_about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meow_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                meow_sound.play()
                if back_button.collidepoint(event.pos):
                    in_about = False

        window.fill(PINK)
        draw_text("About", BLACK, window, 74, 450, 100)
        draw_text('Author:', BLACK, window, 40, 450, 230)
        draw_text('Kacper Jezierski', BLACK, window, 40, 450, 280)
        draw_text('2025', BLACK, window, 40, 450, 330)

        back_button = pygame.Rect(330, 500, 240, 50)
        pygame.draw.rect(window, BLACK, back_button)
        draw_text("Back to Menu", PINK, window, 30, 450, 500)

        pygame.display.update()



def best():
    scores = best_scores()
    in_best = True
    while in_best:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meow_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                meow_sound.play()
                if back_button.collidepoint(event.pos):
                    in_best = False

        window.fill(PINK)
        draw_text("Best scores", BLACK, window, 74, 450, 100)

        with open("data/best.txt", "r") as file:
            best = file.read()

        for i in range(len(scores)):
            #score_info = "{}. {}".format(i + 1, scores[i])
            if i == 0 and best:  
                score_info = " Best score belongs to {}: {}".format(best,scores[0])  
                draw_text(score_info, BLACK, window, 50, 450, 200)  
            else:
                draw_text("{}. {}".format(i + 1, scores[i]), BLACK, window, 50, 450, 200 + 80 * i)

        back_button = pygame.Rect(330, 500, 240, 50)
        pygame.draw.rect(window, BLACK, back_button)
        draw_text("Back to Menu", PINK, window, 30, 450, 500)

        pygame.display.update()


def game_over():
    window.fill(PINK)
    draw_text("Game Over", BLACK, window, 74, 450, 200)
    draw_text("Press any key to return to main menu", BLACK, window, 36, 450, 300)
    lose_sound.play()
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
    main_menu()

def high_score():
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()

        pygame_image = pygame.image.fromstring(data, size, mode)
        frames.append(pygame_image)

    current_frame = 0
    clock = pygame.time.Clock()

    new_score = best_scores()
    yipee_sound.play(loops=-1) 

    input_box = pygame.Rect(325, 420, 250, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    
    font = pygame.font.Font(font_name, 28)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.strip(): 
                            save_high_score(text)
                            waiting = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if event.key == pygame.K_ESCAPE:
                    waiting = False

        window.fill(PINK)
        draw_text("Congratulations!", BLACK, window, 74, 450, 100)
        draw_text(f"You have set new high score, which is: {new_score[0]}", BLACK, window, 36, 450, 250)

        txt_surface = font.render(text, True, color)
        text_x = input_box.x + (input_box.width - txt_surface.get_width()) // 2
        text_y = input_box.y + (input_box.height - txt_surface.get_height()) // 2
        window.blit(txt_surface, (text_x, text_y))
        pygame.draw.rect(window, color, input_box, 2)

        draw_text("Enter your name:", BLACK, window, 36, 450, 350)
        draw_text("Press ENTER to continue", BLACK, window, 36, 450, 500)

        window.blit(frames[current_frame], (50, 300)) 
        window.blit(frames[current_frame], (WINDOW_WIDTH - 50 - frames[current_frame].get_width(), 300))
        pygame.display.flip()

        current_frame = (current_frame + 1) % len(frames)
        clock.tick(30)

        pygame.display.update()
    
    yipee_sound.stop() 
    main_menu()

def main_menu():
    img = pygame.image.load("images/img_menu.png")
    img = pygame.transform.scale(img, (300, 300))
    img_rect = img.get_rect()
    img_rect.topleft = (600, 390)

    global selected_img_index

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meow_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                meow_sound.play()
                if start_button.collidepoint(event.pos):
                    menu = False
                    main(selected_img_index)
                elif rules_button.collidepoint(event.pos):
                    rules()
                elif settings_button.collidepoint(event.pos):
                    selected_img_index = settings()
                elif about_button.collidepoint(event.pos):
                    about()
                elif best_button.collidepoint(event.pos):
                    best()

        window.fill((241, 223, 245))
        draw_text("Cat Catcher 2.0 Deluxe Edition", BLACK, window, 55, 450, 100)

        start_button = pygame.Rect(350, 240, 200, 50)
        rules_button = pygame.Rect(350, 310, 200, 50)
        settings_button = pygame.Rect(350, 380, 200, 50)
        about_button = pygame.Rect(350, 450, 200, 50)
        best_button = pygame.Rect(300, 520, 300, 50)

        pygame.draw.rect(window, BLACK, start_button)
        pygame.draw.rect(window, BLACK, rules_button)
        pygame.draw.rect(window, BLACK, settings_button)
        pygame.draw.rect(window, BLACK, about_button)
        pygame.draw.rect(window, BLACK, best_button)

        draw_text("Start", PINK, window, 50, 450, 230)
        draw_text("Rules", PINK, window, 50, 450, 300)
        draw_text("Settings", PINK, window, 50, 450, 370)
        draw_text("About", PINK, window, 50, 450, 440)
        draw_text("Best scores", PINK, window, 50, 450, 510)

        window.blit(img, img_rect)

        pygame.display.update()

def main(selected_img_index):

    run = True
    img_selected = pygame.image.load(img_paths[selected_img_index])
    player = Player(img_selected)
    clock = pygame.time.Clock()
    food_list = []
    poison_list = []
    score = 0
    lives = player.lives
    pygame.time.set_timer(pygame.USEREVENT, 10 * 1000)

    Food.reset_class_variables()
    Poison.reset_class_variables()

    while run:
        delta_time = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT:
                Food.increase_speed()
                Poison.increase_speed()

        if len(food_list) == 0 or food_list[-1].should_spawn(delta_time):
            for _ in range(Food.spawn_count):
                new_food = Food()
                food_list.append(new_food)

        if len(poison_list) == 0 or poison_list[-1].should_spawn(delta_time):
            for _ in range(Poison.spawn_count):
                new_poison = Poison()
                poison_list.append(new_poison)

        keys = pygame.key.get_pressed()
        player.tick(keys)

        window.fill((241, 223, 245))

        for food in food_list:
            food.fall()
            food.draw(window)

            if food.rect.colliderect(player.rect):
                score += 1
                win_sound.play()
                food.reset_position()

        for poison in poison_list:
            poison.fall()
            poison.draw(window)

            if poison.rect.colliderect(player.rect):
                lives -= 1
                poison_sound.play()
                poison.reset_position()

        if lives == 0 and score > best_scores()[0]:
            save_score(score)
            high_score()        

        if lives == 0:
            save_score(score)
            game_over()
        
        draw_text(f"Score: {score}", BLACK, window, 36, 100, 10)
        draw_text(f"Lives: {lives}", BLACK, window, 36, 800, 10)

        player.draw()

        pygame.display.update()

    game_over()

