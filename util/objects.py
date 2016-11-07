# TODO: Decide if you want the objects to store other relevant objects as ID's or references
import functions, pyglet
from graphics import resources

class Junction(object):
    """junction object, every junction has a unique ID which can be autoassigned.
    Stores location of junction and the incident roads."""

    # auto incrementing ID as a class variable
    auto_id = 0

    def __init__(self, x, y, is_exit=False, junction_id=None, *args, **kwargs):
        if junction_id :
            self.junction_id = Junction.auto_id
            Junction.auto_id += 1
        self.location = self.x, self.y = (x, y)
        self.incident_roads = set()
        self.is_exit = is_exit

    def add_road(self, road):
        self.incident_roads.add(road)


class Road(object):
    """Road object, every road has a unique ID which can be autoassigned.
    Stores nodes between which the road lies and th width of the road."""

    # auto incrementing ID as a class variable
    auto_id = 0
    default_width = 30.0

    def __init__(self, start_junction, end_junction, width=None, road_id=None, *args, **kwargs):
        if not road_id:
            self.road_id = Road.auto_id
            Road.auto_id += 1
        self.start_junction, self.end_junction = start_junction, end_junction
        self.width = width if width else Road.default_width
        (startx, starty), (endx, endy) = start_junction.location, end_junction.location
        self.vector = (endx - startx, endy - starty)
        self.length = functions.magnitude(self.vector)
        #self.slope = functions.slope(start_junction.location, end_junction.location)


class Map(object):
    """Map object, stores all the roads and junctions in a map."""

    def __init__(self, junctions, roads, *args, **kwargs):
        self.roads = set()
        self.junctions = set()
        for road in roads:
            self.add_road(road)
        for junction in junctions:
            self.add_junction(junction)

    def add_road(self, road):
        self.roads.add(road)

    def add_junction(self, junction):
        self.junctions.add(junction)


class Car(pyglet.sprite.Sprite):
    """Car object, stores cars location and velocity"""

    size = resources.car_image.width

    def __init__(self, x, y, vx, vy, car_id, road, *args, **kwargs):
        super(Car, self).__init__(x=x, y=y, img=resources.car_image, *args, **kwargs)
        self.velocity = self.vx, self.vy = vx, vy
        self.car_id = car_id

    def update_road(self, road):
        self.cur_road = road
        if functions.dot( (self.vx, self.vy), road.vector ) > 0:
            self.next_junction = road.end_junction
        else:
            self.next_junction = road.start_junction

        self.update_road(road)

    def add_velocity(self, v):
        vx, vy = v
        self.velocity = self.vx, self.vy = self.vx + vx, self.vy + vy


class ParameterSet(dict):
    def __init__(self,**kw):
        dict.__init__(self,kw)
        self.__dict__ = self