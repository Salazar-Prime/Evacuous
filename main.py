from util.objects import *
from util import load
from graphics.draw_frame import *
import pyglet
from movement import next_state, global_assignment
from time import time

import sys

simple_junctions = [Junction(100, 0, junction_id=0, is_exit=True),
                    Junction(130, 310, junction_id=1),
                    Junction(0, 500, junction_id=2, is_exit=True),
                    Junction(500, 490, junction_id=3),
                    Junction(800, 300, junction_id=4),
                    Junction(300, 390, junction_id=5),
                    Junction(378, 0, junction_id=6, is_exit=True),
                    Junction(278, 500, junction_id=7),
                    Junction(330, 100, junction_id=8),
                    Junction(110, 100, junction_id=9),
                    Junction(0, 150, junction_id=10, is_exit=True),
                   	Junction(200, 700, junction_id=11, is_exit=True),
                   	Junction(1000, 300, junction_id=12),
                   	Junction(1300, 300, junction_id=13, is_exit=True),
                   	Junction(800, 100, junction_id=14),
                   	Junction(1000, 100, junction_id=15),
                   	Junction(1000, 700, junction_id=16, is_exit=True),
                   	Junction(500, 700, junction_id=17, is_exit=True),
                   	Junction(500, 600, junction_id=18),
                   	Junction(700, 600, junction_id=19),
                   	Junction(900, 500, junction_id=20),
                   	Junction(900, 300, junction_id=21)
                   	]
# def add_junction(i,j): # adds a node between 2 existing nodes


# road_conn = [(0, 9), (9, 1), (1, 2), (1, 5), (9, 8), (5, 8), (7, 5), (8, 6), (5, 3), (3, 4)]
road_conn = [(0, 9), (9, 1), (1, 2), (1, 5), (9, 8), (5, 8), (7, 5), (8, 6), (5, 3), (3, 4), (9,10), (7,11), (4,21), (21,12), (12,13), (4,14), (14,8) , (12,15), (14,15),(12,16), (3, 18), (18,17), (18,19), (19,20), (20,21)]
simple_roads = []
roadsbatch = pyglet.graphics.Batch()
for start, end in road_conn:
    cur_road = Road(simple_junctions[start], simple_junctions[end], batch=roadsbatch)
    #print cur_road.length
    simple_roads.append(cur_road)
    simple_junctions[start].add_road(cur_road)
    simple_junctions[end].add_road(cur_road)

"""Setting up GUI"""

GRAPHICS = False
number_of_cars = 1000

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            number_of_cars = int(sys.argv[1])
        if "-g" in sys.argv:
            GRAPHICS = True


curmap = Map(simple_junctions, simple_roads)
carsbatch = pyglet.graphics.Batch()
cars = load.init_random_cars(curmap, number_of_cars, carsbatch, seed=123)

# initialize a parameter set
params = ParameterSet(separation=5, communication_radius=10, scale_rule1=0.01, exit_communication_radius=10)
global_assignment(params)


# creating window
if GRAPHICS:
    WINWIDTH, WINHEIGHT = 1300, 700
    game_window = pyglet.window.Window(WINWIDTH, WINHEIGHT)

# Drawing the labels
#@game_window.event  # lets the Window instance know that on_draw() is an event handler
def on_draw():
    #print "on_draw"
    draw_map(curmap,game_window)
    draw_cars(carsbatch)
    if not cars:
        print "exiting"
        pyglet.app.exit()
    next_state(cars)
    roadsbatch.draw()
    for car in cars:
        pass
        #print car.car_id,car.vx,car.vy

def update(dt):    
    if not GRAPHICS:
        print "Cars left to exit:" + str(len(cars))
    global frame_counter
    frame_counter += 1
    if GRAPHICS:
        draw_map(curmap,game_window)
        draw_cars(carsbatch)
    if not cars:
        print "exiting"
        pyglet.app.exit()
    next_state(cars)


pyglet.clock.schedule_interval(update, 1/1000.0)
frame_counter = 0
t = time()
if __name__ == "__main__":
    pyglet.app.run()
print "time taken", time()-t
print "frames taken", frame_counter
