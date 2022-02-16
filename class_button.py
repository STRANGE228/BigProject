import pygame as pg


class ButtonMap(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, *groups):
        super(ButtonMap, self).__init__(*groups)
        self.image = None
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.font = pg.font.Font(None, 50)
        self.remake = False
        self.texts = [' схема   ',
                      'спутник',
                      'гибрид ']
        self.text = 'спутник'
        self.n = 2

    def change_text(self):
        self.text = self.texts[self.n]
        self.n = (self.n + 1) % 3

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.change_text()
                    self.remake = True

        self.image = self.font.render(self.text, True, 'white', 'black')
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class ButtonSearch(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, *groups):
        super(ButtonSearch, self).__init__(*groups)
        self.font = pg.font.Font(None, 50)
        self.image = self.font.render("Найти", True, 'white', 'black')
        self.rect = pg.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.remake = False

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.remake = True

