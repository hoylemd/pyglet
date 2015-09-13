import pyglet
pyglet.resource.path = ['../../resources']
pyglet.resource.reindex()


def center_image(image):
    """Sets an image's anchor point to it's center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

player_image = pyglet.resource.image('player.png')
center_image(player_image)

fixtures = {
    'player_image': player_image
}
