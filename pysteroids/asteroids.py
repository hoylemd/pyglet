import pyglet
game_window = pyglet.window.Window(800, 600)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(
    text="Pysteroids", x=400, y=575, anchor_x='center')


@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()

if __name__ == '__main__':
    pyglet.app.run()
