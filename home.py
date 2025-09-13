import main
import pygame
import csv
import pandas as pd
import os
import ast

pygame.init()

FONT_HOME = pygame.font.SysFont("arial", 80)
FONT_PLAY = pygame.font.SysFont("arial", 45)
FONT_GOLD = pygame.font.SysFont("arial", 45)
FONT_UNLOCK = pygame.font.SysFont("arial", 20)
FONT_TITLE = pygame.font.SysFont("arial", 100)
FONT_SHOP = pygame.font.SysFont("arial", 25)
FONT_INVENTORY = pygame.font.SysFont("arial", 25)

PLAY_BOX_SIZE = 400
GOLD_SIZE = 40
UNLOCK_GOLD_SIZE = 20
ICON_SIZE = 150

SHOP_Y = 300
SCREEN_X = 500
SCREEN_Y = 625
SCREEN_PIXIL = int(SCREEN_X / 100)

SLOT_SIZE = 60

PLAY_BOX = pygame.transform.scale(pygame.image.load("images/play_box.png"), (PLAY_BOX_SIZE,PLAY_BOX_SIZE))
GOLD = pygame.transform.scale(pygame.image.load("images/BB_Coin.png"), (GOLD_SIZE, GOLD_SIZE))
SHOP = pygame.transform.scale(pygame.image.load("images/[CITYPNG.COM]Download Shopping Store Market Icon PNG - 800x800.png"), (ICON_SIZE, ICON_SIZE))
INVENTORY = pygame.transform.scale(pygame.image.load("images/pngtree-pair-of-crossed-knight-swords-against-background-of-wooden-scandinavian-shield-png-image_6318863.png"), (ICON_SIZE, ICON_SIZE + 30))
INVENTORY_SCREEN_UPGRADE_TAB = pygame.transform.scale(pygame.image.load("images/inventory_screen_upgrade_tab.png"), (SCREEN_X, SCREEN_Y))
INVENTORY_SCREEN_COSMETICS_TAB = pygame.transform.scale(pygame.image.load("images/inventory_screen_cosmetics_tab.png"), (SCREEN_X, SCREEN_Y))
SHOP_SCREEN_UPGRADE_TAB = pygame.transform.scale(pygame.image.load("images/BB_Shop_-_blue_tab_selected.png"), (SCREEN_X, SCREEN_Y))
SHOP_SCREEN_COSMETICS_TAB = pygame.transform.scale(pygame.image.load("images/BB_Shop_-_yellow_tab_selected.png"), (SCREEN_X, SCREEN_Y))
SHOP_SCREEN_PRESTIGE_TAB = pygame.transform.scale(pygame.image.load("images/BB_Shop_-_red_tab_selected.png"), (SCREEN_X, SCREEN_Y))
HEAL = pygame.transform.scale(pygame.image.load("images/heal.png"), (SLOT_SIZE, SLOT_SIZE))
HP_INCREASE = pygame.transform.scale(pygame.image.load("images/hp_increase.png"), (SLOT_SIZE, SLOT_SIZE))
PASSIVE_HEAL = pygame.transform.scale(pygame.image.load("images/passive_heal.png"), (SLOT_SIZE, SLOT_SIZE))
TEMP_HEARTS = pygame.transform.scale(pygame.image.load("images/temp_hearts.png"), (SLOT_SIZE, SLOT_SIZE))
LUCK = pygame.transform.scale(pygame.image.load("images/luck.png"), (SLOT_SIZE, SLOT_SIZE))

SCREEN_TOP_LEFT = (main.WIDTH / 2 - SCREEN_X / 2, main.HEIGHT / 2 - SCREEN_Y / 2)

PLAY_BOX_PIXIL = PLAY_BOX_SIZE / 100

