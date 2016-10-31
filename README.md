# Evacuous
For midsem submission

Authors: Varun Aggarwal, Arvind Roshan, PR Vaidyanathan

This is a simulation based project aimed at implementing both serial and parallel versions of the evacuation simulation that we have developed. Goal is to significantly reduce the run time of simulation by parallelization.

Scenario: 

There are a large number of smart cars in a city. Due to some emergency, all the cars are asked to evacuate the city as fast as possible.
To facilitate evacuation, some number of exit/evacuation points exist (generally on the outskirts), but the information about the 
geographical location of an exit point is only available to the cars which are in the vicinity of one the concerned exit point, 
in other words each exit has to be discovered. Each car has the ability to communicate with other cars in its vicinity. 
The "swarm" of cars has to work collectively to find exits and make use of them to evacuate the city. 

Solution approach:

Each car of the swarm, has it's own thinking and decides which direction to proceed in, based on certain rules and 
parameters - some of which depend on the behavior of the local swarm, and some depend on global goals. 

Description of important files and folder:

root folder :

●	main.py: This .py file draws a map network by calling map.py, updates car parameter by calling movement.py and draws the updated car position till all cars exit the window.

●	movement.py: updates the position and velocity of the car for the next frame. Various rules of boids are implemented here

./graphics: contains files for drawing the frame on screen

●	 resources.py which loads resources like car image from resources directory and map.py.

●	map.py: It contains a function- on_road, which given a point in map and road object will return True if the point is on the given road or else false. It also contains functions which draw roads, intersection.

./resources: Contains image of car.

./util: contains utility code accessible by all the other classes

●	functions.py: Contains basics funtions which are often used in other .py files like, slope of a vector, unit perperndicular to a vector, magnitude of a vector, dot produt between vectors, add; subtract; weighted add of two vectors, scale a vector and projection of one vector on an other.

●	objects.py: creates Map, Road, Junction, Car classes. 

●	load.py: contains a function which randomly initialize cars at the begining.
 
