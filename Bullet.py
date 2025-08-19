import pygame

class Bullet:
    def __init__(self, speed: float, type: tuple, hitBox: pygame.Rect):
        self.speed = speed
        self.type = type
        self.hitBox = hitBox
        for i in range(len(type)):
            if(type[i] == "homing"):
                self.angle = 0
                self.previousAngle = 0
