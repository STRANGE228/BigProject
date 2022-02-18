import pygame as pg
from io import BytesIO
import requests
from PIL import Image


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
        self.need_search = True
        self.image = None
        self.rect = None
        self.pos = [0, 0]
        self.pos_step = 0.016 * 2.5
        self.spn = 0.016
        # self.zoom = 14
        self.mode = "sat"
        self.pts = []
        self.fstring = 'Белая Холуница'
        self.address = ""

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_PAGEUP:
                    self.spn = max(self.spn * 2, 0.0005)
                    # self.zoom = max(self.zoom - 1, 1)
                    self.remake = True
                    self.pos_step = self.spn * 2.5
                elif event.key == pg.K_PAGEDOWN:
                    self.spn = min(self.spn / 2, 65.536)
                    # self.zoom = min(self.zoom + 1, 19)
                    self.remake = True
                    self.pos_step = self.spn * 2.5
                elif event.key == pg.K_UP:
                    self.pos[1] = min(self.pos[1] + self.pos_step, 85)
                    self.remake = True
                elif event.key == pg.K_DOWN:
                    self.pos[1] = max(self.pos[1] - self.pos_step, -85)
                    self.remake = True
                elif event.key == pg.K_LEFT:
                    self.pos[0] = max(self.pos[0] - self.pos_step, -179)
                    self.remake = True
                elif event.key == pg.K_RIGHT:
                    self.pos[0] = min(self.pos[0] + self.pos_step, 179)
                    self.remake = True
        if self.remake:
            if self.need_search:
                self.search()
                self.need_search = False
            self.get_map()
            self.remake = False

    def change_pos(self, bstring):
        self.image = image_conv(bstring)
        self.rect = self.image.get_rect()

    def get_map(self):
        api_map = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": f'{self.pos[0]},{self.pos[1]}',
            "spn": f'{self.spn},{self.spn}',
            # "z": self.zoom,
            "l": self.mode,
            "size": "650,450",
            "pt": "~".join([f'{elem[0]},{elem[1]},pm2ywl' for elem in self.pts])
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
            self.address = result['response']['GeoObjectCollection'][
                'featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
            if not self.pts:
                self.pts.append(self.pos.copy)
        else:
            print(request.status_code)

    def get_address(self):
        return self.address
