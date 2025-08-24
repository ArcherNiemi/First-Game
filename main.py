import pygame
import time
import random
import math
from Upgrade import upgrade
import Upgrade
import Bullet
import Explosion
import math

pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Barrage")

UPGRADE_SIZE = 240
HEART_SIZE = WIDTH / 15
SHIELD_SIZE_WIDTH = 80
SHIELD_SIZE_HEIGHT = 55
ABILITY_SIZE = WIDTH / 20
SLIME_WIDTH = 60
SLIME_HEIGHT = 45

BULLET_WIDTH = 8
BULLET_HEIGHT = 30

EXPLOSION_SIZE = 30

BG = pygame.transform.scale(pygame.image.load("images/vecteezy_green-grass-field-with-blue-sky-ad-white-cloud-nature_40153656.jpg"), (WIDTH, HEIGHT))
EMPTY_HEART = pygame.transform.scale(pygame.image.load("images/empty_heart.png"), (HEART_SIZE, HEART_SIZE))
FULL_HEART = pygame.transform.scale(pygame.image.load("images/full_heart.png"), (HEART_SIZE, HEART_SIZE))
SHIELD = pygame.transform.scale(pygame.image.load("images/Blue_Force_Field.png"), (SHIELD_SIZE_WIDTH, SHIELD_SIZE_HEIGHT))
FRAME = pygame.transform.scale(pygame.image.load("images/Square_Frame_PNG_Clipart.png"), (UPGRADE_SIZE, UPGRADE_SIZE))
SHIELD_FULL = pygame.transform.scale(pygame.image.load("images/Blue_Force_Field_Full.png"), (ABILITY_SIZE, ABILITY_SIZE))
CLOCK = pygame.transform.scale(pygame.image.load("images/Time Clock Black Icon - 1000x1000.png"), (ABILITY_SIZE, ABILITY_SIZE))
SHRINK = pygame.transform.scale(pygame.image.load("images/resize-option.png"), (ABILITY_SIZE, ABILITY_SIZE))
BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/bullets-png-22781(1).png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
SPEED_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/speed_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
EXPLODING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/exploding_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
HOMING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/homing_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
SPEED_EXPLODING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/speed_exploding_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
SPEED_HOMING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/speed_homing_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
EXPLODING_HOMING_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/exploding_homing_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
SUPER_BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/super_bullet.png"), (BULLET_HEIGHT + 10, BULLET_WIDTH + 2)), -90)
EXPLOSION = pygame.transform.scale(pygame.image.load("images/NicePng_light-effect-png_43400.png"), (EXPLOSION_SIZE * 2, EXPLOSION_SIZE * 2))
slime_left = pygame.transform.scale(pygame.image.load("images/Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
slime_right = pygame.transform.scale(pygame.image.load("images/Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 35
PLAYER_VELOCITY = 8
PLAYER_STARTING_HEALTH = 3

BULLET_VELOCITY = 8

FONT = pygame.font.SysFont("arial", 30)
FONT_START = pygame.font.SysFont("arial", 60)
FONT_END = pygame.font.SysFont("arial", 80)
FONT_LEVEL = pygame.font.SysFont("arial", 60)
FONT_UPGRADE = pygame.font.SysFont("arial", 28)
FONT_BUTTONS = pygame.font.SysFont("arial", 40)
FONT_TITLE = pygame.font.SysFont("arial", 80)
FONT_RESTART = pygame.font.SysFont("arial", 80)

START_DELAY_BETWEEN_BULLETS = 2000
START_AMOUNT_OF_BULLETS_PER_WAVE = 5
START_LENGTH_OF_ROUNDS = 5

UPGRADE_LIST = ["Hp Increase", "Heal", "Shield", "Shrink", "Time Slow"]


SHRINK_SIZE = 2
TIME_SLOW_AMOUNT = 2

COMMON_RARITY = 3125
RARE_RARITY = 625
EPIC_RARITY = 125
LEGENDARY_RARITY = 25
MYTHIC_RARITY = 1

UNLOCK_CHANCE = 0.1

COMMON_POWER = 1
RARE_POWER = 2
EPIC_POWER = 4
LEGENDARY_POWER = 8
MYTHIC_POWER = 32

TOTAL_AMOUNT_OF_COMMON_UPGRADES = 5
TOTAL_AMOUNT_OF_RARE_UPGRADES = 5
TOTAL_AMOUNT_OF_EPIC_UPGRADES = 5
TOTAL_AMOUNT_OF_LENGENDARY_UPGRADES = 5

COOL_DOWN = 5

SPEED_BULLET_START_ROUND = 5
EXPLODING_BULLET_START_ROUND = 10
HOMING_BULLET_START_ROUND = 15
COMBO_BULLET_START_ROUND = 20
SUPER_BULLET_START_ROUND = 25

SPECIAL_BULLET_LEVEL_SCALING = 2

SPECIAL_BULLET_STARTING_AMOUNT = 10

EXPLOSION_TIME = 0.25

MAX_HOMING = 4
MAX_ANGLE = 20
HOMING_INCREASE = 30

LUCK_STARTING_AMOUNT = 1
LUCK_SCALING = 0.25 #higher is stronger luck scaling

finalRareRarity = 0
finalEpicRarity = 0

finalCommonLuck = 0
finalRareLuck = 0
finalEpicLuck = 0

BASE = [LEGENDARY_RARITY, EPIC_RARITY, RARE_RARITY, COMMON_RARITY]

health = PLAYER_STARTING_HEALTH
maxHp = PLAYER_STARTING_HEALTH
running = True
luck = LUCK_STARTING_AMOUNT

upgrade_stats = [maxHp, health, Upgrade.shield.duration, Upgrade.shrink.duration, Upgrade.timeSlow.duration]
UPGRADE_STAT_AMOUNT = [1, 3, 0.25, 0.5, 0.75]

SPEED_AMOUNT = 2

lockedUpgrades = ["maxHp", "health", "shield", "shrink", "timeSlow"]
allUpgrades = ["maxHp", "health", "shield", "shrink", "timeSlow"]

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
        if(len(bullet.type) == 3):
            WIN.blit(pygame.transform.rotate(SUPER_BULLET, bullet.angle), (bullet.hitBox.x, bullet.hitBox.y))
        elif(bullet.type[0] == "homing"):
            if(bullet.type[1] == "exploding"):
                WIN.blit(pygame.transform.rotate(EXPLODING_HOMING_BULLET, bullet.angle), (bullet.hitBox.x, bullet.hitBox.y))
            elif(bullet.type[1] == "speed"):
                WIN.blit(pygame.transform.rotate(SPEED_HOMING_BULLET, bullet.angle), (bullet.hitBox.x, bullet.hitBox.y))
            else:
                WIN.blit(pygame.transform.rotate(HOMING_BULLET, bullet.angle), (bullet.hitBox.x, bullet.hitBox.y))
        elif(bullet.type[0] == "exploding"):
            if(bullet.type[1] == "speed"):
                WIN.blit(SPEED_EXPLODING_BULLET, (bullet.hitBox.x, bullet.hitBox.y))
            elif(bullet.type[1] == "homing"):
                WIN.blit(pygame.transform.rotate(EXPLODING_HOMING_BULLET, bullet.angle), (bullet.hitBox.x, bullet.hitBox.y))
            else:
                WIN.blit(EXPLODING_BULLET, (bullet.hitBox.x, bullet.hitBox.y))
        elif(bullet.type[0] == "speed"):
            if(bullet.type[1] == "exploding"):
                WIN.blit(SPEED_EXPLODING_BULLET, (bullet.hitBox.x, bullet.hitBox.y))
            elif(bullet.type[1] == "homing"):
                WIN.blit(pygame.transform.rotate(SPEED_HOMING_BULLET, bullet.angle), (bullet.hitBox.x, bullet.hitBox.y))
            else:
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
    buttons_text = FONT_BUTTONS.render("Shield = 1", 1, "white")
    WIN.blit(buttons_text, (WIDTH/4 - buttons_text.get_width()/2, HEIGHT/(1 + 1/6) - buttons_text.get_height()/2))
    buttons_text = FONT_BUTTONS.render("Shrink = 2", 1, "white")
    WIN.blit(buttons_text, (WIDTH/(4/2) - buttons_text.get_width()/2, HEIGHT/(1 + 1/6) - buttons_text.get_height()/2))
    buttons_text = FONT_BUTTONS.render("Time Slow = 3", 1, "white")
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

def upgradeScreen(unlock_chance):
    global luck
    WIN.blit(BG, (0, 0))
    upgrade = [0,0,0]
    rarity_increase = [COMMON_POWER,COMMON_POWER,COMMON_POWER]
    upgradeColor = "white"

    for i in range(len(upgrade)):
        rarity = roll_item(luck, unlock_chance)
        print(rarity)
        if(rarity == "unlock"):
            rarity_increase[i] = 0
            upgradeColor = (30, 200, 255)
        elif(rarity == "mythic"):
            rarity_increase[i] = MYTHIC_POWER
            upgradeColor = "red"
        elif(rarity == "legendary"):
            rarity_increase[i] = LEGENDARY_POWER
            upgradeColor = "yellow"
        elif(rarity == "epic"):
            rarity_increase[i] = EPIC_POWER
            upgradeColor = "purple"
        elif(rarity == "rare"):
            rarity_increase[i] = RARE_POWER
            upgradeColor = "green"
        else:
            rarity_increase[i] = COMMON_POWER
            upgradeColor = "white"

        totalAmountOfNumbers = TOTAL_AMOUNT_OF_COMMON_UPGRADES - 1

        upgrade[i] = random.randint(0, totalAmountOfNumbers)

        currentString = allUpgrades[upgrade[i]]
        if(rarity == "unlock"):
            while(not(currentString in lockedUpgrades)):
                upgrade[i] = random.randint(0, totalAmountOfNumbers)
                currentString = allUpgrades[upgrade[i]]
        else:
            while(currentString in lockedUpgrades):
                upgrade[i] = random.randint(0, totalAmountOfNumbers)
                currentString = allUpgrades[upgrade[i]]

        if(rarity == "unlock"):
            if(i == 1):
                while(upgrade[0] == upgrade[1] or not(currentString in lockedUpgrades)):
                    upgrade[1] = random.randint(0, totalAmountOfNumbers)
                    currentString = allUpgrades[upgrade[1]]
            elif(i == 2):
                while(upgrade[0] == upgrade[2] or upgrade[1] == upgrade[2] or not(currentString in lockedUpgrades)):
                    upgrade[2] = random.randint(0, totalAmountOfNumbers)
                    currentString = allUpgrades[upgrade[2]]
        else:
            if(i == 1):
                while(upgrade[0]== upgrade[1] or currentString in lockedUpgrades):
                    upgrade[1] = random.randint(0, totalAmountOfNumbers)
                    currentString = allUpgrades[upgrade[1]]
            elif(i == 2):
                while(upgrade[0] == upgrade[2] or upgrade[1] == upgrade[2] or currentString in lockedUpgrades):
                    upgrade[2] = random.randint(0, totalAmountOfNumbers)
                    currentString = allUpgrades[upgrade[2]]

        pygame.draw.rect(WIN, "black", pygame.Rect(getUpgradeLocation(i) - UPGRADE_SIZE / 2, HEIGHT / 2 - UPGRADE_SIZE / 2, UPGRADE_SIZE, UPGRADE_SIZE))
        WIN.blit(FRAME, (getUpgradeLocation(i) - UPGRADE_SIZE / 2, HEIGHT / 2 - UPGRADE_SIZE / 2))

        for t in range(TOTAL_AMOUNT_OF_COMMON_UPGRADES):
            splitUpgrade = []
            if(rarity == "unlock"):
                splitUpgrade.append("Unlock")
            if(upgrade[i] == t):
                nameSplit = UPGRADE_LIST[t].split()
                for q in range(len(nameSplit)):
                    splitUpgrade.append(nameSplit[q])
                if(rarity != "unlock"):
                    if(upgrade[i] == 0):
                        splitUpgrade.append(f"{upgrade_stats[t]} => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i]}")
                    elif(upgrade[i] == 1):
                        if(health + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i] >= maxHp):
                            splitUpgrade.append(f"{health} => {upgrade_stats[0]}")
                        else:
                            splitUpgrade.append(f"{health} => {health + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i]}")
                    else:
                        splitUpgrade.append(f"{upgrade_stats[t]}s => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * rarity_increase[i]}s")
                for p in range(len(splitUpgrade)):
                    upgrade_text = FONT_UPGRADE.render(splitUpgrade[p], 1, upgradeColor)
                    WIN.blit(upgrade_text, (getUpgradeLocation(i) - upgrade_text.get_width()/2, HEIGHT/2 - (upgrade_text.get_height()/2) * ((len(splitUpgrade)) - p * 2) ))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = event.pos
                for i in range(len(upgrade)):
                    if(clickpos[0] > getUpgradeLocation(i) - UPGRADE_SIZE / 2 and clickpos[0] < getUpgradeLocation(i) + UPGRADE_SIZE / 2 
                       and clickpos[1] > HEIGHT / 2 - UPGRADE_SIZE / 2 and clickpos[1] < HEIGHT / 2 + UPGRADE_SIZE / 2):
                        clickedAbility = upgrade[i] % TOTAL_AMOUNT_OF_COMMON_UPGRADES
                        print(f"upgrade: {clickedAbility}")
                        print(f"rarity: {rarity_increase[i]}")
                        number = rarity_increase[i]
                        run = False
    giveAbility(clickedAbility, number)

def getUpgradeLocation(i):
    return WIDTH - ((WIDTH / 7)) * (i * 2 + 1.5)
    
def giveAbility(clickedAbility, rarityIncrease):
    global upgrade_stats
    global maxHp
    global health
    if(allUpgrades[clickedAbility] in lockedUpgrades):
        lockedUpgrades.remove(allUpgrades[clickedAbility])
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

def roll_item(luck, unlock_chance):
    global finalRareRarity
    global finalEpicRarity
    global finalCommonLuck
    global finalRareLuck
    global finalEpicLuck

    if(len(lockedUpgrades) != 0):
        if(random.uniform(0,1) <= unlock_chance):
            return "unlock"

    newCommonRarity = COMMON_RARITY
    newRareRarity = RARE_RARITY * (LUCK_SCALING * luck + 1)
    newEpicRarity = EPIC_RARITY * (LUCK_SCALING * 2.5 * luck + 1)
    newLegendaryRarity = LEGENDARY_RARITY * (LUCK_SCALING * 5 * luck + 1)
    newMythicRarity = MYTHIC_RARITY * (LUCK_SCALING * 10 * luck + 1)

    if(newCommonRarity <= newRareRarity / 2):
        if(finalRareRarity == 0):
            finalRareRarity = newRareRarity
            finalCommonLuck = luck
        newRareRarity = finalRareRarity
        newCommonRarity = COMMON_RARITY / (LUCK_SCALING / 3 * (luck - finalCommonLuck) + 1)
    if(newRareRarity <= newEpicRarity / 2):
        if(finalEpicRarity == 0):
            finalEpicRarity = newEpicRarity
            finalRareLuck = luck
        newEpicRarity = finalEpicRarity
        newRareRarity = finalRareRarity / (LUCK_SCALING / 2 * (luck - finalRareLuck) + 1)
    
    print([newCommonRarity, newRareRarity, newEpicRarity, newLegendaryRarity, newMythicRarity])

    totalChance = newCommonRarity + newRareRarity + newEpicRarity + newLegendaryRarity + newMythicRarity
    commonChance = newCommonRarity / totalChance
    rareChance = newRareRarity / totalChance
    epicChance = newEpicRarity / totalChance
    legendaryChance = newLegendaryRarity / totalChance
    mythicChance = newMythicRarity / totalChance
    print([commonChance, rareChance, epicChance, legendaryChance, mythicChance])

    chanceList = [commonChance, rareChance, epicChance, legendaryChance, mythicChance]
    returnList = ["common", "rare", "epic", "legendary", "mythic"]

    previousChance = 0
    number = random.uniform(0,1)
    for i in range(len(chanceList)):
        print(number)
        if(number <= chanceList[i] + previousChance):
            return returnList[i]
        else:
            previousChance += chanceList[i]

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
    global luck
    global lockedUpgrades
    luck = LUCK_STARTING_AMOUNT
    health = PLAYER_STARTING_HEALTH
    maxHp = PLAYER_STARTING_HEALTH
    Upgrade.shield.duration = 0
    Upgrade.shrink.duration = 0
    Upgrade.timeSlow.duration = 0
    upgrade_stats = [maxHp, health, Upgrade.shield.duration, Upgrade.shrink.duration, Upgrade.timeSlow.duration]
    lockedUpgrades = ["maxHp", "health", "shield", "shrink", "timeSlow"]
    print("Reset")

def chooseType(level):
    randomInt = random.randint(1,100)
    totalBulletTypeAmount = 0
    if(level >= SUPER_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - SUPER_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return ("speed", "exploding", "homing")
    if(level >= COMBO_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - COMBO_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            type1 = random.choice(("speed", "exploding", "homing"))
            type2 = random.choice(("speed", "exploding", "homing"))
            while(type1 == type2):
                type2 = random.choice(("speed", "exploding", "homing"))
            return (type1, type2)
    if(level >= HOMING_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - HOMING_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return ("homing","")
    if(level >= EXPLODING_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - EXPLODING_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return ("exploding","")
    if(level >= SPEED_BULLET_START_ROUND):
        totalBulletTypeAmount += SPECIAL_BULLET_STARTING_AMOUNT + (SPECIAL_BULLET_LEVEL_SCALING * (level - SPEED_BULLET_START_ROUND))
        if(randomInt > 100 - (totalBulletTypeAmount)):
            return ("speed","")
    return ("normal","")

def findAngle(player, bullet):
    differenceInX = (player.x + PLAYER_WIDTH / 2) - (bullet.hitBox.x + BULLET_WIDTH / 2)
    differenceInY = (player.y + PLAYER_HEIGHT / 2) - (bullet.hitBox.y + BULLET_HEIGHT / 2)
    angle = math.tan(math.radians(differenceInX / differenceInY))
    for i in range(len(bullet.type)):
        if(bullet.type[i] == "speed"):
            turnAngle = angle * HOMING_INCREASE * SPEED_AMOUNT
            if(turnAngle <= MAX_HOMING * SPEED_AMOUNT or turnAngle >= -MAX_HOMING * SPEED_AMOUNT):
                return turnAngle
            else:
                return MAX_HOMING
        else:
            turnAngle = angle * HOMING_INCREASE
            if(turnAngle <= MAX_HOMING or turnAngle >= -MAX_HOMING):
                return turnAngle
            else:
                return MAX_HOMING



def main():
    global running
    global luck
    startScreen()
    while(True):
        if(luck != 0):
            for i in range(luck):
                roll_item(i, UNLOCK_CHANCE)
                print(i)
        for i in range(3):
            upgradeScreen(1)
        level = 1
        running = True
        while(running):
            levelStart(level)
            run(level)
            if(running):
                levelEnd(level)
                upgradeScreen(UNLOCK_CHANCE)
            level += 1
            luck += 1
        resetScreen()

def run(level):
    global currentDirection
    global slime_left
    global slime_right
    global running

    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    slime_left = pygame.transform.scale(pygame.image.load("images/Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
    slime_right = pygame.transform.scale(pygame.image.load("images/Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    bullet_add_increment = 2000
    bullet_count = 0
    
    bullets = []
    hit = False
    dead = False

    explosions = []

    difficulty = 1 + level / 15

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
                    print(bullet_type)
                    for i in range(len(bullet_type)):
                        if(bullet_type[i] == "speed"):
                            bullet_speed = random.randint((BULLET_VELOCITY - 1) * SPEED_AMOUNT, (BULLET_VELOCITY + 1) * SPEED_AMOUNT)
                            break
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
            noHoming = False
            for i in range(len(bullet.type)):
                if(bullet.type[i] == "homing"):
                    bullet.previousAngle = bullet.angle
                    angle = findAngle(player, bullet)
                    currentAngle = bullet.angle + angle
                    if(currentAngle > MAX_ANGLE):
                        bullet.angle = MAX_ANGLE
                    elif(currentAngle < -MAX_ANGLE):
                        bullet.angle = -MAX_ANGLE
                    else:
                        bullet.angle = currentAngle
                    amountInX = round(bullet.speed * math.sin(math.radians(bullet.angle)))
                    amountInY = round(bullet.speed * math.cos(math.radians(bullet.angle)))
                    bullet.hitBox.x += amountInX
                    bullet.hitBox.y += amountInY
                    noHoming = False
                    break
                else:
                    noHoming = True
            if(noHoming):
                bullet.hitBox.y += bullet.speed
            if bullet.hitBox.y > HEIGHT:
                for i in range(len(bullet.type)):
                    if(bullet.type[i] == "exploding"):
                        explosion = Explosion.Explosion(elapsed_time, False, pygame.Rect(bullet.hitBox.x - EXPLOSION_SIZE / 2, bullet.hitBox.y - EXPLOSION_SIZE, EXPLOSION_SIZE, EXPLOSION_SIZE))
                        explosions.append(explosion)
                bullets.remove(bullet)
            elif bullet.hitBox.y + bullet.hitBox.height >= player.y and bullet.hitBox.colliderect(player):
                for i in range(len(bullet.type)):
                    if(bullet.type[i] == "exploding"):
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