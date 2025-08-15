import pygame

class Bullet:
    def __init__(self, speed: float, type: str, hitBox: pygame.Rect):
        self.speed = speed
        self.type = type
        self.hitBox = hitBox