CONTINUE_LOCATION = (main.WIDTH - PLAY_BOX_PIXIL * 72, main.WIDTH - PLAY_BOX_PIXIL * 6, main.HEIGHT - PLAY_BOX_PIXIL * 56, main.HEIGHT - PLAY_BOX_PIXIL * 35)
NEW_GAME_LOCATION = (main.WIDTH - PLAY_BOX_PIXIL * 72, main.WIDTH - PLAY_BOX_PIXIL * 6, main.HEIGHT - PLAY_BOX_PIXIL * 26, main.HEIGHT - PLAY_BOX_PIXIL * 6)
SHOP_LOCATION = (10, 10 + ICON_SIZE, SHOP_Y, SHOP_Y + ICON_SIZE)
SHOP_SCREEN_LOCATIONS = (((SCREEN_TOP_LEFT[1] + 18 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 29 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 4 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 30 * SCREEN_PIXIL), 
                          (SCREEN_TOP_LEFT[0] + 36 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 63 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 69 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 96 * SCREEN_PIXIL)), 
                          ((SCREEN_TOP_LEFT[0] + 88 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 99 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[1] + 1 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 12 * SCREEN_PIXIL)),
                          (SCREEN_TOP_LEFT[0] + 59 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 1.5 * SCREEN_PIXIL),
                          (SCREEN_TOP_LEFT[0] + 16.5 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 49 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 82 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 23 * SCREEN_PIXIL))

SHOP_SCREEN_UPGRADE_TAB_LOCATIONS = ((SCREEN_TOP_LEFT[0] + 6 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 36 * SCREEN_PIXIL), #unlock text
                                     ((SCREEN_TOP_LEFT[0] + 6 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 42 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 96 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 77 * SCREEN_PIXIL))) #unlock start and end

INVENTORY_LOCATION = (10, 10 + ICON_SIZE,  SHOP_Y + SHOP.get_height() + 15, SHOP_Y + SHOP.get_height() + 15 + INVENTORY.get_height())
INVENTORY_SCREEN_LOCATIONS = (((SCREEN_TOP_LEFT[1] + 1 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 12 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 79 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 88 * SCREEN_PIXIL),(SCREEN_TOP_LEFT[0] + 89 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 98 * SCREEN_PIXIL)), #x and check mark locations
                              ((SCREEN_TOP_LEFT[1] + 19 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 29 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 5 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 47 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 54 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 97 * SCREEN_PIXIL)), #tab locations
                              (SCREEN_TOP_LEFT[1] + 23 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 26 * SCREEN_PIXIL, SCREEN_TOP_LEFT[0] + 75 * SCREEN_PIXIL)) #word locations
INVENTORY_TOP = ((SCREEN_TOP_LEFT[0] + 5 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 36 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 96 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 64 * SCREEN_PIXIL))
INVENTORY_BOTTOM = ((SCREEN_TOP_LEFT[0] + 5 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 71 * SCREEN_PIXIL), (SCREEN_TOP_LEFT[0] + 96 * SCREEN_PIXIL, SCREEN_TOP_LEFT[1] + 121 * SCREEN_PIXIL))

INVENTORY_SLOTS_TOP = []
INVENTORY_SLOTS_BOTTOM = []

INVENTORY_ITEMS_TOP = []
INVENTORY_ITEMS_BOTTOM = []

SHOP_SLOTS = []

IMAGES = [HP_INCREASE, LUCK, PASSIVE_HEAL, TEMP_HEARTS, HEAL, pygame.transform.scale(main.SHRINK,(SLOT_SIZE, SLOT_SIZE)), pygame.transform.scale(main.CLOCK,(SLOT_SIZE, SLOT_SIZE)), pygame.transform.scale(main.SHIELD_FULL,(SLOT_SIZE, SLOT_SIZE)), pygame.transform.scale(main.TYPE_DECREASE,(SLOT_SIZE, SLOT_SIZE)), pygame.transform.scale(main.SCREEN_WIPE,(SLOT_SIZE, SLOT_SIZE))]
UPGRADE_PRICES = [10, 50, 50, 50, 5, 25, 25, 25, 100, 250]

SHOP_BACKGROUND = pygame.Rect(300, 100, 300, 500)

local_appdata = os.getenv("LOCALAPPDATA")  # e.g., C:\Users\<User>\AppData\Local
app_name = "BulletBarrage"
app_folder = os.path.join(local_appdata, app_name)

gameSaveData_path = os.path.join(app_folder, "gameSaveData.csv")
allData_path = os.path.join(app_folder, "allData.csv")
print(app_folder)

