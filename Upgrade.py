SHIELD_UPGRADE_AMOUNT = 0.25
SHRINK_UPGRADE_AMOUNT = 0.5
TIME_SLOW_UPGRADE_AMOUNT = 0.75


SHIELD_COOLDOWN = 5
SHRINK_COOLDOWN = 5
TIME_SLOW_COOLDOWN = 5

class Upgrade:
    def __init__(self, type: str, rarity: str, amountIncrease: float, amount: float, coolDown: float):
        self.rarity = rarity
        if(rarity == "common"):
            self.rarityNum = 1
        elif(rarity == "rare"):
            self.rarityNum = 2
        elif(rarity == "epic"):
            self.rarityNum = 2
        elif(rarity == "legendary"):
            self.rarityNum = 4

        if(type == "ability"):
            self.duration = amount
            self.durationIncrease = amountIncrease
            self.coolDown = coolDown
        elif(type == "stat increase"):
            self.amount = amountIncrease

def upgrade(clickedAbility, rarityIncrease, maxHp):
    if(clickedAbility == 0):
        return increaseHp(rarityIncrease)
    elif(clickedAbility == 1):
        return healUp(rarityIncrease, maxHp)
    elif(clickedAbility == 2):
        return shieldIncrease(rarityIncrease)
    elif(clickedAbility == 3):
        return shrinkIncrease(rarityIncrease)
    elif(clickedAbility == 4):
        return timeSlowIncrease(rarityIncrease)


def increaseHp(rarityIncrease):
    return hpIncrease.amount * rarityIncrease

def healUp(rarityIncrease, maxHp, health):
    healAmount = heal.amount * rarityIncrease
    if(healAmount + health >= maxHp):
        return maxHp - health
    else:
        return healAmount

def shieldIncrease(rarityIncrease):
    if(shield.duration == 0):
        return shield.durationIncrease * 2
    else:
        return shield.durationIncrease * rarityIncrease

def shrinkIncrease(rarityIncrease):
    if(shrink.duration == 0):
        return shrink.durationIncrease * 2
    else:
        return shrink.durationIncrease * rarityIncrease

def timeSlowIncrease(rarityIncrease):
    if(timeSlow.duration == 0):
        return timeSlow.durationIncrease * 2
    else:
        return timeSlow.durationIncrease * rarityIncrease


hpIncrease = Upgrade("stat increase", "common", 1, None, None)
heal = Upgrade("stat increase", "common", 3, None,  None)
shield = Upgrade("ability", "common", SHIELD_UPGRADE_AMOUNT, 0, SHIELD_COOLDOWN)
shrink = Upgrade("ability", "common", SHRINK_UPGRADE_AMOUNT, 0, SHRINK_COOLDOWN)
timeSlow = Upgrade("ability", "common", TIME_SLOW_UPGRADE_AMOUNT, 0, TIME_SLOW_COOLDOWN)