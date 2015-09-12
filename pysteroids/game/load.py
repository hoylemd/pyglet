import pyglet
import random
import resources
import utils
from physicalobject import PhysicalObject
from settings import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    LIVES_VERTICAL_OFFSET, LIVES_HORIZONTAL_OFFSET,
    WINDOW_HORIZONTAL_CENTER, WINDOW_VERTICAL_CENTER)


def asteroids(num_asteroids, player_position, batch=None):
    asteroids = []

    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position

        while utils.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, WINDOW_WIDTH)
            asteroid_y = random.randint(0, WINDOW_HEIGHT)

        new_asteroid = PhysicalObject(
            img=resources.asteroid_image, x=asteroid_x, y=asteroid_y,
            batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40

        asteroids.append(new_asteroid)

    return asteroids


def player_ship(batch=None):
    return PhysicalObject(
        img=resources.player_image, x=WINDOW_HORIZONTAL_CENTER,
        y=WINDOW_VERTICAL_CENTER, batch=batch)


def player_lives(num_icons, batch=None):
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(
            img=resources.player_image, x=(LIVES_HORIZONTAL_OFFSET - i * 30),
            y=LIVES_VERTICAL_OFFSET, batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives
