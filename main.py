import pygame
import time
import random
import math

pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")

UPGRADE_SIZE = 280
HEART_SIZE = WIDTH / 15
SHIELD_SIZE_WIDTH = 80
SHIELD_SIZE_HEIGHT = 55
ABILITY_SIZE = WIDTH / 20
SLIME_WIDTH = 60
SLIME_HEIGHT = 45

STAR_WIDTH = 10
STAR_HEIGHT = 30

BG = pygame.transform.scale(pygame.image.load("vecteezy_green-grass-field-with-blue-sky-ad-white-cloud-nature_40153656.jpg"), (WIDTH, HEIGHT))
EMPTY_HEART = pygame.transform.scale(pygame.image.load("empty_heart.png"), (HEART_SIZE, HEART_SIZE))
FULL_HEART = pygame.transform.scale(pygame.image.load("full_heart.png"), (HEART_SIZE, HEART_SIZE))
SHIELD = pygame.transform.scale(pygame.image.load("Blue_Force_Field.png"), (SHIELD_SIZE_WIDTH, SHIELD_SIZE_HEIGHT))
FRAME = pygame.transform.scale(pygame.image.load("Square_Frame_PNG_Clipart.png"), (UPGRADE_SIZE, UPGRADE_SIZE))
SHIELD_FULL = pygame.transform.scale(pygame.image.load("Blue_Force_Field_Full.png"), (ABILITY_SIZE, ABILITY_SIZE))
CLOCK = pygame.transform.scale(pygame.image.load("Time Clock Black Icon - 1000x1000.png"), (ABILITY_SIZE, ABILITY_SIZE))
SHRINK = pygame.transform.scale(pygame.image.load("resize-option.png"), (ABILITY_SIZE, ABILITY_SIZE))
BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullets-png-22781(1).png"), (STAR_HEIGHT + 10, STAR_WIDTH)), -90)
slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 35
PLAYER_VELOCITY = 8
PLAYER_STARTING_HEALTH = 3

STAR_VELOCITY = 8

FONT = pygame.font.SysFont("arial", 30)
FONT_START = pygame.font.SysFont("arial", 60)
FONT_END = pygame.font.SysFont("arial", 80)
FONT_LEVEL = pygame.font.SysFont("arial", 60)
FONT_UPGRADE = pygame.font.SysFont("arial", 30)
FONT_BUTTONS = pygame.font.SysFont("arial", 40)
FONT_TITLE = pygame.font.SysFont("arial", 80)

START_DELAY_BETWEEN_STARS = 2000
START_AMOUNT_OF_STARS_PER_WAVE = 5
START_LENGTH_OF_ROUNDS = 5

UPGRADE_LIST = ["Hp Increase", "Full Heal", "Shield", "Shrink", "Time Slow"]


SHRINK_SIZE = 2
TIME_SLOW_AMOUNT = 2

RARE_RARITY = 5

RARE_POWER = 2

TOTAL_AMOUNT_OF_UPGRADES = 5

COOL_DOWN = 5

health = PLAYER_STARTING_HEALTH
maxHp = PLAYER_STARTING_HEALTH
shieldLength = 0
shrinkLength = 0
timeSlowLength = 0

upgrade_stats = [maxHp, health, shieldLength, shrinkLength, timeSlowLength]
UPGRADE_STAT_AMOUNT = [1, 0, 0.25, 0.5, 0.75]

currentDirection = slime_left


