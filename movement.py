from util.objects import Car, Junction, Road
import random
from util.functions import *
from graphics.draw_frame import on_road

# total_cars = 50;
separation, exit_communication_radius, communication_radius, scale_rule1 = 0, 0, 0, 0


def global_assignment(params):
    # Pass the object of class ParameterSet to this function
    global separation, exit_communication_radius, communication_radius, scale_rule1
    separation = params.separation
    exit_communication_radius = params.exit_communication_radius
    communication_radius = params.communication_radius
    scale_rule1 = params.scale_rule1


def next_state(cars):
    #print "next_state"
    new_position(cars)
    # disabling handle collision for now
    #handle_collision(cars)
    update_velocity(cars)
    #print "frame over"

def new_position(cars):
    # update the position of the car with the current
    #print "next_position"
    total_cars = len(cars)
    i = 0
    while i < len(cars): # while loop since we are modifying cars
        if cars[i].cur_node: # car is at intersection, has to decide which way to go
            max_allign = 0
            allign_road = None
            for choice_road in cars[i].cur_node.incident_roads:
                if choice_road.start_junction == cars[i].cur_node:
                    modifier = 1
                else:
                    modifier = -1
                p = modifier * projection((cars[i].vx, cars[i].vy), choice_road.vector)
                if p > max_allign:
                    max_allign = p
                    allign_road = choice_road
            print "{}{} changed roads from {} to {}".format(cars[i].car_id, cars[i].position,
                                                            cars[i].cur_road.road_id, allign_road.road_id)
            cars[i].update_road(allign_road)
            cars[i].cur_node = None
            # if allign_road.start_junction == cars[i].cur_node:
            #     cars[i].next_junction = allign_road.end_junction
            # else:
            #     cars[i].next_junction = allign_road.start_junction

        next_j = cars[i].next_junction
        speed = projection((cars[i].vx, cars[i].vy), cars[i].cur_road.vector)  # velocity component in direction of road
        if next_j == cars[i].cur_road.end_junction:
            speed = scale(speed, -1)
        distance_to_node = sub((next_j.x, next_j.y), (cars[i].x, cars[i].y))

        if magnitude(distance_to_node) > magnitude(speed):  # distanceToNode > speed
            cars[i].x, cars[i].y = cars[i].x + speed[0], cars[i].y + speed[1]
            i += 1
        else:
            if cars[i].next_junction.is_exit: # car has reached exit
                print "exit", i, cars[i].car_id, cars[i].position
                print [c.car_id for c in cars]
                cars[i].delete()  # delete car object and remove it from batch
                cars = cars[:i] + cars[i+1:]  # remove car from cars
                print [c.car_id for c in cars]
            else: # car is near junction so move it to junction
                #p = projection(distance_to_node, cars[i].cur_road.vector)
                #cars[i].x, cars[i].y = cars[i].x + p[0], cars[i].y + p[1]
                # place car at junction
                print "proceed"
                cars[i].x , cars[i].y = next_j.x, next_j.y
                cars[i].cur_node = next_j
                #cars[i].cur_road = None # clear cur_road, don't know which road to go
                i += 1


def handle_collision(cars):
    # remove collisions between cars
    #print "handle_collision"
    num_collide = 1
    total_cars = len(cars)
    while num_collide != 0:
        num_collide = 0
        collide_pair = []  # stores tuple of colliding cars

        # find colliding cars
        for i in range(total_cars):
            for j in range(i + 1, total_cars):
                if dist(cars[i].position, cars[j].position) < separation:
                    # separation is allowed separation specified by UI sliders
                    print "collision"
                    collide_pair.append((cars[i], cars[j]))
                    num_collide += 1

        # remove collisions
        print len(collide_pair)
        for i in range(len(collide_pair)):
            car_reference = collide_pair[i][0]
            car_to_move = collide_pair[i][1]

            # moving the second car by distance = separation
            #car_on_road = False
            x, y = 0, 0
            print "now handle"
            while True:
                # find random position for placing the car
                x = random.uniform(car_reference.x - separation, car_reference.x + separation)
                y1,y2 = calc_y_on_circle(car_reference.x, car_reference.y, x, separation)
                car_on_road_1 = on_road(x, y1, car_to_move.cur_road)  # function provided by aravind
                car_on_road_2 = on_road(x, y2, car_to_move.cur_road)
                print x, y1, y2, car_to_move.cur_road.start_junction.location, car_to_move.cur_road.end_junction.location
                #break
                if car_on_road_1:
                    y =y1
                    break
                if car_on_road_2:
                    y=y2
                    break
                #car_on_road = car_on_road_1  car_on_road_2
            print "handled"
            # updating the velocity for 'car_to_move'
            car_to_move.vx = car_to_move.vx + (x - car_to_move.x)
            car_to_move.vy = car_to_move.vy + (y - car_to_move.y)

            # updating the position of car
            car_to_move.x = x
            car_to_move.y = y


def update_velocity(cars):
    # update the velocity vector of each car for next frame
    #print "update_velocity"
    total_cars = len(cars)
    for i in range(total_cars):
        car1 = cars[i]  # first car
        velo_add_rule1 = [0, 0]

        # if cars sees the exit then move the car towards exit with high speed
        if car1.next_junction.is_exit:
            if dist((car1.x, car1.y), (car1.next_junction.x, car1.next_junction.y)) < exit_communication_radius:
                car1.vx, car1.vy = sub((car1.next_junction.x, car1.next_junction.y), (car1.x, car1.y))
                continue
        # checking only for different cars
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
            car1.vx, car1.vy = add((car1.vx, car1.vy), scale(velo_add_rule1, scale_rule1))
