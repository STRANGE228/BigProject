import sys
import pygame as pg
from const import *
from class_map import Map
from class_input import InputStr

pg.init()
level0_sprites = pg.sprite.Group()
level1_sprites = pg.sprite.Group()
level2_sprites = pg.sprite.Group()

# Добавляем классы
main_map = Map(level0_sprites)
input1 = InputStr(10, 10, 100, 20, level1_sprites)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
FPS = 25

work = True
while work:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            work = False

    level0_sprites.update(events)
    level1_sprites.update(events)
    level2_sprites.update(events)

    screen.fill('black')
    level0_sprites.draw(screen)
    level1_sprites.draw(screen)
    level2_sprites.draw(screen)

    if input1.text_out:
        main_map.fstring = input1.text_out
        main_map.need_search = True
        main_map.remake = True
        input1.text_out = ''

    pg.display.flip()
    clock.tick(FPS)

sys.exit(pg.quit())
