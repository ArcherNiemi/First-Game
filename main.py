import pygame
import time
import random
import math
from Upgrade import upgrade
import Upgrade
import Bullet
import Explosion

pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Barrage")

UPGRADE_SIZE = 280
HEART_SIZE = WIDTH / 15
SHIELD_SIZE_WIDTH = 80
SHIELD_SIZE_HEIGHT = 55
ABILITY_SIZE = WIDTH / 20
SLIME_WIDTH = 60
SLIME_HEIGHT = 45

BULLET_WIDTH = 8
BULLET_HEIGHT = 30

EXPLOSION_SIZE = 30

BG = pygame.transform.scale(pygame.image.load("vecteezy_green-grass-field-with-blue-sky-ad-white-cloud-nature_40153656.jpg"), (WIDTH, HEIGHT))
EMPTY_HEART = pygame.transform.scale(pygame.image.load("empty_heart.png"), (HEART_SIZE, HEART_SIZE))
FULL_HEART = pygame.transform.scale(pygame.image.load("full_heart.png"), (HEART_SIZE, HEART_SIZE))
SHIELD = pygame.transform.scale(pygame.image.load("Blue_Force_Field.png"), (SHIELD_SIZE_WIDTH, SHIELD_SIZE_HEIGHT))
FRAME = pygame.transform.scale(pygame.image.load("Square_Frame_PNG_Clipart.png"), (UPGRADE_SIZE, UPGRADE_SIZE))
SHIELD_FULL = pygame.transform.scale(pygame.image.load("Blue_Force_Field_Full.png"), (ABILITY_SIZE, ABILITY_SIZE))
CLOCK = pygame.transform.scale(pygame.image.load("Time Clock Black Icon - 1000x1000.png"), (ABILITY_SIZE, ABILITY_SIZE))
SHRINK = pygame.transform.scale(pygame.image.load("resize-option.png"), (ABILITY_SIZE, ABILITY_SIZE))
BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullets-png-22781(1).png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
SPEED_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("speed_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
EXPLODING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("exploding_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
HOMING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("homing_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
EXPLOSION = pygame.transform.scale(pygame.image.load("NicePng_light-effect-png_43400.png"), (EXPLOSION_SIZE * 2, EXPLOSION_SIZE * 2))
slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 35
PLAYER_VELOCITY = 8
PLAYER_STARTING_HEALTH = 30

BULLET_VELOCITY = 8

FONT = pygame.font.SysFont("arial", 30)
FONT_START = pygame.font.SysFont("arial", 60)
FONT_END = pygame.font.SysFont("arial", 80)
FONT_LEVEL = pygame.font.SysFont("arial", 60)
FONT_UPGRADE = pygame.font.SysFont("arial", 30)
FONT_BUTTONS = pygame.font.SysFont("arial", 40)
FONT_TITLE = pygame.font.SysFont("arial", 80)
FONT_RESTART = pygame.font.SysFont("arial", 80)

START_DELAY_BETWEEN_BULLETS = 2000
START_AMOUNT_OF_BULLETS_PER_WAVE = 5
START_LENGTH_OF_ROUNDS = 5

UPGRADE_LIST = ["Hp Increase", "Heal", "Shield", "Shrink", "Time Slow"]


SHRINK_SIZE = 2
TIME_SLOW_AMOUNT = 2

RARE_RARITY = 5

RARE_POWER = 2

TOTAL_AMOUNT_OF_UPGRADES = 5

COOL_DOWN = 5

SPEED_BULLET_START_ROUND = 5
EXPLODING_BULLET_START_ROUND = 10
HOMING_BULLET_START_ROUND = 15
COMBO_BULLET_START_ROUND = 20
SUPER_BULLET_START_ROUND = 25

SPECIAL_BULLET_LEVEL_SCALING = 2

SPECIAL_BULLET_STARTING_AMOUNT = 10

EXPLOSION_TIME = 0.5

health = PLAYER_STARTING_HEALTH
maxHp = PLAYER_STARTING_HEALTH
running = True

upgrade_stats = [maxHp, health, Upgrade.shield.duration, Upgrade.shrink.duration, Upgrade.timeSlow.duration]
UPGRADE_STAT_AMOUNT = [1, 3, 0.25, 0.5, 0.75]

SPEED_AMOUNT = 2

currentDirection = slime_left


def draw(player, elapsed_time, bullets, explosions, shield, shrink, timeSlow, level, currentShieldCoolDown, currentShrinkCoolDown, currentTimeSlowCoolDown, shrink_time, shield_time, timeSlow_time):
    pygame.draw.rect(WIN, "red", player)
    for bullet in bullets:
        pygame.draw.rect(WIN, "black", bullet.hitBox)
    for explosion in explosions:
        pygame.draw.rect(WIN, "red", explosion.hitBox)
    WIN.blit(BG, (0, 0))
    if(timeSlow):
        draw_rect_alpha(WIN, pygame.Color(128, 0, 128, 90), pygame.Rect(0,0,WIDTH, HEIGHT))
    if(maxHp <= 14):
        for i in range(maxHp):
            if(health > i):
                WIN.blit(FULL_HEART, (WIDTH - (WIDTH / 15) * ((i) * (0.9)) - WIDTH / 60 - FULL_HEART.get_width(), 0))
            else:
                WIN.blit(EMPTY_HEART, (WIDTH - (WIDTH / 15) * ((i) * (0.9)) - WIDTH / 60 - EMPTY_HEART.get_width(), 0))
    else:
        for i in range(maxHp):
            if(health > i):
                WIN.blit(FULL_HEART, (WIDTH - (WIDTH / 15) * ((i) * (0.3)) - WIDTH / 60 - FULL_HEART.get_width(), 0))
            else:
                WIN.blit(EMPTY_HEART, (WIDTH - (WIDTH / 15) * ((i) * (0.3)) - WIDTH / 60 - EMPTY_HEART.get_width(), 0))


    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
    WIN.blit(time_text, (10, 10))
    level_text = FONT.render(f"Level: {level}", 1, "black")
    WIN.blit(level_text, (10, 15 + time_text.get_height()))
    WIN.blit(SHIELD_FULL, (10, 20 + time_text.get_height() + level_text.get_height()))
    WIN.blit(SHRINK, (10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE))
    WIN.blit(CLOCK, (10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2))

    if(Upgrade.shield.duration <= 0):
        draw_rect_alpha(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 20 + time_text.get_height() + level_text.get_height(), ABILITY_SIZE, ABILITY_SIZE))
    elif(currentShieldCoolDown > 0):
        draw_transparent_arc(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 20 + time_text.get_height() + level_text.get_height(), ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * currentShieldCoolDown)/ COOL_DOWN)
    elif(shield):
        draw_transparent_arc(WIN, pygame.Color(0, 255, 0, 128), pygame.Rect(10, 20 + time_text.get_height() + level_text.get_height(), ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * (shield_time - elapsed_time + Upgrade.shield.duration))/Upgrade.shield.duration)
    
    if(Upgrade.shrink.duration <= 0):
        draw_rect_alpha(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE, ABILITY_SIZE, ABILITY_SIZE))
    elif(currentShrinkCoolDown > 0):
        draw_transparent_arc(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * currentShrinkCoolDown)/ COOL_DOWN)
    elif(shrink):
        draw_transparent_arc(WIN, pygame.Color(0, 255, 0, 128), pygame.Rect(10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * (shrink_time - elapsed_time + Upgrade.shrink.duration))/ Upgrade.shrink.duration)
    
    if(Upgrade.timeSlow.duration <= 0):
        draw_rect_alpha(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2, ABILITY_SIZE, ABILITY_SIZE))
    elif(currentTimeSlowCoolDown > 0):
        draw_transparent_arc(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * currentTimeSlowCoolDown)/ COOL_DOWN)
    elif(timeSlow):
        draw_transparent_arc(WIN, pygame.Color(0, 255, 0, 128), pygame.Rect(10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * (timeSlow_time - time.time() + Upgrade.timeSlow.duration))/ Upgrade.timeSlow.duration)
    if(shrink):
        WIN.blit(currentDirection, (player.x - 5 / SHRINK_SIZE, player.y - 5 / SHRINK_SIZE))
    else:
        WIN.blit(currentDirection, (player.x - 5, player.y - 5))

    if(shield):
        WIN.blit(SHIELD, (player.x + player.width / 2 - SHIELD.get_width() / 2, HEIGHT - SHIELD.get_height()))

    for bullet in bullets:
        if(bullet.type == "homing"):
            WIN.blit(HOMING_BULLET, (bullet.hitBox.x, bullet.hitBox.y))
        elif(bullet.type == "exploding"):
            WIN.blit(EXPLODING_BULLET, (bullet.hitBox.x, bullet.hitBox.y))
        elif(bullet.type == "speed"):
            WIN.blit(SPEED_BULLET, (bullet.hitBox.x, bullet.hitBox.y))
        else:
            WIN.blit(BULLET, (bullet.hitBox.x, bullet.hitBox.y))

    for explosion in explosions:
        WIN.blit(EXPLOSION, (explosion.hitBox.x - EXPLOSION_SIZE / 2, explosion.hitBox.y - EXPLOSION_SIZE / 2))

    pygame.display.update()

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw_transparent_arc(surface, color, rect, start_angle, stop_angle, width=round(ABILITY_SIZE), alpha=255):
    arc_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    arc_surface.fill((0, 0, 0, 0))
    pygame.draw.arc(arc_surface, color, (0, 0, rect.width, rect.height), start_angle, stop_angle, width)
    arc_surface.set_alpha(alpha)
    surface.blit(arc_surface, rect.topleft)

def startScreen():
    run = True
    title_text = FONT_TITLE.render("Bullet Barrage", 1, "white")
    WIN.blit(title_text, (WIDTH/2 - title_text.get_width()/2, HEIGHT/4 - title_text.get_height()/2))
    start_text = FONT_START.render("Press Space To Start", 1, "white")
    WIN.blit(start_text, (WIDTH/2 - start_text.get_width()/2, HEIGHT/2 - start_text.get_height()/2))
    buttons_text = FONT_BUTTONS.render("shield = 1", 1, "white")
    WIN.blit(buttons_text, (WIDTH/4 - buttons_text.get_width()/2, HEIGHT/(1 + 1/6) - buttons_text.get_height()/2))
    buttons_text = FONT_BUTTONS.render("shrink = 2", 1, "white")
    WIN.blit(buttons_text, (WIDTH/(4/2) - buttons_text.get_width()/2, HEIGHT/(1 + 1/6) - buttons_text.get_height()/2))
    buttons_text = FONT_BUTTONS.render("timeSlow = 3", 1, "white")
    WIN.blit(buttons_text, (WIDTH/(4/3) - buttons_text.get_width()/2, HEIGHT/(1 + 1/6) - buttons_text.get_height()/2))
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

def upgradeScreen():
    WIN.blit(BG, (0, 0))
    upgrade = [0,0]
    rarity_increase = [1,1]
    upgradeColor = "white"
    upgrade[0] = random.randint(0, TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY - 1)
    upgrade[1] = random.randint(0, TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY - 1)

    while(upgrade[0] % TOTAL_AMOUNT_OF_UPGRADES == upgrade[1] % TOTAL_AMOUNT_OF_UPGRADES):
        upgrade[1] = random.randint(0, TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY - 1)
    for i in range(2):
        if(upgrade[i] >= (TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY) - TOTAL_AMOUNT_OF_UPGRADES):
            rarity_increase[i] = RARE_POWER
            upgradeColor = "green"
        else:
            rarity_increase[i] = 1
            upgradeColor = "white"

        pygame.draw.rect(WIN, "black", pygame.Rect(WIDTH / (1.5 * (i + 1)) - UPGRADE_SIZE / 2, HEIGHT / 2 - UPGRADE_SIZE / 2, UPGRADE_SIZE, UPGRADE_SIZE))
        WIN.blit(FRAME, (WIDTH / (1.5 * (i + 1)) - UPGRADE_SIZE / 2, HEIGHT / 2 - UPGRADE_SIZE / 2 ))

        for t in range(TOTAL_AMOUNT_OF_UPGRADES):
            if(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == t):
                splitUpgrade = UPGRADE_LIST[t].split()
                if(upgrade_stats[t] == 0):
                    splitUpgrade.append(f"({upgrade_stats[t]}s => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * 2}s)")
                    for p in range(len(splitUpgrade)):
                        upgrade_text = FONT_UPGRADE.render(splitUpgrade[p], 1, "white")
                        WIN.blit(upgrade_text, (WIDTH/((i+1) * 1.5) - upgrade_text.get_width()/2, HEIGHT/2 - (upgrade_text.get_height()/2) * ((len(splitUpgrade)) - p * 2) ))
                else:
                    if(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 0):
                        splitUpgrade.append(f"({upgrade_stats[t]} => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i]})")
                    elif(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 1):
                        if(health + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i] >= maxHp):
                            splitUpgrade.append(f"({health} => {upgrade_stats[0]})")
                        else:
                            splitUpgrade.append(f"({upgrade_stats[t]} => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i]})")
                    else:
                        splitUpgrade.append(f"({upgrade_stats[t]}s => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i]}s)")
                    for p in range(len(splitUpgrade)):
                        upgrade_text = FONT_UPGRADE.render(splitUpgrade[p], 1, upgradeColor)
                        WIN.blit(upgrade_text, (WIDTH/((i+1) * 1.5) - upgrade_text.get_width()/2, HEIGHT/2 - (upgrade_text.get_height()/2) * ((len(splitUpgrade)) - p * 2) ))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = event.pos
                for i in range(2):
                    if(clickpos[0] > WIDTH / (1.5 * (i + 1)) - UPGRADE_SIZE / 2 and clickpos[0] < WIDTH / (1.5 * (i + 1)) + UPGRADE_SIZE / 2 
                       and clickpos[1] > HEIGHT / 2 - UPGRADE_SIZE / 2 and clickpos[1] < HEIGHT / 2 + UPGRADE_SIZE / 2):
                        clickedAbility = upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES
                        print(f"upgrade: {clickedAbility}")
                        print(f"rarity: {rarity_increase[i]}")
                        number = rarity_increase[i]
                        run = False
    giveAbility(clickedAbility, number)
    
