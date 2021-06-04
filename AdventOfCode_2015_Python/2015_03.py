FILEPATH = "../data/2015/03.txt"


def main():
    directions = get_data(FILEPATH)
    houses_visited_by_santa = santa_deliveries(directions)
    print(f"Santa visited at least {houses_visited_by_santa} houses.")
    houses_visited_by_santa_and_robo = santa_robo_deliveries(directions)
    print(f"Santa and Robo Santa visited at least {houses_visited_by_santa_and_robo} houses.")


def get_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def santa_robo_deliveries(directions):
    direction_index = 0
    total_moves = 0
    santa_location = (0,0)
    robo_location = (0,0)
    places_visited = {(0,0)}
    presents_delivered = 2
    houses_already_hit = 1
    for direction in directions:
            presents_delivered += 1
            total_moves += 1
            if direction_index % 2 == 0:
                new_location_x = santa_location[0]
                new_location_y = santa_location[1]
            else:
                new_location_x = robo_location[0]
                new_location_y = robo_location[1]
            if direction == ">":
                new_location_x += 1
            elif direction == "^":
                new_location_y += 1              
            elif direction == "<":
                new_location_x -= 1
            elif direction == "v" or "V":
                new_location_y -= 1
            new_location = (new_location_x, new_location_y)
            if direction_index % 2 == 0:
                santa_location = new_location
            else:
                robo_location = new_location
            if new_location in places_visited:
                houses_already_hit += 1
            else:
                places_visited.add(new_location)
            direction_index += 1
    return presents_delivered-houses_already_hit


def santa_deliveries(directions):
        total_moves = 0
        current_location = (0,0)
        places_visited = {(0,0)}
        presents_delivered = 1
        houses_already_hit = 0
        for direction in directions:
            presents_delivered += 1
            total_moves += 1
            old_location_x = current_location[0]
            old_location_y = current_location[1]
            if direction == ">":
                old_location_x += 1
            elif direction == "^":
                old_location_y += 1              
            elif direction == "<":
                old_location_x -= 1
            elif direction == "v" or "V":
                old_location_y -= 1
            new_location = (old_location_x, old_location_y)
            current_location = new_location
            if new_location in places_visited:
                houses_already_hit += 1
            else:
                places_visited.add(new_location)
        return presents_delivered - houses_already_hit


if __name__ ==  "__main__":
    main()