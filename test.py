import os

app_name = "BulletBarrage"
appdata = os.getenv("LOCALAPPDATA")  # e.g., C:\Users\YourName\AppData\Roaming
folder = os.path.join(appdata, app_name)

print(f"heloo {folder}")