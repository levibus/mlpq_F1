# generate_mlpq.py
import random
import math

def write_mlpq(
    filename,
    car_id,
    driver_id,
    team_id,
    tire_id,
    car_number,
    x_position,
    y_position,
    talent,
    dt_first_straight,
    dt_turn,
    dt_short_straight,
    dt_long_straight,
    final_position_x=32,
    final_position_y=-8,
):

    with open(filename, "a") as f:
        
        hardness = random.choice(["hard", "medium", "soft"])
        condition = "good"        
        # tires
        
        for lap_number in range(1,4):
            match hardness:
                case "hard":
                    if lap_number == 3:
                        condition = "medium"
                case "medium":
                    if lap_number == 2:
                        condition = "medium"
                    elif lap_number == 3:
                        condition = "bad"
                case "soft":
                    if lap_number == 2:
                        condition = "bad"
            f.write(
                f"tire{car_number}(tire_id, hardness, condition, lap_number) :- "
                f"tire_id={tire_id}, hardness=\"{hardness}\", condition=\"{condition}\", lap_number={lap_number}. \n"
            )

        lap_number = 1
        condition = "good"        

        next_speed = random.randint(1,talent)
        next_turn_speed = math.ceil(next_speed / 2)
        dt_first_straight_var = math.floor(dt_first_straight / next_speed)
        
        previous_t = 0
        next_x = x_position
        next_y = y_position
        next_t = dt_first_straight_var
        
        speed = next_speed
        turn_speed = next_turn_speed

        # first straight
        f.write(
            f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
            f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x-{speed}t>={next_x}, x-{speed}t<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
         
        for i in range(3):
            
            match hardness:
                case "hard":
                    if lap_number == 3:
                        condition = "medium"
                case "medium":
                    if lap_number == 2:
                        condition = "medium"
                    elif lap_number == 3:
                        condition = "bad"
                        talent -= 1
                case "soft":
                    if lap_number == 2:
                        condition = "bad"
                        talent -= 1
             
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_turn_var =  math.floor(dt_turn / next_turn_speed)

            previous_t = next_t
            next_x += (speed * previous_t) - (next_turn_speed * previous_t )
            next_y +=  -(next_turn_speed * previous_t)
            next_t = previous_t + dt_turn_var
            
            speed = next_speed
            turn_speed = next_turn_speed
        
            # first turn
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x-{turn_speed}t>={next_x}, x-{turn_speed}t<={next_x + 1}, y-{turn_speed}t>={next_y}, y-{turn_speed}t<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_short_straight_var =  math.floor(dt_short_straight / next_speed)

            previous_t = next_t
            next_x += turn_speed * previous_t
            next_y += turn_speed * previous_t - (next_speed * previous_t)
            previous_t += 1
            next_t += dt_short_straight_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # first short straight 
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x>={next_x}, x<={next_x + 1}, y-{speed}t>={next_y}, y-{speed}t<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_turn_var =  math.floor(dt_turn / next_turn_speed)

            previous_t = next_t
            next_x += (next_turn_speed * previous_t)
            next_y += speed * previous_t - (next_turn_speed * previous_t)
            previous_t += 1
            next_t += dt_turn_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # second turn
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x+{turn_speed}t>={next_x}, x+{turn_speed}t<={next_x + 1}, y-{turn_speed}t>={next_y}, y-{turn_speed}t<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_long_straight_var =  math.floor(dt_long_straight / next_speed)

            previous_t = next_t
            next_x += next_speed * previous_t - (turn_speed * previous_t)
            next_y += turn_speed * previous_t
            previous_t += 1
            next_t += dt_long_straight_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # back long straight
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x+{speed}t>={next_x}, x+{speed}t<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_turn_var =  math.floor(dt_turn / next_turn_speed)
            
            previous_t = next_t
            next_x += next_turn_speed * previous_t - (speed * previous_t)
            next_y += next_turn_speed * previous_t
            previous_t += 1
            next_t += dt_turn_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # third turn
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x+{turn_speed}t>={next_x}, x+{turn_speed}t<={next_x + 1}, y+{turn_speed}t>={next_y}, y+{turn_speed}t<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_short_straight_var =  math.floor(dt_short_straight / next_speed)
            
            previous_t = next_t
            next_x += -(turn_speed * previous_t)
            next_y += next_speed * previous_t - (turn_speed * previous_t)
            previous_t += 1
            next_t += dt_short_straight_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # second short straight
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x>={next_x}, x<={next_x + 1}, y+{speed}t>={next_y}, y+{speed}t<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_turn_var =  math.floor(dt_turn / next_turn_speed)
            
            previous_t = next_t
            next_x += -(next_turn_speed * previous_t) # TODO: is this right?
            next_y += next_turn_speed * previous_t - (speed * previous_t)
            previous_t += 1
            next_t += dt_turn_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # fourth turn
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x-{turn_speed}t>={next_x}, x-{turn_speed}t<={next_x + 1}, y+{turn_speed}t>={next_y}, y+{turn_speed}t<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            next_speed = random.randint(1,talent)
            next_turn_speed =  math.ceil(next_speed / 2)
            dt_long_straight_var =  math.floor(dt_long_straight / next_speed)
            
            previous_t = next_t
            next_x += -(next_speed * previous_t) + (turn_speed * previous_t)
            next_y += -(turn_speed * previous_t)
            previous_t += 1
            next_t += dt_long_straight_var
            
            speed = next_speed
            turn_speed = next_turn_speed
            
            # front long straight
            f.write(
                f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
                f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x-{speed}t>={next_x}, x-{speed}t<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
                f"t>={previous_t}, t<={next_t}. \n"
            )
            
            lap_number += 1
        
        previous_t = next_t
        next_x = final_position_x
        next_y = final_position_y
        previous_t += 1
        next_t = 1000
        
        # stop at end
        f.write(
            f"car{car_number}(car_id, x, y, t, driver_id, team_id, tire_id, lap_number, talent) :- "
            f"car_id={car_id}, driver_id={driver_id}, team_id={team_id}, tire_id={tire_id}, lap_number={lap_number}, talent={talent}, x>={next_x}, x<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
         

if __name__ == "__main__":
    
    # units of speed 1
    # dt_first_straight=44
    # dt_turn=16
    # dt_short_straight=36
    # dt_long_straight=96
    
    with open('output.txt','w') as f:
        pass

    # 1st right lane
    write_mlpq(
        "output.txt",
        car_id=10,
        driver_id=1,
        team_id=1,
        tire_id=1,
        car_number=1,
        x_position=0,
        y_position=-28,
        talent=4,
        dt_first_straight=44,
        dt_turn=10,
        dt_short_straight=32,
        dt_long_straight=90,
        final_position_x=32,
        final_position_y=-8,
    )
    
    # 1st left lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=2,
        team_id=2,
        tire_id=2,
        car_number=2,
        x_position=0,
        y_position=-24,
        talent=5,
        dt_first_straight=44,
        dt_turn=10,
        dt_short_straight=31,
        dt_long_straight=90,
        final_position_x=32,
        final_position_y=-4,
    )
    
    # 2nd right lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=3,
        team_id=3,
        tire_id=3,
        car_number=3,
        x_position=-4,
        y_position=-28,
        talent=3,
        dt_first_straight=48,
        dt_turn=10,
        dt_short_straight=32,
        dt_long_straight=90,
        final_position_x=28,
        final_position_y=-8,
    )
    
    # 2nd left lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=4,
        team_id=4,
        tire_id=4,
        car_number=4,
        x_position=-4,
        y_position=-24,
        talent=2,
        dt_first_straight=48,
        dt_turn=10,
        dt_short_straight=31,
        dt_long_straight=90,
        final_position_x=28,
        final_position_y=-4,
    )
    
    # 3rd right lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=5,
        team_id=5,
        tire_id=5,
        car_number=5,
        x_position=-8,
        y_position=-28,
        talent=3,
        dt_first_straight=52,
        dt_turn=10,
        dt_short_straight=32,
        dt_long_straight=90,
        final_position_x=24,
        final_position_y=-8,
    )
    
    # 3rd left lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=6,
        team_id=5,
        tire_id=6,
        car_number=6,
        x_position=-8,
        y_position=-24,
        talent=2,
        dt_first_straight=52,
        dt_turn=9,
        dt_short_straight=31,
        dt_long_straight=90,
        final_position_x=24,
        final_position_y=-4,
    )
    
    # 4th right lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=7,
        team_id=4,
        tire_id=7,
        car_number=7,
        x_position=-12,
        y_position=-28,
        talent=3,
        dt_first_straight=56,
        dt_turn=10,
        dt_short_straight=32,
        dt_long_straight=90,
        final_position_x=20,
        final_position_y=-8,
    )
    
    # 4th left lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=8,
        team_id=3,
        tire_id=8,
        car_number=8,
        x_position=-12,
        y_position=-24,
        talent=3,
        dt_first_straight=56,
        dt_turn=9,
        dt_short_straight=31,
        dt_long_straight=90,
        final_position_x=20,
        final_position_y=-4,
    )
    
    # 5th right lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=9,
        team_id=2,
        tire_id=9,
        car_number=9,
        x_position=-16,
        y_position=-28,
        talent=4,
        dt_first_straight=60,
        dt_turn=10,
        dt_short_straight=32,
        dt_long_straight=90,
        final_position_x=16,
        final_position_y=-8,
    )
    
    # 5th left lane
    write_mlpq(
        "output.txt",
        car_id=11,
        driver_id=10,
        team_id=1,
        tire_id=10,
        car_number=10,
        x_position=-16,
        y_position=-24,
        talent=5,
        dt_first_straight=60,
        dt_turn=9,
        dt_short_straight=31,
        dt_long_straight=90,
        final_position_x=16,
        final_position_y=-4,
    )