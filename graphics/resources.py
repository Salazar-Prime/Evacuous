import pyglet
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

car_image = pyglet.resource.image('car.png')
car_image.height = 20
car_image.width = 20
center_image(car_image)
