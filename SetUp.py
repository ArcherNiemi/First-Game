import pandas as pd
import os
import main

local_appdata = os.getenv("LOCALAPPDATA")  # e.g., C:\Users\<User>\AppData\Local
app_name = "BulletBarrage"
app_folder = os.path.join(local_appdata, app_name)

gameSaveData_path = os.path.join(app_folder, "gameSaveData.csv")
allData_path = os.path.join(app_folder, "allData.csv")

current_version = "0.0.2"

def setUp():
    if not(os.path.exists(app_folder)):
        os.makedirs(app_folder, exist_ok=True)
    if not(os.path.exists(gameSaveData_path)):
        data = {}
        df = pd.DataFrame(data)
        df.to_csv(gameSaveData_path, index=False)
    if not(os.path.exists(allData_path)):
        data = {}
        df = pd.DataFrame(data)
        df.to_csv(gameSaveData_path, index=False)

    df1 = pd.read_csv(gameSaveData_path)
    df2 = pd.read_csv(allData_path)

    headers1 = df1.columns.tolist()
    headers2 = df2.columns.tolist()

    print(headers1)
    print(headers2)

    print(gameSaveData_path)

    if(not('level' in headers1)):
        level = 0
    else:
        level = df1['level'][0]
    if(not('upgrades' in headers1)):
        upgrades = []
    else:
        upgrades = df1['upgrades'][0]
    if(not('locked upgrades' in headers1)):
        locked_upgrades_1 = []
    else:
        locked_upgrades_1 = df1['locked upgrades'][0]
    
    if(not('gold' in headers2)):
        gold = 0
    else:
        gold = df2['gold'][0]
    if(not('high score' in headers2)):
        high_score = 0
    else:
        high_score = df2['high score'][0]
    if(not('locked upgrades' in headers2)):
        locked_upgrades_2 = [main.UPGRADE_LIST]
    else:
        locked_upgrades_2 = df2['locked upgrades'][0]
    if(not('prestige level' in headers2)):
        prestige_level = 0
    else:
        prestige_level = df2['prestige level'][0]
    if(not('current loadout' in headers2)):
        current_loadout = [" "]
    else:
        current_loadout = df2['current loadout'][0]

    data1 = {"level": [level],
             "upgrades": [upgrades],
             "locked upgrades": [locked_upgrades_1]}

    data2 = {"gold": [gold],
            "high score": [high_score],
            "prestige level": [prestige_level],
            "version": [current_version],
            "locked upgrades": [locked_upgrades_2],
            "current loadout": [current_loadout]}
    
    df1 = pd.DataFrame(data1)
    print(df1)
    df1.to_csv(gameSaveData_path, index=False)
    df2 = pd.DataFrame(data2)
    print(df2)
    df2.to_csv(allData_path, index=False)


if __name__ == "__main__":
    setUp()