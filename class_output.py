import pygame as pg


class OutputStr(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, *groups):
        super(OutputStr, self).__init__(*groups)
        self.rect = pg.Rect(x, y, w, h)
        self.text = ""
        self.font = pg.font.Font(None, 32)
        self.image = self.font.render(self.text, True, 'white')
        self.out = True

    def print_out(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, 'white')


class OutputIndex(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, *groups):
        super(OutputIndex, self).__init__(*groups)
        self.rect = pg.Rect(x, y, w, h)
        self.text = ""
        self.font = pg.font.Font(None, 32)
        self.image = self.font.render(self.text, True, 'white')

    def print_out(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, 'white')
