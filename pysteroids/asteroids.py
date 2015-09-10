import pyglet
from game import resources, load
from settings import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TOPBAR_VERTICAL_OFFSET,
    WINDOW_HORIZONTAL_CENTER, WINDOW_VERTICAL_CENTER)


game_window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(
    text="Score: 0", x=10, y=TOPBAR_VERTICAL_OFFSET, batch=main_batch)
level_label = pyglet.text.Label(
    text="Pysteroids", x=WINDOW_HORIZONTAL_CENTER, y=TOPBAR_VERTICAL_OFFSET,
    anchor_x='center', batch=main_batch)

player_ship = pyglet.sprite.Sprite(
    img=resources.player_image, x=WINDOW_HORIZONTAL_CENTER,
    y=WINDOW_VERTICAL_CENTER, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)

lives = load.player_lives(3, main_batch)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':
    pyglet.app.run()
