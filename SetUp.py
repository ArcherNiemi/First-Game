import pandas as pd
import os
import main

local_appdata = os.getenv("LOCALAPPDATA")  # e.g., C:\Users\<User>\AppData\Local
app_name = "BulletBarrage"
app_folder = os.path.join(local_appdata, app_name)

gameSaveData_path = os.path.join(app_folder, "gameSaveData.csv")
currentData_path = os.path.join(app_folder, "currentData.csv")
allData_path = os.path.join(app_folder, "allData.csv")

current_version = "0.0.4"

def setUp():
    print(app_folder)
    if not(os.path.exists(app_folder)):
        os.makedirs(app_folder, exist_ok=True)
    if not(os.path.exists(gameSaveData_path)):
        data = {"": [0]}
        df = pd.DataFrame(data)
        df.to_csv(gameSaveData_path, index=False)
    if not(os.path.exists(currentData_path)):
        data = {"": [0]}
        df = pd.DataFrame(data)
        df.to_csv(currentData_path, index=False)
    if not(os.path.exists(allData_path)):
        data = {"": [0]}
        df = pd.DataFrame(data)
        df.to_csv(allData_path, index=False)

    df1 = pd.read_csv(gameSaveData_path)
    df2 = pd.read_csv(currentData_path)
    df3 = pd.read_csv(allData_path)

    headers1 = df1.columns.tolist()
    headers2 = df2.columns.tolist()
    headers3 = df3.columns.tolist()

    print(headers1)
    print(headers2)
    print(headers3)

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

    gold = [0,0,0]
    high_score = [0,0,0]
    locked_upgrades_2 = [0,0,0]
    prestige_level = [0,0,0]
    current_loadout = [0,0,0]
    
    for i in range(3):
        if(not('gold' in headers2)):
            gold[i] = 0
        else:
            gold[i] = df2['gold'][i]
        if(not('high score' in headers2)):
            high_score[i] = 0
        else:
            high_score[i] = df2['high score'][i]
        if(not('locked upgrades' in headers2)):
            locked_upgrades_2[i] = main.UPGRADE_LIST
        else:
            locked_upgrades_2[i] = df2['locked upgrades'][i]
        if(not('prestige level' in headers2)):
            prestige_level[i] = 0
        else:
            prestige_level[i] = df2['prestige level'][i]
        if(not('current loadout' in headers2)):
            current_loadout[i] = [" "]
        else:
            current_loadout[i] = df2['current loadout'][i]

    if(not('current save' in headers3)):
        current_save = 0
    else:
        current_save = df3['current save'][0]

    data1 = {"level": [level],
             "upgrades": [upgrades],
             "locked upgrades": [locked_upgrades_1]}

    data2 = {"gold": [gold[0], gold[1], gold[2]],
            "high score": [high_score[0], high_score[1], high_score[2]],
            "prestige level": [prestige_level[0], prestige_level[1], prestige_level[2]],
            "locked upgrades": [locked_upgrades_2[0], locked_upgrades_2[1], locked_upgrades_2[2]],
            "current loadout": [current_loadout[0], current_loadout[1], current_loadout[2]]}

    data3 = {"version": [current_version],
             "current save": [current_save]}
    
    df1 = pd.DataFrame(data1)
    print(df1)
    df1.to_csv(gameSaveData_path, index=False)
    df2 = pd.DataFrame(data2)
    print(df2)
    df2.to_csv(currentData_path, index=False)
    df3 = pd.DataFrame(data3)
    print(df3)
    df3.to_csv(allData_path, index=False)


if __name__ == "__main__":
    setUp()