def homePage():
    print(allData_path)
    run = True
    createInventorySlots()
    createUnlockSlots()
    createFiles()
    df = pd.read_csv(allData_path)
    amountOfGold = df["gold"][0]
    highScore = df["high score"][0]
    lockedUpgrades = ast.literal_eval(df["locked upgrades"][0])
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
                elif(clickpos[0] >= SHOP_LOCATION[0] and clickpos[0] <= SHOP_LOCATION[1] and clickpos[1] >= SHOP_LOCATION[2] and clickpos[1] <= SHOP_LOCATION[3]):
                    shopPage(amountOfGold, lockedUpgrades)
                elif(clickpos[0] >= INVENTORY_LOCATION[0] and clickpos[0] <= INVENTORY_LOCATION[1] and clickpos[1] >= INVENTORY_LOCATION[2] and clickpos[1] <= INVENTORY_LOCATION[3]):
                    inventoryPage(lockedUpgrades)
        homePageDraw(amountOfGold, highScore)

def homePageDraw(amountOfGold, highScore):
    main.WIN.blit(main.BG, (0, 0))
    main.WIN.blit(PLAY_BOX, (main.WIDTH - PLAY_BOX.get_width(), main.HEIGHT - PLAY_BOX.get_height()))

    gold_text = FONT_GOLD.render(f"{amountOfGold}", 1, "gold")
    main.WIN.blit(GOLD, (main.WIDTH - GOLD.get_width() - gold_text.get_width() - 15, 5))
    main.WIN.blit(gold_text, (main.WIDTH - gold_text.get_width() - 10, 0))

    high_score_text = FONT_GOLD.render(f"High Score: {highScore}", 1, "black")
    main.WIN.blit(high_score_text, (10, 10))

    main.WIN.blit(SHOP, (10, SHOP_Y))

    main.WIN.blit(INVENTORY, (10, SHOP_Y + SHOP.get_height() + 15))

    inventory_text = FONT_INVENTORY.render("Inventory", 1, "black")
    main.WIN.blit(inventory_text, (10 + ICON_SIZE / 2 - inventory_text.get_width() / 2, SHOP_Y + SHOP.get_height() + 10))

    title_text = FONT_TITLE.render("Bullet Barage", 1, "black")
    play_text = FONT_HOME.render("Play", 1, "black")
    continue_text = FONT_PLAY.render("Continue", 1, "black")
    new_game_text = FONT_PLAY.render("New Game", 1, "black")
    main.WIN.blit(title_text, (main.WIDTH / 2 - title_text.get_width() / 2, 50))
    main.WIN.blit(play_text, (main.WIDTH - PLAY_BOX.get_width() / 2 - play_text.get_width() / 2, main.HEIGHT - PLAY_BOX.get_height() * 0.8 - play_text.get_height() / 2))
    main.WIN.blit(continue_text, (main.WIDTH - 78 * PLAY_BOX.get_width() / 200 - continue_text.get_width() / 2, main.HEIGHT - PLAY_BOX.get_height() * 0.45 - continue_text.get_height() / 2))
    main.WIN.blit(new_game_text, (main.WIDTH -  78 * PLAY_BOX.get_width() / 200 - new_game_text.get_width() / 2, main.HEIGHT - PLAY_BOX.get_height() * 0.15 - new_game_text.get_height() / 2))

    pygame.display.update()