def draw(player, elapsed_time, stars, shield, shrink, timeSlow, level, currentShieldCoolDown, currentShrinkCoolDown, currentTimeSlowCoolDown, shrink_time, shield_time, timeSlow_time):
    pygame.draw.rect(WIN, "red", player)
    for star in stars:
        pygame.draw.rect(WIN, "black", star)
    WIN.blit(BG, (0, 0))
    if(timeSlow):
        draw_rect_alpha(WIN, pygame.Color(128, 0, 128, 90), pygame.Rect(0,0,WIDTH, HEIGHT))
    for i in range(maxHp):
        if(health > i):
            WIN.blit(FULL_HEART, (WIDTH - (WIDTH / 15) * ((i + 1) * (0.9)) - WIDTH / 60, 0))
        else:
            WIN.blit(EMPTY_HEART, (WIDTH - (WIDTH / 15) * ((i + 1) * (0.9)) - WIDTH / 60, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
    WIN.blit(time_text, (10, 10))
    level_text = FONT.render(f"Level: {level}", 1, "black")
    WIN.blit(level_text, (10, 15 + time_text.get_height()))
    WIN.blit(SHIELD_FULL, (10, 20 + time_text.get_height() + level_text.get_height()))
    WIN.blit(SHRINK, (10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE))
    WIN.blit(CLOCK, (10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2))

    if(shieldLength <= 0):
        draw_rect_alpha(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 20 + time_text.get_height() + level_text.get_height(), ABILITY_SIZE, ABILITY_SIZE))
    elif(currentShieldCoolDown > 0):
        draw_transparent_arc(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 20 + time_text.get_height() + level_text.get_height(), ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * currentShieldCoolDown)/ COOL_DOWN)
    elif(shield):
        draw_transparent_arc(WIN, pygame.Color(0, 255, 0, 128), pygame.Rect(10, 20 + time_text.get_height() + level_text.get_height(), ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * (shield_time - elapsed_time + shieldLength))/shieldLength)
    
    if(shrinkLength <= 0):
        draw_rect_alpha(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE, ABILITY_SIZE, ABILITY_SIZE))
    elif(currentShrinkCoolDown > 0):
        draw_transparent_arc(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * currentShrinkCoolDown)/ COOL_DOWN)
    elif(shrink):
        draw_transparent_arc(WIN, pygame.Color(0, 255, 0, 128), pygame.Rect(10, 25 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * (shrink_time - elapsed_time + shrinkLength))/ shrinkLength)
    
    if(timeSlowLength <= 0):
        draw_rect_alpha(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2, ABILITY_SIZE, ABILITY_SIZE))
    elif(currentTimeSlowCoolDown > 0):
        draw_transparent_arc(WIN, pygame.Color(50, 50, 50, 128), pygame.Rect(10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * currentTimeSlowCoolDown)/ COOL_DOWN)
    elif(timeSlow):
        draw_transparent_arc(WIN, pygame.Color(0, 255, 0, 128), pygame.Rect(10, 30 + time_text.get_height() + level_text.get_height() + ABILITY_SIZE * 2, ABILITY_SIZE, ABILITY_SIZE), 0, (2 * math.pi * (timeSlow_time - time.time() + timeSlowLength))/ timeSlowLength)
    if(shrink):
        WIN.blit(currentDirection, (player.x - 5 / SHRINK_SIZE, player.y - 5 / SHRINK_SIZE))
    else:
        WIN.blit(currentDirection, (player.x - 5, player.y - 5))

    if(shield):
        WIN.blit(SHIELD, (player.x + player.width / 2 - SHIELD.get_width() / 2, HEIGHT - SHIELD.get_height()))

    for star in stars:
        WIN.blit(BULLET, (star.x, star.y))

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
    upgrade[0] = random.randint(0, TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY - 1)
    upgrade[1] = random.randint(0, TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY - 1)

    while(upgrade[0] % TOTAL_AMOUNT_OF_UPGRADES == upgrade[1] % TOTAL_AMOUNT_OF_UPGRADES):
        upgrade[1] = random.randint(0, TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY - 1)
    for i in range(2):
        if(upgrade[i] >= (TOTAL_AMOUNT_OF_UPGRADES * RARE_RARITY) - TOTAL_AMOUNT_OF_UPGRADES):
            rarity_increase[i] = RARE_POWER
        else:
            rarity_increase[i] = 1
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
                elif(rarity_increase[i] == RARE_POWER and not(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 1)):
                    if(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 0):
                        splitUpgrade.append(f"({upgrade_stats[t]} => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * RARE_POWER})")
                    elif(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 1):
                        splitUpgrade.append(f"({health} => {upgrade_stats[0]})")
                    else:
                        splitUpgrade.append(f"({upgrade_stats[t]}s => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t] * RARE_POWER}s)")
                    for p in range(len(splitUpgrade)):
                        upgrade_text = FONT_UPGRADE.render(splitUpgrade[p], 1, "green")
                        WIN.blit(upgrade_text, (WIDTH/((i+1) * 1.5) - upgrade_text.get_width()/2, HEIGHT/2 - (upgrade_text.get_height()/2) * ((len(splitUpgrade)) - p * 2) ))
                else:
                    if(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 0):
                        splitUpgrade.append(f"({upgrade_stats[t]} => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t]})")
                    elif(upgrade[i] % TOTAL_AMOUNT_OF_UPGRADES == 1):
                        splitUpgrade.append(f"({health} => {upgrade_stats[0]})")
                    else:
                        splitUpgrade.append(f"({upgrade_stats[t]}s => {upgrade_stats[t] + UPGRADE_STAT_AMOUNT[t]}s)")
                    for p in range(len(splitUpgrade)):
                        upgrade_text = FONT_UPGRADE.render(splitUpgrade[p], 1, "white")
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
                        print(clickedAbility)
                        print(rarity_increase[i])
                        number = rarity_increase[i]
                        run = False
    giveAbility(clickedAbility, number)
    
