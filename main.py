import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")

BG = pygame.transform.scale(pygame.image.load("vecteezy_green-grass-field-with-blue-sky-ad-white-cloud-nature_40153656.jpg"), (WIDTH, HEIGHT))
EMPTY_HEART = pygame.transform.scale(pygame.image.load("empty_heart.png"), (WIDTH / 15, WIDTH / 15))
FULL_HEART = pygame.transform.scale(pygame.image.load("full_heart.png"), (WIDTH / 15, WIDTH / 15))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 4
PLAYER_STARTING_HEALTH = 3

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 4

FONT = pygame.font.SysFont("arial", 30)
FONT_START = pygame.font.SysFont("arial", 80)
FONT_END = pygame.font.SysFont("arial", 100)
FONT_LEVEL = pygame.font.SysFont("arial", 60)
FONT_UPGRADE = pygame.font.SysFont("arial", 30)

START_DELAY_BETWEEN_STARS = 2000
START_AMOUNT_OF_STARS_PER_WAVE = 5
START_LENGTH_OF_ROUNDS = 5

UPGRADE_LIST = ["Hp Increase", "Full Heal", "Shrink", "Shield", "Time Slow"]
UPGRADE_SIZE = 150

health = PLAYER_STARTING_HEALTH

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    for i in range(PLAYER_STARTING_HEALTH):
        if(health > i):
            WIN.blit(FULL_HEART, (WIDTH - (WIDTH / 15) * (i + 1), 0))
        else:
            WIN.blit(EMPTY_HEART, (WIDTH - (WIDTH / 15) * (i + 1), 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "black", star)

    pygame.display.update()

def startScreen():
    run = True

    start_text = FONT_START.render("Press Space To Start", 1, "white")
    WIN.blit(start_text, (WIDTH/2 - start_text.get_width()/2, HEIGHT/2 - start_text.get_height()/2))
    pygame.display.update()

    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break

def levelStart(level: int):
    WIN.blit(BG, (0, 0))
    level_text = FONT_LEVEL.render(f"Level: {level}", 1, "black")
    WIN.blit(level_text, (WIDTH/2 - level_text.get_width()/2, HEIGHT/2 - level_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    

def levelEnd(level: int):
    WIN.blit(BG, (0, 0))
    level_text = FONT_LEVEL.render(f"Level: {level} complete", 1, "black")
    WIN.blit(level_text, (WIDTH/2 - level_text.get_width()/2, HEIGHT/2 - level_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

def updrageScreen():
    WIN.blit(BG, (0, 0))
    upgrade = [0,0]
    upgrade[0] = random.randint(0, 4)
    upgrade[1] = random.randint(0, 4)
    while(upgrade[0] == upgrade[1]):
        upgrade[1] = random.randint(0, 4)
    for i in range(2):
        pygame.draw.rect(WIN, "black", pygame.Rect(WIDTH / (1.5 * (i + 1)) - UPGRADE_SIZE / 2, HEIGHT / 2 - UPGRADE_SIZE / 2, UPGRADE_SIZE, UPGRADE_SIZE))
        for t in range(5):
            if(upgrade[i] == t):
                upgrade_text = FONT_UPGRADE.render(UPGRADE_LIST[i], 1, "white")
                WIN.blit(upgrade_text, (WIDTH/((i+1) * 1.5) - upgrade_text.get_width()/2, HEIGHT/2 - upgrade_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)





def main():
    level = 1
    startScreen()
    while(True):
        levelStart(level)
        run(level)
        levelEnd(level)
        updrageScreen()
        level += 1

def run(level):
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    dead = False

    difficulty = 1 + level / 10

    while run:
        star_count += clock.tick(120)
        elapsed_time = time.time() - start_time

        star_add_increment = random.randint(int(round(START_DELAY_BETWEEN_STARS / difficulty) / 3), int(round(START_DELAY_BETWEEN_STARS / difficulty)))

        if(elapsed_time < START_LENGTH_OF_ROUNDS * difficulty):
            if star_count > star_add_increment:
                for _ in range(random.randint(int(round(START_AMOUNT_OF_STARS_PER_WAVE * difficulty)) - 3, int(round(START_AMOUNT_OF_STARS_PER_WAVE * difficulty)))):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)
                
                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0
        
        elif(len(stars) <= 0):
            break
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            global health
            health -= 1
            hit = False
            if(health <= 0):
                dead = True

        draw(player, elapsed_time, stars)

        if dead:
            lost_text = FONT_END.render("You Lost!", 1, "black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()

            

if __name__ == "__main__":
    main()