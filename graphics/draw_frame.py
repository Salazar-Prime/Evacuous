from util.objects import Map, Junction, Road
from util.functions import *
import random, math
import pyglet


def draw_map(curmap,game_window):  # lets to redraw the window
    game_window.clear()
    for i in curmap.roads:
        draw_road(i)
    for j in curmap.junctions:
        draw_intersection(j)


def draw_road(a):
    x1, y1 = a.start_junction.location
    x2, y2 = a.end_junction.location
    z1, z2 = perp(a.vector)
    rect_vertices = (x1 + z1 * (a.width / 2), y1 + z2 * (a.width / 2), x2 + z1 * (a.width / 2), y2 + z2 * (a.width / 2),
                     x1 - z1 * (a.width / 2), y1 - z2 * (a.width / 2), x2 - z1 * (a.width / 2), y2 - z2 * (a.width / 2))
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS, [0, 1, 3, 2], ('v2f', rect_vertices))


def draw_intersection(a):
    num_points = 1000  # nodes of circle
    vertices = ()
    b = list(a.incident_roads)[0]
    for i in range(num_points):
        angle = math.radians(float(i) / num_points * 360.0)
        x = b.width / 2 * math.cos(angle) + a.location[0]
        y = b.width / 2 * math.sin(angle) + a.location[1]
        vertices += (x, y)
    pyglet.graphics.draw(num_points, pyglet.gl.GL_POLYGON, ('v2f', vertices))


def draw_cars(batch):
    batch.draw()


def on_road(x, y, road):
    pt = (x, y)
    z1, z2 = perp(road.vector)
    start_r = (x1, y1) = road.start_junction.location
    end_r = (x2, y2) = road.end_junction.location
    pt_rel = (pt[0] - x1, pt[1] - y1)

    unit_len = (road.vector[0] / magnitude(road.vector), road.vector[1] / magnitude(road.vector))
    vec_pll = (dot(pt_rel, unit_len) * unit_len[0], dot(pt, unit_len) * unit_len[1])
    vec_perp = ((pt_rel[0] - vec_pll[0]), (pt_rel[1] - vec_pll[1]))
    # condt = (a.width*z1/2, a.width*z2/2)
    # return 0

    print magnitude(vec_pll), magnitude(road.vector), magnitude(vec_perp), (road.width / 2) * magnitude((z1, z2))
    if (magnitude(vec_pll) <= magnitude(road.vector) and magnitude(vec_perp) <= (road.width / 2) * magnitude((z1, z2))):
        return True
    else:
        return False


# Checkinf if on_road works!
"""a = True

for i in range(100,300):
	b = 100+random.randint(-25,25)
	print b
	a = a and (on_road(i, b,Road(Junction(99,100,junction_id=0),
                    Junction(300,100,junction_id=1)))	)
print a	
"""

