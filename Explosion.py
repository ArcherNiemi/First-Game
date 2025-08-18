import pygame

class Explosion:
    def __init__(self, startTime: float, hasHit: bool, hitBox: pygame.Rect):
        self.startTime = startTime
        self.hasHit = hasHit
        self.hitBox = hitBox