benches = [-5, -1, 3, 6, 8, 9]
radius = 5


# finding the number of points it will be in the radius and where the center would be.
def find(benches, radius):
    line_length = benches[-1] - benches[0] + (2 * radius) + 2
    points = [0] * line_length
    if benches[0] < 0:
        offset = radius - benches[0]
    else:
        offset = radius - benches[0]

    for i in benches:
        start = i - radius + offset
        end = i + radius + offset
        points[start] += 1
        points[end + 1] -= 1

    max_light = current_light = 0
    lamp_location = 0
    for loc, changes in enumerate(points):
        current_light += changes
        if current_light > max_light:
            max_light = current_light
            lamp_location = loc

    return max_light, (lamp_location - offset)


print(find(benches, radius))

