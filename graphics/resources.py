import pyglet
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

car_image = pyglet.resource.image('car.png')
center_image(car_image)
