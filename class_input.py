import pygame as pg


class InputStr(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, *groups):
        super(InputStr, self).__init__(*groups)
        self.rect = pg.Rect(x, y, w, h)
        self.image = None
        self.text = ""
        self.font = pg.font.Font(None, 32)
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

        self.image = self.font.render(self.text, True, 'white')
        self.rect = self.image.get_rect()


