import sys
from const import *
from class_map import Map
from class_input import InputStr
from class_button import *
from class_output import *

pg.init()
level0_sprites = pg.sprite.Group()
level1_sprites = pg.sprite.Group()
level2_sprites = pg.sprite.Group()

names = {' схема   ': 'map',
         'спутник': 'sat',
         'гибрид ': 'sat,skl'}

main_map = Map(level0_sprites)
input1 = InputStr(10, 10, 100, 20, level1_sprites)
type_map = ButtonMap(10, (HEIGHT - 50), 100, 50, level1_sprites)
search_map = ButtonSearch((WIDTH - 110), (HEIGHT - 50), 100, 50, level1_sprites)
clear_map = ButtonClear((WIDTH - 300), (HEIGHT - 50), 100, 50, level1_sprites)
output1 = OutputStr(10, 25, 100, 20, level1_sprites)
index = ButtonIndex((WIDTH - 300), (HEIGHT - 100), 100, 50, level1_sprites)
output2 = OutputStr(10, 45, 100, 20, level1_sprites)

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

    if clear_map.clear:
        main_map.pts = []
        clear_map.clear = False
        main_map.remake = True
        main_map.address = ""
        main_map.index = ""
        output1.print_out(main_map.address)
        output2.print_out(main_map.index)

    if search_map.remake:
        search_map.remake = False
        input1.text_out = input1.text
        input1.text = ""

    if input1.text_out:
        main_map.fstring = input1.text_out
        main_map.need_search = True
        main_map.remake = True
        input1.text_out = ''

    if output1.out:
        output1.print_out(main_map.address)
        output1.text = ""
        if index.index:
            output2.print_out(main_map.index)
        else:
            output2.print_out("")

    if type_map.remake:
        main_map.mode = names[type_map.text]
        type_map.remake = False
        main_map.remake = True

    pg.display.flip()
    clock.tick(FPS)

sys.exit(pg.quit())
