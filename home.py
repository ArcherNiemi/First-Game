import main
import pygame
import csv
import pandas as pd

pygame.init()

FONT_HOME = pygame.font.SysFont("arial", 80)
FONT_PLAY = pygame.font.SysFont("arial", 45)
FONT_GOLD = pygame.font.SysFont("arial", 45)
FONT_TITLE = pygame.font.SysFont("arial", 100)

PLAY_BOX_SIZE = 400
GOLD_SIZE = 40

PLAY_BOX = pygame.transform.scale(pygame.image.load("images/play_box.png"), (PLAY_BOX_SIZE,PLAY_BOX_SIZE))
GOLD = pygame.transform.scale(pygame.image.load("images/toppng.com-plain-gold-coin-png-300x300.png"), (GOLD_SIZE, GOLD_SIZE))

PLAY_BOX_PIXIL = PLAY_BOX_SIZE / 100

CONTINUE_LOCATION = (main.WIDTH - PLAY_BOX_PIXIL * 72, main.WIDTH - PLAY_BOX_PIXIL * 6, main.HEIGHT - PLAY_BOX_PIXIL * 56, main.HEIGHT - PLAY_BOX_PIXIL * 35)
NEW_GAME_LOCATION = (main.WIDTH - PLAY_BOX_PIXIL * 72, main.WIDTH - PLAY_BOX_PIXIL * 6, main.HEIGHT - PLAY_BOX_PIXIL * 26, main.HEIGHT - PLAY_BOX_PIXIL * 6)

def homePage():
    run = True
    df = pd.read_csv('personalData.csv')
    amountOfGold = df["gold"][0]
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = event.pos
                if(clickpos[0] >= NEW_GAME_LOCATION[0] and clickpos[0] <= NEW_GAME_LOCATION[1] and clickpos[1] >= NEW_GAME_LOCATION[2] and clickpos[1] <= NEW_GAME_LOCATION[3]):
                    main.main(1)
                elif(clickpos[0] >= CONTINUE_LOCATION[0] and clickpos[0] <= CONTINUE_LOCATION[1] and clickpos[1] >= CONTINUE_LOCATION[2] and clickpos[1] <= CONTINUE_LOCATION[3]):
                    main.continueGame()
        homePageDraw(amountOfGold)

def homePageDraw(amountOfGold):
    main.WIN.blit(main.BG, (0, 0))
    main.WIN.blit(PLAY_BOX, (main.WIDTH - PLAY_BOX.get_width(), main.HEIGHT - PLAY_BOX.get_height()))

    gold_text = FONT_GOLD.render(f"{amountOfGold}", 1, "gold")
    main.WIN.blit(GOLD, (main.WIDTH - GOLD.get_width() - gold_text.get_width() - 15, 5))
    main.WIN.blit(gold_text, (main.WIDTH - gold_text.get_width() - 10, 0))

    title_text = FONT_TITLE.render("Bullet Barage", 1, "black")
    play_text = FONT_HOME.render("Play", 1, "black")
    continue_text = FONT_PLAY.render("Continue", 1, "black")
    new_game_text = FONT_PLAY.render("New Game", 1, "black")
    main.WIN.blit(title_text, (main.WIDTH / 2 - title_text.get_width() / 2, 50))
    main.WIN.blit(play_text, (main.WIDTH - PLAY_BOX.get_width() / 2 - play_text.get_width() / 2, main.HEIGHT - PLAY_BOX.get_height() * 0.8 - play_text.get_height() / 2))
    main.WIN.blit(continue_text, (main.WIDTH - 78 * PLAY_BOX.get_width() / 200 - continue_text.get_width() / 2, main.HEIGHT - PLAY_BOX.get_height() * 0.45 - continue_text.get_height() / 2))
    main.WIN.blit(new_game_text, (main.WIDTH -  78 * PLAY_BOX.get_width() / 200 - new_game_text.get_width() / 2, main.HEIGHT - PLAY_BOX.get_height() * 0.15 - new_game_text.get_height() / 2))

    pygame.display.update()

if __name__ == "__main__":
    homePage()