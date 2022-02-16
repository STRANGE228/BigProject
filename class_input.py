import pygame as pg


class InputStr(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, *groups):
        super(InputStr, self).__init__(*groups)
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.image = None
        self.text = ""
        self.font = pg.font.Font(None, 50)
        self.text_out = self.text

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.text_out = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        self.image = self.font.render(f"Найти: {self.text} {' ' * (58 - len(self.text))}", True, 'white', (230, 0, 230))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

