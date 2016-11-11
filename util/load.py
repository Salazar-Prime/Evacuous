from util.objects import Car
from util.functions import *

import random

def init_random_cars(curmap, num_cars=10, batch=None, maxcarvel=5.0, seed=None):
    carobjs = []
    roads = list(curmap.roads)
    if seed:
        random.seed(seed)
        print random.random()
    for i in range(num_cars):
        r = random.choice(roads)
        dist = random.random()
        pos_on_road = weight_add(r.start_junction.location, r.end_junction.location, dist, 1-dist)
        transverse_pos = (random.random()-1)*(r.width-Car.size)/2
        final_pos = add(pos_on_road, scale( perp(r.vector), transverse_pos ))
        velx, vely = random.random()*maxcarvel, random.random()*maxcarvel
        newcar = Car(*final_pos, vx=velx, vy=vely, car_id=i, road=r, batch=batch)
        carobjs.append(newcar)
    return carobjs