def shopPage(amountOfGold, lockedUpgrades):
    currentScreen = ["upgrade screen", SHOP_SCREEN_UPGRADE_TAB]
    run = True
    sortedUpgrades = sortLockedUpgrades(lockedUpgrades)
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = event.pos
                if(clickpos[1] >= SHOP_SCREEN_LOCATIONS[0][0][0] and clickpos[1] <= SHOP_SCREEN_LOCATIONS[0][0][1]):
                    if(clickpos[0] >= SHOP_SCREEN_LOCATIONS[0][1][0] and clickpos[0] <= SHOP_SCREEN_LOCATIONS[0][1][1]):
                        currentScreen = ["upgrade screen", SHOP_SCREEN_UPGRADE_TAB]
                    elif(clickpos[0] >= SHOP_SCREEN_LOCATIONS[0][2][0] and clickpos[0] <= SHOP_SCREEN_LOCATIONS[0][2][1]):
                        currentScreen = ["cosmetic screen", SHOP_SCREEN_COSMETICS_TAB]
                    elif(clickpos[0] >= SHOP_SCREEN_LOCATIONS[0][3][0] and clickpos[0] <= SHOP_SCREEN_LOCATIONS[0][3][1]):
                        currentScreen = ["prestige screen", SHOP_SCREEN_PRESTIGE_TAB]
                elif(clickpos[0] >= SHOP_SCREEN_LOCATIONS[1][0][0] and clickpos[0] <= SHOP_SCREEN_LOCATIONS[1][0][1] and 
                     clickpos[1] >= SHOP_SCREEN_LOCATIONS[1][1][0] and clickpos[1] <= SHOP_SCREEN_LOCATIONS[1][1][1]):
                    run = False
                for i in range(len(sortedUpgrades[0])):
                    if(clickpos[0] >= SHOP_SLOTS[i][0] and clickpos[1] >= SHOP_SLOTS[i][1] and clickpos[0] <= SHOP_SLOTS[i][0] + SLOT_SIZE and clickpos[1] <= SHOP_SLOTS[i][1] + SLOT_SIZE):
                        print(f"{sortedUpgrades[0][i]}")
                        run = False
                        buyItem(sortedUpgrades, i)
        shopPageDraw(currentScreen, amountOfGold, sortedUpgrades)

def shopPageDraw(currentScreen, amountOfGold, sortedUpgrades):
    main.WIN.blit(main.BG, (0, 0))
    main.WIN.blit(currentScreen[1], (main.WIDTH / 2 - SCREEN_X / 2, main.HEIGHT / 2 - SCREEN_Y / 2))

    gold_text = FONT_GOLD.render(f"{amountOfGold}", 1, "gold")
    main.WIN.blit(gold_text, SHOP_SCREEN_LOCATIONS[2])

    upgrade_text = FONT_SHOP.render("Upgrade", 1, "black")
    main.WIN.blit(upgrade_text, (SHOP_SCREEN_LOCATIONS[3][0] - upgrade_text.get_width() / 2, SHOP_SCREEN_LOCATIONS[3][3]  - upgrade_text.get_height() / 2))

    cosmetics_text = FONT_SHOP.render("Cosmetics", 1, "black")
    main.WIN.blit(cosmetics_text, (SHOP_SCREEN_LOCATIONS[3][1] - cosmetics_text.get_width() / 2, SHOP_SCREEN_LOCATIONS[3][3]  - cosmetics_text.get_height() / 2))

    prestige_text = FONT_SHOP.render("Prestige", 1, "black")
    main.WIN.blit(prestige_text, (SHOP_SCREEN_LOCATIONS[3][2] - prestige_text.get_width() / 2, SHOP_SCREEN_LOCATIONS[3][3]  - prestige_text.get_height() / 2))

    if(currentScreen[0] == "upgrade screen"):
        unlock_text = FONT_SHOP.render("Unlock:", 1, "black")
        main.WIN.blit(unlock_text, (SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[0][0], SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[0][1]))
        for i in range(len(sortedUpgrades[0])):
            for t in range(len(main.UPGRADE_LIST)):
                if(sortedUpgrades[0][i] == main.UPGRADE_LIST[t]):
                    main.WIN.blit(IMAGES[t], SHOP_SLOTS[i])
                main.WIN.blit(pygame.transform.scale(GOLD, (UNLOCK_GOLD_SIZE,UNLOCK_GOLD_SIZE)), (SHOP_SLOTS[i][0], SHOP_SLOTS[i][1] + SLOT_SIZE))
                price_text = FONT_UNLOCK.render(f"{sortedUpgrades[1][i]}", "1", "gold")
                main.WIN.blit(price_text, (SHOP_SLOTS[i][0]+ UNLOCK_GOLD_SIZE, SHOP_SLOTS[i][1] + SLOT_SIZE))

    pygame.display.update()