def giveAbility(clickedAbility, rarityIncrease):
    global upgrade_stats
    global maxHp
    global health 
    if(clickedAbility == 0):
        maxHp += Upgrade.increaseHp(rarityIncrease)
    elif(clickedAbility == 1):
        health += Upgrade.healUp(rarityIncrease, maxHp, health)
    elif(clickedAbility == 2):
        Upgrade.shield.duration += Upgrade.shieldIncrease(rarityIncrease)
    elif(clickedAbility == 3):
        Upgrade.shrink.duration += Upgrade.shrinkIncrease(rarityIncrease)
    elif(clickedAbility == 4):
        Upgrade.timeSlow.duration += Upgrade.timeSlowIncrease(rarityIncrease)
    upgrade_stats = [maxHp, health, Upgrade.shield.duration, Upgrade.shrink.duration, Upgrade.timeSlow.duration]

def resetScreen():
    background = pygame.Rect(0, 0, WIDTH, HEIGHT)
    pygame.draw.rect(WIN, "black", background)
    restart_text = FONT_RESTART.render("Restart", 1, "white")
    WIN.blit(restart_text, (WIDTH/2 - restart_text.get_width()/2, HEIGHT/5 * 2 - restart_text.get_height()/2))
    quit_text = FONT_RESTART.render("Quit", 1, "white")
    WIN.blit(quit_text, (WIDTH/2 - quit_text.get_width()/2, HEIGHT/5 * 3 - quit_text.get_height()/2))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = event.pos
                if(clickpos[0] > WIDTH / 2 - restart_text.get_width() / 2 and clickpos[0] < WIDTH / 2 + restart_text.get_width() / 2 and clickpos[1] > HEIGHT / 5 * 2 - restart_text.get_height() / 2 and clickpos[1] < HEIGHT / 5 * 2 + restart_text.get_height() / 2):
                    reset()
                    run = False
                elif(clickpos[0] > WIDTH / 2 - quit_text.get_width() / 2 and clickpos[0] < WIDTH / 2 + quit_text.get_width() / 2 and clickpos[1] > HEIGHT / 5 * 3 - quit_text.get_height() / 2 and clickpos[1] < HEIGHT / 5 * 3 + quit_text.get_height() / 2):
                    run = False
                    pygame.quit()

