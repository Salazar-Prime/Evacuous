from util.objects import Car, Junction, Road
import random
from util.functions import *
from graphics.draw_frame import on_road

# total_cars = 50;

def global_assignment(params):   # Pass the object of class ParameterSet to this function
	global separation, exit_communication_radius, communication_radius, scale_rule1
	separation= params.separation
	exit_communication_radius = params.exit_communication_radius
	communication_radius = params.communication_radius
	scale_rule1 = params.scale_rule1


def new_position(cars):
    # update the position of the car with the current
    total_cars = len(cars)
    '''Add to car object "moving towards node" '''
    for i in range(total_cars):
        speed = dot(velocity, road)  # component of velocity in direction of road
        if sub((cars.next_node.x, cars.next_node.y), (cars[i].x, cars[i].y)) > speed:  # distanceToNode > speed
            cars[i].x, cars[i].y = cars[i].x + speed, cars[i].y + speed
        else:
            p = projection((cars[i].next_node.x, cars[i].next_node.y), cars[i].cur_road.vector)  '''# !!!!!!!!!!!!!correct this'''
            cars[i].x, cars[i].y = cars[i].x + p, cars[i].y + p


def handle_collision(cars):
    # remove collisions between cars
    num_collide = 0
    total_cars = len(cars)
    while num_collide != 0:
        num_collide = 0
        collide_pair = []  # stores tuple of colliding cars

        # find colliding cars
        for i in range(total_cars):
            for j in range(i + 1, total_cars):
                if dist(i, j) < separation:
                    # separation is allowed separation specified by UI sliders
                    collide_pair.append((cars[i], cars[j]))
                    num_collide += 1

        # remove collisions
        for i in range(len(collide_pair)):
            car_reference = collide_pair[i][0]
            car_to_move = collide_pair[i][1]

            # moving the second car by distance = separation
            car_on_road = False
            while not (car_on_road):
                # find random position for placing the car
                x = random.uniform(car_reference.x - separation, car_reference.x + separation)
                y = calc_y_on_circle(car_reference.x, car_reference.y, x)
                car_on_road = on_road(x, y, car_on_road.cur_road.road_id)  # function provided by aravind

            # updating the velocity for 'car_to_move'
            car_to_move.vx = car_to_move.vx + (x - car_to_move.x)
            car_to_move.vy = car_to_move.vy + (y - car_to_move.y)

            # updating the position of car
            car_to_move.x = x
            car_to_move.y = y


def update_velocity(cars):
    # update the velocity vector of each car for next frame
    total_cars = len(cars)
    for i in range(total_cars):
        car1 = cars[i]  # first car
        velo_add_rule1 = [0, 0]

        # if cars sees the exit then move the car towards exit with high speed
        if car1.next_node.is_exit:
            if dist((car1.x, car1.y), (car1.next_node.x, car1.next_node.y)) < exit_communication_radius:
                car1.vx, car1.vy = sub((car1.next_node.x, car1.next_node.y), (car1.x, car1.y))
                continue
        for j in range(total_cars):
            car2 = cars[j]
            if i == j:
                continue

            # Rule1: Alignment - Other cars influence the velocity of the car in consideration
            distance = dist((car1.x, car1.y), (car2.x, car2.y))
            if distance < communication_radius:
                velo_add_rule1[0] += car2.vx
                velo_add_rule1[1] += car2.vy

            # updating velocity
            car1.vx, car1.vy = add((car1.vx, car1.vy), scale(scale_rule1, velo_add_rule1))
