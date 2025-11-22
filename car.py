# generate_mlpq.py
import math

def write_mlpq(
    filename,
    id,
    car_number,
    x_position,
    y_position,
    speed, 
    dt_first_straight,
    dt_turn,
    dt_short_straight,
    dt_long_straight,
):

    with open(filename, "w") as f:

        turn_speed = math.sqrt(speed)

        # first straight
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x-{speed}t>={x_position}, x-{speed}t<={x_position + 1}, y>={y_position}, y<={y_position + 1}, "
            f"t>=0, t<={dt_first_straight}. \n"
        )
        previous_t = dt_first_straight + 1
        next_x = x_position + turn_speed * previous_t 
        next_y = y_position - turn_speed * previous_t 
        next_t = previous_t + dt_turn
        
        # first turn
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x-{turn_speed}t>={next_x}, x-{turn_speed}t<={next_x + 1}, y-{turn_speed}t>={next_y}, y-{turn_speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        previous_t = next_t
        next_x += turn_speed * previous_t
        next_y += turn_speed * previous_t - (speed * previous_t)
        previous_t += 1
        next_t += dt_short_straight
        
        # first short straight 
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x>={next_x}, x<={next_x + 1}, y-{speed}t>={next_y}, y-{speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        previous_t = next_t
        next_x += speed * previous_t - (turn_speed * previous_t)
        next_y += speed * previous_t - (turn_speed * previous_t)
        previous_t += 1
        next_t += dt_turn
        
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x+{turn_speed}t>={next_x}, x+{turn_speed}t<={next_x + 1}, y-{turn_speed}t>={next_y}, y-{turn_speed}t<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )
        previous_t = next_t
        next_x += speed * previous_t - (turn_speed * previous_t)
        next_y += turn_speed * previous_t
        previous_t += 1
        next_t += dt_long_straight
        
        f.write(
            f"car{car_number}(id, x, y, t) :- "
            f"id={id}, x+{speed}t>={next_x}, x+{speed}t<={next_x + 1}, y>={next_y}, y<={next_y + 1}, "
            f"t>={previous_t}, t<={next_t}. \n"
        )


if __name__ == "__main__":
    # Example usage
    write_mlpq(
        "output.txt",
        id=10,
        car_number=1,
        x_position=0,
        y_position=-28,
        speed=4,
        dt_first_straight=11,
        dt_turn=4,
        dt_short_straight=9,
        dt_long_straight=24,
    )