def giveAbility(clickedAblility, rarity_increase):
    global maxHp
    global health
    global shieldLength
    global shrinkLength
    global timeSlowLength
    global upgrade_stats
    if(clickedAblility == 0):
        maxHp += 1 * rarity_increase
    if(clickedAblility == 1):
        health = maxHp
    if(clickedAblility == 2):
        if(shieldLength == 0):
            shieldLength = 0.5
        else:
            shieldLength += 0.25 * rarity_increase
    if(clickedAblility == 3):
        if(shrinkLength == 0):
            shrinkLength = 1 
        else:
            shrinkLength += 0.5 * rarity_increase
    if(clickedAblility == 4):
        if(timeSlowLength == 0):
            timeSlowLength = 1.5 
        else:
            timeSlowLength += 0.75 * rarity_increase
    upgrade_stats = [maxHp, health, shieldLength, shrinkLength, timeSlowLength]


def main():
    level = 1
    startScreen()
    while(True):
        levelStart(level)
        run(level)
        levelEnd(level)
        upgradeScreen()
        level += 1

def run(level):
    global currentDirection
    global slime_left
    global slime_right

    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    slime_left = pygame.transform.scale(pygame.image.load("Slime_Left.png"), (SLIME_WIDTH, SLIME_HEIGHT))
    slime_right = pygame.transform.scale(pygame.image.load("Slime_Right.png"), (SLIME_WIDTH, SLIME_HEIGHT))

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    dead = False

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
            star_count += clock.tick(60 / TIME_SLOW_AMOUNT)
        else:
            star_count += clock.tick(60)
        elapsed_time = time.time() - start_time - amountOfTimeSlow
        if(timeSlow):
            amountOfTimeSlow = (time.time() - timeSlow_time) / 2 + totalAmountOfTimeSlow
        else:
            totalAmountOfTimeSlow = amountOfTimeSlow

        if(shield and elapsed_time - shield_time >= shieldLength):
            shield = False
            startShieldCoolDown = elapsed_time
        else:
            currentShieldCoolDown = startShieldCoolDown - elapsed_time + COOL_DOWN
        if(shrink and elapsed_time - shrink_time >= shrinkLength):
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
        if(timeSlow and time.time() - timeSlow_time >= timeSlowLength):
            timeSlow = False
            startTimeSlowCoolDown = time.time()
        else:
            currentTimeSlowCoolDown = startTimeSlowCoolDown - time.time() + COOL_DOWN
        if(timeSlow):
            star_add_increment = int(round(random.randint(int(round(START_DELAY_BETWEEN_STARS / difficulty) / 3), int(round(START_DELAY_BETWEEN_STARS / difficulty))) / 2))
        else:
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
        if keys[pygame.K_1] and currentShieldCoolDown <= 0 and not(shield) and shieldLength > 0:
            shield = True
            shield_time = elapsed_time
        if keys[pygame.K_2] and currentShrinkCoolDown <= 0 and not(shrink) and shrinkLength > 0:
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
        if keys[pygame.K_3] and currentTimeSlowCoolDown <= 0 and not(timeSlow) and timeSlowLength > 0:
            timeSlow = True
            timeSlow_time = time.time()
        if keys[pygame.K_LEFT] and player.x - currentPlayerVelocity >= 0:
            player.x -= currentPlayerVelocity
            currentDirection = slime_left
        if keys[pygame.K_RIGHT] and player.x + currentPlayerVelocity + player.width <= WIDTH:
            player.x += currentPlayerVelocity
            currentDirection = slime_right

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                if(not(shield)):
                    hit = True
                break

        if hit:
            global health
            health -= 1
            hit = False
            if(health <= 0):
                dead = True

        draw(player, elapsed_time, stars, shield, shrink, timeSlow, level, currentShieldCoolDown, currentShrinkCoolDown, currentTimeSlowCoolDown, shrink_time, shield_time, timeSlow_time)

        if dead:
            lost_text = FONT_END.render("You Lost", 1, "black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()))
            lost_text = FONT_END.render(f"Levels Beaten: {level - 1}", 1, "black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()

            

if __name__ == "__main__":
    main()