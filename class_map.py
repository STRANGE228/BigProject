import pygame as pg
from io import BytesIO

import requests
from PIL import Image

from const import *


def image_conv(bstring):
    image = Image.open(BytesIO(bstring))
    size = image.size
    typ = image.mode
    data = image.tobytes()
    pg_image = pg.image.fromstring(data, size, typ)
    return pg_image


class Map(pg.sprite.Sprite):
    """

    """
    def __init__(self, *group):
        super(Map, self).__init__(*group)
        self.remake = True
        self.image = None
        self.rect = None
        self.pos = [0, 0]
        self.pos_step = 0.001
        self.zoom = 14
        self.mode = "sat"
        self.fstring = 'Белая Холуница'

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_PAGEUP:
                    self.zoom = max(self.zoom - 1, 1)
                    self.remake = True
                elif event.key == pg.K_PAGEDOWN:
                    self.zoom = min(self.zoom + 1, 19)
                    self.remake = True
        if self.remake:
            self.search()
            self.get_map()
            self.remake = False

    def change_pos(self, bstring):
        self.image = image_conv(bstring)
        self.rect = self.image.get_rect()

    def get_map(self):
        api_map = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": f'{self.pos[0]},{self.pos[1]}',
            # "spn": f'{self.spn},{self.spn}',
            "z": self.zoom,
            "l": self.mode
        }
        request = requests.get(api_map, params=params)
        if request.status_code == 200:
            self.change_pos(request.content)
        else:
            print(request.status_code)

    def search(self):
        api_map = "http://geocode-maps.yandex.ru/1.x/"
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": self.fstring,
            "format": "json"
        }
        request = requests.get(api_map, params=params)
        if request.status_code == 200:
            result = request.json()
            self.pos = list(map(float, result["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]["Point"]["pos"].split()))
        else:
            print(request.status_code)
