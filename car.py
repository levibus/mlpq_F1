# generate_mlpq.py
import random
import math

def write_mlpq(
    filename,
    id,
    car_number,
    x_position,
    y_position,
    dt_first_straight,
    dt_turn,
    dt_short_straight,
    dt_long_straight,
):

    with open(filename, "a") as f:

        speed = random.randint(1,3)
        turn_speed = math.ceil(speed / 2)
        dt_first_straight_var = math.floor(dt_first_straight / speed)

        # first straight
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x-{speed}t>={x_position}, x-{speed}t<={x_position + 1}, y>={y_position}, y<={y_position + 1}, "
            f"t>=0, t<={dt_first_straight_var}. \n"
        )
        
        next_speed = random.randint(1,3)
        next_turn_speed =  math.ceil(next_speed / 2)
        dt_turn_var =  math.floor(dt_turn / next_turn_speed)

        previous_t = dt_first_straight_var + 1
        next_x = x_position + (speed * previous_t) - (next_turn_speed * previous_t )
        next_y = y_position - next_turn_speed * previous_t 
        next_t = previous_t + dt_turn_var
        
        speed = next_speed
        turn_speed = next_turn_speed
        
        # first turn
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x-{turn_speed}t>={next_x}, x-{turn_speed}t<={next_x + 1}, y-{turn_speed}t>={next_y}, y-{turn_speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        next_speed = random.randint(1,3)
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
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x>={next_x}, x<={next_x + 1}, y-{speed}t>={next_y}, y-{speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        next_speed = random.randint(1,3)
        next_turn_speed =  math.ceil(next_speed / 2)
        dt_turn_var =  math.floor(dt_turn / next_turn_speed)

        # TODO: something is going wrong here

        previous_t = next_t
        next_x += speed * previous_t - (next_turn_speed * previous_t)
        next_y += speed * previous_t - (next_turn_speed * previous_t)
        previous_t += 1
        next_t += dt_turn_var
        
        speed = next_speed
        turn_speed = next_turn_speed
        
        # second turn
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x+{turn_speed}t>={next_x}, x+{turn_speed}t<={next_x + 1}, y-{turn_speed}t>={next_y}, y-{turn_speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        next_speed = random.randint(1,3)
        next_turn_speed =  math.ceil(next_speed / 2)
        dt_long_straight_var =  math.floor(dt_long_straight / next_speed)

        previous_t = next_t
        next_x += speed * previous_t - (next_turn_speed * previous_t)
        next_y += turn_speed * previous_t
        previous_t += 1
        next_t += dt_long_straight_var
        
        speed = next_speed
        turn_speed = next_turn_speed
        
        # back long straight
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x+{speed}t>={next_x}, x+{speed}t<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        next_speed = random.randint(1,3)
        next_turn_speed =  math.ceil(next_speed / 2)
        dt_turn_var =  math.floor(dt_turn / next_turn_speed)
        
        previous_t = next_t
        next_x += turn_speed * previous_t - (next_speed * previous_t)
        next_y += turn_speed * previous_t
        previous_t += 1
        next_t += dt_turn_var
        
        # third turn
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x+{turn_speed}t>={next_x}, x+{turn_speed}t<={next_x + 1}, y+{turn_speed}t>={next_y}, y+{turn_speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        speed = random.randint(1,3)
        turn_speed =  math.ceil(speed / 2)
        dt_short_straight_var =  math.floor(dt_short_straight / speed)
        
        previous_t = next_t
        next_x += -(turn_speed * previous_t)
        next_y += speed * previous_t - (turn_speed * previous_t)
        previous_t += 1
        next_t += dt_short_straight_var
        
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x>={next_x}, x<={next_x + 1}, y+{speed}t>={next_y}, y+{speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        speed = random.randint(1,3)
        turn_speed =  math.ceil(speed / 2)
        dt_turn_var =  math.floor(dt_turn / turn_speed)
        
        previous_t = next_t
        next_x += -(turn_speed * previous_t)
        next_y += turn_speed * previous_t - (speed * previous_t)
        previous_t += 1
        next_t += dt_turn_var
        
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x-{turn_speed}t>={next_x}, x-{turn_speed}t<={next_x + 1}, y+{turn_speed}t>={next_y}, y+{turn_speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        
        speed = random.randint(1,3)
        turn_speed =  math.ceil(speed / 2)
        dt_long_straight_var =  math.floor(dt_long_straight / speed)
        
        previous_t = next_t
        next_x += -(speed * previous_t) + (turn_speed * previous_t)
        next_y += -(turn_speed * previous_t)
        previous_t += 1
        next_t += dt_long_straight
        
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x-{speed}t>={next_x}, x-{speed}t<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
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

    
    write_mlpq(
        "output.txt",
        id=10,
        car_number=1,
        x_position=0,
        y_position=-28,
        dt_first_straight=44,
        dt_turn=16,
        dt_short_straight=36,
        dt_long_straight=96,
    )
    
    write_mlpq(
        "output.txt",
        id=11,
        car_number=2,
        x_position=0,
        y_position=-24,
        dt_first_straight=48,
        dt_turn=16,
        dt_short_straight=36,
        dt_long_straight=98,
    )