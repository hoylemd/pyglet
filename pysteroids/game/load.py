import pyglet
import random
import resources
import utils


def asteroids(num_asteroids, player_position):
    asteroids = []

    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position

        while utils.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)

        new_asteroid = pyglet.sprite.Sprite(
            img=resources.asteroid_image, x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)

        asteroids.append(new_asteroid)

    return asteroids