def buyItem(sortedUpgrades, location):
    df = pd.read_csv(allData_path)
    lockedUpgrades = ast.literal_eval(df["locked upgrades"][0])
    gold = df["gold"][0]

    print(lockedUpgrades)
    print(gold)
    lockedUpgrades.remove(sortedUpgrades[0][location])
    gold -= sortedUpgrades[1][location]
    print(lockedUpgrades)
    print(gold)

    df.at[0, "gold"] = gold
    df.at[0, "locked upgrades"] = lockedUpgrades
    df.to_csv(allData_path, index=False)
    shopPage(gold, lockedUpgrades)
    

            

def inventoryPage(lockedUpgrades):
    global INVENTORY_ITEMS_TOP
    global INVENTORY_ITEMS_BOTTOM
    inventoryItemsTop = INVENTORY_ITEMS_TOP.copy()
    inventoryItemsBottom = INVENTORY_ITEMS_BOTTOM.copy()
    currentScreen = ["upgrade screen", INVENTORY_SCREEN_UPGRADE_TAB]
    setUpInventory(lockedUpgrades)

    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = event.pos
                if(clickpos[1] >= INVENTORY_SCREEN_LOCATIONS[0][0][0] and clickpos[1] <= INVENTORY_SCREEN_LOCATIONS[0][0][1]):
                    if(clickpos[0] >= INVENTORY_SCREEN_LOCATIONS[0][1][0] and clickpos[0] <= INVENTORY_SCREEN_LOCATIONS[0][1][1]):
                        print("x")
                        run = False
                    elif(clickpos[0] >= INVENTORY_SCREEN_LOCATIONS[0][2][0] and clickpos[0] <= INVENTORY_SCREEN_LOCATIONS[0][2][1]):
                        print("check")
                        INVENTORY_ITEMS_TOP = inventoryItemsTop.copy()
                        INVENTORY_ITEMS_BOTTOM = inventoryItemsBottom.copy()
                        updateCurrentLoadout()
                        print(INVENTORY_ITEMS_TOP)
                        print(INVENTORY_ITEMS_BOTTOM)
                        run = False
                elif(clickpos[1] >= INVENTORY_SCREEN_LOCATIONS[1][0][0] and clickpos[1] <= INVENTORY_SCREEN_LOCATIONS[1][0][1]):
                    if(clickpos[0] >= INVENTORY_SCREEN_LOCATIONS[1][1][0] and clickpos[0] <= INVENTORY_SCREEN_LOCATIONS[1][1][1]):
                        currentScreen[0] = "upgrade screen"
                        currentScreen[1] = INVENTORY_SCREEN_UPGRADE_TAB
                    elif(clickpos[0] >= INVENTORY_SCREEN_LOCATIONS[1][2][0] and clickpos[0] <= INVENTORY_SCREEN_LOCATIONS[1][2][1]):
                        currentScreen[0] = "cosmetics screen"
                        currentScreen[1] = INVENTORY_SCREEN_COSMETICS_TAB
                if(currentScreen[0] == "upgrade screen"):
                    for i in range(len(INVENTORY_SLOTS_TOP)):
                        if(clickpos[0] >= INVENTORY_SLOTS_TOP[i][0] and clickpos[1] >= INVENTORY_SLOTS_TOP[i][1] and
                        clickpos[0] <= INVENTORY_SLOTS_TOP[i][0] + SLOT_SIZE and clickpos[1] <= INVENTORY_SLOTS_TOP[i][1] + SLOT_SIZE):
                            print(i)
                            if(not(inventoryItemsTop == "")):
                                for t in range(len(inventoryItemsBottom)):
                                    if(inventoryItemsBottom[t] == ""):
                                        inventoryItemsBottom[t] = inventoryItemsTop[i]
                                        inventoryItemsTop[i] = ""
                                        print(inventoryItemsTop)
                                        break
                            break
                    for i in range(len(INVENTORY_SLOTS_BOTTOM)):
                        if(clickpos[0] >= INVENTORY_SLOTS_BOTTOM[i][0] and clickpos[1] >= INVENTORY_SLOTS_BOTTOM[i][1] and
                        clickpos[0] <= INVENTORY_SLOTS_BOTTOM[i][0] + SLOT_SIZE and clickpos[1] <= INVENTORY_SLOTS_BOTTOM[i][1] + SLOT_SIZE):
                            print(i)
                            if(not(inventoryItemsBottom == "")):
                                for t in range(len(inventoryItemsTop)):
                                    if(inventoryItemsTop[t] == ""):
                                        inventoryItemsTop[t] = inventoryItemsBottom[i]
                                        inventoryItemsBottom[i] = ""
                                        print(inventoryItemsBottom)
                                        break
                            break
        inventoryPageDraw(inventoryItemsTop, inventoryItemsBottom, currentScreen)

def inventoryPageDraw(inventoryItemsTop, inventoryItemsBottom, currentScreen):
    main.WIN.blit(main.BG, (0, 0))
    main.WIN.blit(currentScreen[1], (main.WIDTH / 2 - SCREEN_X / 2, main.HEIGHT / 2 - SCREEN_Y / 2))

    if(currentScreen[0] == "upgrade screen"):
        for i in range(len(main.UPGRADE_LIST)):
            for t in range(len(inventoryItemsTop)):
                if(inventoryItemsTop[t] == main.UPGRADE_LIST[i]):
                    main.WIN.blit(IMAGES[i], INVENTORY_SLOTS_TOP[t])
                    break
            for t in range(len(inventoryItemsBottom)):
                if(inventoryItemsBottom[t] == main.UPGRADE_LIST[i]):
                    main.WIN.blit(IMAGES[i], INVENTORY_SLOTS_BOTTOM[t])
                    break
    
    upgrade_text = FONT_SHOP.render("Upgrade", 1, "black")
    main.WIN.blit(upgrade_text, (INVENTORY_SCREEN_LOCATIONS[2][1] - upgrade_text.get_width() / 2, INVENTORY_SCREEN_LOCATIONS[2][0]  - upgrade_text.get_height() / 2))

    cosmetics_text = FONT_SHOP.render("Cosmetics", 1, "black")
    main.WIN.blit(cosmetics_text, (INVENTORY_SCREEN_LOCATIONS[2][2] - cosmetics_text.get_width() / 2, INVENTORY_SCREEN_LOCATIONS[2][0]  - cosmetics_text.get_height() / 2))

    # for i in range(len(INVENTORY_SLOTS_TOP)):
    #     pygame.draw.rect(main.WIN, "orange", pygame.Rect(INVENTORY_SLOTS_TOP[i][0], INVENTORY_SLOTS_TOP[i][1], SLOT_SIZE, SLOT_SIZE))
    # for i in range(len(INVENTORY_SLOTS_BOTTOM)):
    #     pygame.draw.rect(main.WIN, "orange", pygame.Rect(INVENTORY_SLOTS_BOTTOM[i][0], INVENTORY_SLOTS_BOTTOM[i][1], SLOT_SIZE, SLOT_SIZE))

    pygame.display.update()

def updateCurrentLoadout():
    df = pd.read_csv(allData_path)
    currentLoadoutList = []
    for i in range(len(INVENTORY_ITEMS_TOP)):
        if(INVENTORY_ITEMS_TOP[i] != ""):
            currentLoadoutList.append(INVENTORY_ITEMS_TOP[i])
    
    print(currentLoadoutList)
    df.at[0, "current loadout"] = currentLoadoutList
    df.to_csv(allData_path, index=False)
    print(f"current: {df["current loadout"][0]}")

def setUpInventory(lockedUpgrades):
    global INVENTORY_ITEMS_TOP
    global INVENTORY_ITEMS_BOTTOM

    df = pd.read_csv(allData_path)
    current_loadout = ast.literal_eval(df["current loadout"][0])
    print(f"thing thing{current_loadout}")
    unlockedUpgrades = findUnlockedUpgrades(lockedUpgrades)
    
    for i in range(len(unlockedUpgrades)):
        if(unlockedUpgrades[i] in current_loadout):
            for t in range(len(INVENTORY_ITEMS_TOP)):
                if(INVENTORY_ITEMS_TOP[t] == ""):
                    INVENTORY_ITEMS_TOP[t] = unlockedUpgrades[i]
                    break
        else:
            for t in range(len(INVENTORY_ITEMS_BOTTOM)):
                if(INVENTORY_ITEMS_BOTTOM[t] == ""):
                    INVENTORY_ITEMS_BOTTOM[t] = unlockedUpgrades[i]
                    break
    print(INVENTORY_ITEMS_TOP)
    print(INVENTORY_ITEMS_BOTTOM)

