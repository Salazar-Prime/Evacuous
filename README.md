# Evacuous

Note: The parallel implementation of [Project Evacuous](https://github.com/Salazar-Prime/Evacuous-parallel/) using PyCUDA

## Authors
* [Varun Aggarwal](https://github.com/Salazar-Prime/)
* [Arvind Roshaan](https://github.com/Arvind-Roshaan-S)
* [P.R.Vaidyanathan](https://github.com/aditya95sriram)

## Dependencies

* [CUDA v7.5](https://developer.nvidia.com/cuda-75-downloads-archive)
* [PyCUDA v2016.1.2](https://wiki.tiker.net/PyCuda/Installation)
* [Pyglet v1.2.4](http://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/programming_guide/installation.html)

## How to run

From the project root execute `python main.py [<number_of_cars>] [-g]` with the optional `-g` switch to run the simulation with graphics enabled and `<number_of_cars>` indicating the number of cars to run the simulation with (defaults to 1000 cars).

Example: `python main.py 1000 -g`

## Description

This is a simulation based project aimed at parallelizing the simulation(with graphics) of an evacuation situtation of smart cars. The main goal was to significantly reduce the run time of simulation using PyCUDA. This project was developed as a part of the course **ES611: Algorithms for Advanced Computer Architecture** conducted by Dr. Ravi Hegde at Indian Institute of Technology Gandhinagar.

## Scenario

There are a large number of smart cars in a city. Due to some emergency, all the cars are asked to evacuate the city as fast as possible.
To facilitate evacuation, some number of exit/evacuation points exist (generally on the outskirts), but the information about the
geographical location of an exit point is only available to the cars which are in the vicinity of one of the concerned exit point.
In other words, each exit has to be *discovered*. Each car has the ability to communicate with other cars in its vicinity.
There is not central coordinating body and each car has to make its own decisions based on the cars in its neighbourhood.
The *swarm* of cars has to work collectively to find exits and evacuate the city.

## Solution approach

The solution is inspired by the [Boids problem](http://www.red3d.com/cwr/boids/) by Craig Reynolds.
Each car of the swarm, has it's own thinking and decides which direction to proceed in, based on certain rules and
parameters - some of which depend on the behavior of the local swarm, and some depend on global goals.
These rules are aggregated to compute the new velocity of the car in question.

## Future Work

* Incorporate Collision Detection
* Allow directly importing map from Google Maps, and internally constructing the network