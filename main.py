from util.objects import *
from util import load
from graphics.draw_frame import *
import pyglet
from movement import next_state, global_assignment

simple_junctions = [Junction(100, 0, junction_id=0, is_exit=True),
                    Junction(130, 310, junction_id=1),
                    Junction(0, 500, junction_id=2, is_exit=True),
                    Junction(500, 490, junction_id=3),
                    Junction(800, 300, junction_id=4, is_exit=True),
                    Junction(300, 390, junction_id=5),
                    Junction(378, 0, junction_id=6, is_exit=True),
                    Junction(278, 500, junction_id=7),
                    Junction(330, 240, junction_id=8),
                    Junction(110, 100, junction_id=9)]
# def add_junction(i,j): # adds a node between 2 existing nodes


road_conn = [(0, 9), (9, 1), (1, 2), (1, 5), (9, 8), (5, 8), (7, 5), (8, 6), (5, 3), (3, 4)]
simple_roads = []
for start, end in road_conn:
    cur_road = Road(simple_junctions[start], simple_junctions[end])
    #print cur_road.length
    simple_roads.append(cur_road)
    simple_junctions[start].add_road(cur_road)
    simple_junctions[end].add_road(cur_road)

curmap = Map(simple_junctions, simple_roads)
carsbatch = pyglet.graphics.Batch()
cars = load.init_random_cars(curmap, 10, carsbatch)

# initialize a parameter set
params = ParameterSet(separation=5, communication_radius=50, scale_rule1=0.25, exit_communication_radius=0.1)
global_assignment(params)

"""Setting up GUI"""

# creating window
WINWIDTH, WINHEIGHT = 800, 600
game_window = pyglet.window.Window(WINWIDTH, WINHEIGHT)

# Drawing the labels
@game_window.event  # lets the Window instance know that on_draw() is an event handler
def on_draw():
    #print "on_draw"
    draw_map(curmap,game_window)
    draw_cars(carsbatch)
    next_state(cars)
    for car in cars:
        #print car.car_id,car.vx,car.vy
        pass

def update(dt):
    draw_map(curmap,game_window)
    draw_cars(carsbatch)
    next_state(cars)

#pyglet.clock.schedule_interval(update, 1/60.0)

if __name__ == "__main__":
    pyglet.app.run()

