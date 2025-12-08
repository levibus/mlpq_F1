# IndyCar Race Implemented in MLPQ
Levi Busching, Joseph Holy, Aaron Perkey<br>
Presentation Video: https://youtu.be/jtV48J4WkHQ

![still image of track](track.png)

This project simulates an IndyCar race in the database system MLPQ for our CSCE413/813 Database Systems final project. To do this, we created a constraint database that models moving objects. 

## How to run:
1. download MLPQ with the provided executable file
2. load the database from the '413 Track.txt' file
    - you may have to zoom in a little
3. run the time simulation
4. to change the cars in the simulation, run the car.py file and copy the output from output.txt into '413 Track.txt' in place of the current car data. The functionality of car.py is further explained below.

## Parts of the demonstration:
#### 413 Track.txt

This file contains all the tables required in the simulation. Every table apart from the car and tire tables is a static part of the course. These objects have time steps built into them so if you change the colors in MLPQ they will change over time. We used this in our simulation to show the track colors going from afternoon sunlight to dusk. The car and tire data are generated from the car.py file.

#### 413 Driver_Team_Stats.txt

We wanted the cars / drivers in our MLPQ database simulation to have accurate-to-life speed and consistency, so we created a small dataset featuring overall 2025 Indycar season statistics and Indy 500 race-specific statistics. We then applied min-max normalization to these values, and summed them to give each driver an “Indy 500 score”. In our simulation, the better the “Indy 500 score”, the more likely the driver was to be fast and consistent, and vice versa. This is the type of work racing game devs would do to create realistic simulations of races / realistic alternate outcomes. We use this to rank the drivers based on how good they are so we can assign higher or lower talent values in car.py.

#### car.py

This file generates the paths of all cars and their associated tires. First, it randomly selects tires for the car that are hard, medium, or soft. Each tire also has a condition component that starts at good at the beginning of the race. Hard tires transition from a condition of hard to medium on the third lap. Medium tires turn to medium on the second lap and bad on the third lap. Soft tires turn to bad on the second lap. Once tires are bad, the talent score for the driver decreases by 1. The talent score determines the maximum speed of the driver. Each section of the course (4 straights and 4 turns), a new speed is randomly generated with bounds between 1 and the drivers talent score. Slow drivers have a talent of 2, while fast drivers have a talent of 5. Thus, slow drivers can still drive faster than fast drivers on certain sections, though it is unlikely. This file currently generates 10 cars and places them in a grid that is two cars across and five cars deep.

## ER Diagram



## Sources

Sources:
https://www.indycar.com/Standings
https://www.racing-reference.info/indycar-series/
https://en.wikipedia.org/wiki/2025_IndyCar_Series
https://en.wikipedia.org/wiki/2025_Indianapolis_500