def findUnlockedUpgrades(lockedUpgrades):
    unlockedUpgrades = []
    for i in range(len(main.UPGRADE_LIST)):
        if(not(main.UPGRADE_LIST[i] in lockedUpgrades)):
            unlockedUpgrades.append(main.UPGRADE_LIST[i])
    return unlockedUpgrades


def createFiles():
    if not(os.path.exists(app_folder)):
        os.makedirs(app_folder, exist_ok=True)
    if not(os.path.exists(gameSaveData_path)):
        data = {"level": [0]}
        df = pd.DataFrame(data)
        df.to_csv(gameSaveData_path, index=False)
    if not(os.path.exists(allData_path)):
        data = {"gold": [362],
                "high score": [50],
                "locked upgrades": [main.UPGRADE_LIST],
                "current loadout": [" "]}
        df = pd.DataFrame(data)
        df.to_csv(allData_path, index=False)

def createInventorySlots():
    global INVENTORY_SLOTS_TOP
    global INVENTORY_SLOTS_BOTTOM
    global INVENTORY_ITEMS_TOP
    global INVENTORY_ITEMS_BOTTOM

    current_location = [INVENTORY_TOP[0][0], INVENTORY_TOP[0][1]]
    print(INVENTORY_TOP)
    while(current_location[1] + SLOT_SIZE <= INVENTORY_TOP[1][1]):
        while(current_location[0] + SLOT_SIZE <= INVENTORY_TOP[1][0]):
            INVENTORY_SLOTS_TOP.append(current_location.copy())
            INVENTORY_ITEMS_TOP.append("")
            print(current_location)
            current_location[0] += SLOT_SIZE + 5
        current_location[1] += SLOT_SIZE + 5
        current_location[0] = INVENTORY_TOP[0][0]

    current_location = [INVENTORY_BOTTOM[0][0], INVENTORY_BOTTOM[0][1]]
    print(INVENTORY_BOTTOM)
    while(current_location[1] + SLOT_SIZE <= INVENTORY_BOTTOM[1][1]):
        while(current_location[0] + SLOT_SIZE <= INVENTORY_BOTTOM[1][0]):
            INVENTORY_SLOTS_BOTTOM.append(current_location.copy())
            INVENTORY_ITEMS_BOTTOM.append("")
            print(current_location)
            current_location[0] += SLOT_SIZE + 5
        current_location[1] += SLOT_SIZE + 5
        current_location[0] = INVENTORY_BOTTOM[0][0]
    print(INVENTORY_SLOTS_BOTTOM)

def createUnlockSlots():
    global SHOP_SLOTS

    current_location = [SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[1][0][0], SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[1][0][1]]
    print(INVENTORY_TOP)
    while(current_location[1] + SLOT_SIZE <= SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[1][1][1]):
        while(current_location[0] + SLOT_SIZE <= SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[1][1][0]):
            SHOP_SLOTS.append(current_location.copy())
            current_location[0] += SLOT_SIZE + 5
        current_location[1] += SLOT_SIZE + 30
        current_location[0] = SHOP_SCREEN_UPGRADE_TAB_LOCATIONS[1][0][0]

def sortLockedUpgrades(lockedUpgrades):
    sortedList = [[],[]]

    for i in range(200):
        for t in range(len(UPGRADE_PRICES)):
            if(i * 5 == UPGRADE_PRICES[t]):
                if(main.UPGRADE_LIST[t] in lockedUpgrades):
                    sortedList[0].append(main.UPGRADE_LIST[t])
                    sortedList[1].append(UPGRADE_PRICES[t])
    return sortedList

        

if __name__ == "__main__":
    homePage()