def reset():
    global health
    global maxHp
    global upgrade_stats
    health = PLAYER_STARTING_HEALTH
    maxHp = PLAYER_STARTING_HEALTH
    Upgrade.shield.duration = 0
    Upgrade.shrink.duration = 0
    Upgrade.timeSlow.duration = 0
    upgrade_stats = [maxHp, health, Upgrade.shield.duration, Upgrade.shrink.duration, Upgrade.timeSlow.duration]
    print("Reset")

def chooseType(level):
    randomInt = random.randint(1,100)
    totalBulletTypeAmount = 0
    if(level >= HOMING_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - HOMING_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return "homing"
    if(level >= EXPLODING_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - EXPLODING_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return "exploding"
    if(level >= SPEED_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - SPEED_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return "speed"
    return "normal"

def main():
    global running
    startScreen()
    while(True):
        level = 1
        running = True
        while(running):
            levelStart(level)
            run(level)
            if(running):
                levelEnd(level)
                upgradeScreen()
            level += 1
        resetScreen()

def run(level):
    global currentDirection
    global slime_left
    global slime_right
    global running

    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
    slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    bullet_add_increment = 2000
    bullet_count = 0
    
    bullets = []
    hit = False
    dead = False

    explosions = []

    difficulty = 1 + level / 10

    currentShieldCoolDown = 0
    currentShrinkCoolDown = 0
    currentTimeSlowCoolDown = 0

    startShieldCoolDown = -COOL_DOWN
    startShrinkCoolDown = -COOL_DOWN
    startTimeSlowCoolDown = -COOL_DOWN

    shield = False
    shrink = False
    timeSlow = False

    shield_time = 0
    shrink_time = 0
    timeSlow_time = 0

    currentPlayerVelocity = PLAYER_VELOCITY
    amountOfTimeSlow = 0
    totalAmountOfTimeSlow = 0

    while run:
        if(timeSlow):
            bullet_count += clock.tick(60 / TIME_SLOW_AMOUNT)
        else:
            bullet_count += clock.tick(60)
        elapsed_time = time.time() - start_time - amountOfTimeSlow
        if(timeSlow):
            amountOfTimeSlow = (time.time() - timeSlow_time) / 2 + totalAmountOfTimeSlow
        else:
            totalAmountOfTimeSlow = amountOfTimeSlow

        if(shield and elapsed_time - shield_time >= Upgrade.shield.duration):
            shield = False
            startShieldCoolDown = elapsed_time
        else:
            currentShieldCoolDown = startShieldCoolDown - elapsed_time + COOL_DOWN
        if(shrink and elapsed_time - shrink_time >= Upgrade.shrink.duration):
            shrink = False
            player.x -= player.width / 2
            player.width *= SHRINK_SIZE
            player.height *= SHRINK_SIZE
            if(currentDirection == slime_left):
                slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
                slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))
                currentDirection = slime_left
            elif(currentDirection == slime_right):
                slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
                slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))
                currentDirection = slime_right
            player.y = HEIGHT - player.height
            currentPlayerVelocity = PLAYER_VELOCITY
            startShrinkCoolDown = elapsed_time
        else:
            currentShrinkCoolDown = startShrinkCoolDown - elapsed_time + COOL_DOWN
        if(timeSlow and time.time() - timeSlow_time >= Upgrade.timeSlow.duration):
            timeSlow = False
            startTimeSlowCoolDown = time.time()
        else:
            currentTimeSlowCoolDown = startTimeSlowCoolDown - time.time() + COOL_DOWN
        if(timeSlow):
            bullet_add_increment = int(round(random.randint(int(round(START_DELAY_BETWEEN_BULLETS / difficulty) / 3), int(round(START_DELAY_BETWEEN_BULLETS / difficulty))) * TIME_SLOW_AMOUNT))
        else:
            bullet_add_increment = random.randint(int(round(START_DELAY_BETWEEN_BULLETS / difficulty) / 3), int(round(START_DELAY_BETWEEN_BULLETS / difficulty)))


        if(elapsed_time < START_LENGTH_OF_ROUNDS * difficulty):
            if bullet_count > bullet_add_increment:
                for _ in range(random.randint(int(round(START_AMOUNT_OF_BULLETS_PER_WAVE * difficulty)/2), int(round(START_AMOUNT_OF_BULLETS_PER_WAVE * difficulty)))):
                    bullet_x = random.randint(0, WIDTH - BULLET_WIDTH)
                    bullet_type = chooseType(level)
                    if(bullet_type == "speed"):
                        bullet_speed = random.randint((BULLET_VELOCITY - 1) * SPEED_AMOUNT, (BULLET_VELOCITY + 1) * SPEED_AMOUNT)
                    else:
                        bullet_speed = random.randint(BULLET_VELOCITY - 1, BULLET_VELOCITY + 1)
                    bullet = Bullet.Bullet(bullet_speed, bullet_type, pygame.Rect(bullet_x, -BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT))
                    bullets.append(bullet)
                
                bullet_add_increment = max(200, bullet_add_increment - 50)
                bullet_count = 0
        
        elif(len(bullets) <= 0):
            break
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and currentShieldCoolDown <= 0 and not(shield) and Upgrade.shield.duration > 0:
            shield = True
            shield_time = elapsed_time
        if keys[pygame.K_2] and currentShrinkCoolDown <= 0 and not(shrink) and Upgrade.shrink.duration > 0:
            shrink = True
            shrink_time = elapsed_time
            player.width /= SHRINK_SIZE
            player.height /= SHRINK_SIZE
            if(currentDirection == slime_left):
                slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH / SHRINK_SIZE, SLIME_HEIGHT / SHRINK_SIZE))
                slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH / SHRINK_SIZE, SLIME_HEIGHT / SHRINK_SIZE))
                currentDirection = slime_left
            elif(currentDirection == slime_right):
                slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH / SHRINK_SIZE, SLIME_HEIGHT / SHRINK_SIZE))
                slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH / SHRINK_SIZE, SLIME_HEIGHT / SHRINK_SIZE))
                currentDirection = slime_right

            player.y = HEIGHT - player.height
            player.x += player.width / 2
            currentPlayerVelocity /= SHRINK_SIZE
        if keys[pygame.K_3] and currentTimeSlowCoolDown <= 0 and not(timeSlow) and Upgrade.timeSlow.duration > 0:
            timeSlow = True
            timeSlow_time = time.time()
        if keys[pygame.K_LEFT] and player.x - currentPlayerVelocity >= 0:
            player.x -= currentPlayerVelocity
            currentDirection = slime_left
        if keys[pygame.K_RIGHT] and player.x + currentPlayerVelocity + player.width <= WIDTH:
            player.x += currentPlayerVelocity
            currentDirection = slime_right

        for bullet in bullets[:]:
            bullet.hitBox.y += bullet.speed
            if bullet.hitBox.y > HEIGHT:
                if(bullet.type == "exploding"):
                    explosion = Explosion.Explosion(elapsed_time, False, pygame.Rect(bullet.hitBox.x - EXPLOSION_SIZE / 2, bullet.hitBox.y - EXPLOSION_SIZE, EXPLOSION_SIZE, EXPLOSION_SIZE))
                    explosions.append(explosion)
                bullets.remove(bullet)
            elif bullet.hitBox.y + bullet.hitBox.height >= player.y and bullet.hitBox.colliderect(player):
                if(bullet.type == "exploding"):
                    explosion = Explosion.Explosion(elapsed_time, True, pygame.Rect(bullet.hitBox.x - EXPLOSION_SIZE / 2, bullet.hitBox.y, EXPLOSION_SIZE, EXPLOSION_SIZE))
                    explosions.append(explosion)
                bullets.remove(bullet)
                if(not(shield)):
                    hit = True
                break
        
        for explosion in explosions[:]:
            if(explosion.startTime + EXPLOSION_TIME <= elapsed_time):
                explosions.remove(explosion)
            elif(explosion.hitBox.x <= player.x + PLAYER_WIDTH and explosion.hitBox.x + EXPLOSION_SIZE >= player.x and not(explosion.hasHit)):
                print("here")
                explosion.hasHit = True
                hit = True

        if hit:
            global health
            health -= 1
            hit = False
            if(health <= 0):
                dead = True

        draw(player, elapsed_time, bullets, explosions, shield, shrink, timeSlow, level, currentShieldCoolDown, currentShrinkCoolDown, currentTimeSlowCoolDown, shrink_time, shield_time, timeSlow_time)

        if dead:
            lost_text = FONT_END.render("You Lost", 1, "black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()))
            lost_text = FONT_END.render(f"Levels Beaten: {level - 1}", 1, "black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2))
            pygame.display.update()
            pygame.time.delay(3000)
            run = False
            running = False

if __name__ == "__main__":
    main()