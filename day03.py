input_path = 'input.txt'


def get_direction_modifiers(direction):
    if direction[0] == 'L':
        return -1, 0
    if direction[0] == 'R':
        return 1, 0
    if direction[0] == 'U':
        return 0, 1
    if direction[0] == 'D':
        return 0, -1


def intersection_distance(coords):
    return abs(coords[0]) + abs(coords[1])


def trace_wire(wire_path):
    coordinates = set()
    current_x = 0
    current_y = 0

    directions = wire_path.split(',')
    for direction in directions:
        (x_modifier, y_modifier) = get_direction_modifiers(direction)
        distance = int(direction[1:])

        for pos in range(distance):
            current_x += x_modifier
            current_y += y_modifier
            coordinates.add((current_x, current_y))

    return coordinates


def solve_part_one():
    with open(input_path) as input_file:
        wire1 = input_file.readline().strip()
        wire1_coords = trace_wire(wire1)

        wire2 = input_file.readline().strip()
        wire2_coords = trace_wire(wire2)

        min_distance = 1 << 63
        intersections = wire1_coords.intersection(wire2_coords)
        for intersection in intersections:
            current_distance = intersection_distance(intersection)
            min_distance = min(min_distance, current_distance)

        print(min_distance)


def get_intersection_steps(wire_path, intersections):
    intersection_steps = {}
    current_x = 0
    current_y = 0

    total = 0
    directions = wire_path.split(',')
    for direction in directions:
        (x_modifier, y_modifier) = get_direction_modifiers(direction)
        distance = int(direction[1:])

        for pos in range(distance):
            total += 1
            current_x += x_modifier
            current_y += y_modifier
            if (current_x, current_y) in intersections:
                if (current_x, current_y) not in intersection_steps:
                    intersection_steps[(current_x, current_y)] = total

    return intersection_steps


def solve_part_two():
    with open(input_path) as input_file:
        wire1 = input_file.readline().strip()
        wire1_coords = trace_wire(wire1)

        wire2 = input_file.readline().strip()
        wire2_coords = trace_wire(wire2)

        intersections = wire1_coords.intersection(wire2_coords)
        wire1_steps = get_intersection_steps(wire1, intersections)
        wire2_steps = get_intersection_steps(wire2, intersections)

        min_distance = 1 << 63
        for intersection in intersections:
            current_distance = wire1_steps[intersection] + wire2_steps[intersection]
            min_distance = min(min_distance, current_distance)

        return min_distance


if __name__ == '__main__':
    result = solve_part_two()
    print(result)
