import pygame as pg


class TextAddress(pg.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super(TextAddress, self).__init__(*groups)
        self.font = pg.font.Font(None, 35)
        self.image = self.font.render("", True, 'white', 'grey')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.text = None

    def change_text(self, text):
        self.image = self.font.render(text, True, 'white')
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
