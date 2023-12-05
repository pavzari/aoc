def get_lowest_location(input):
    seeds = input[0][0].split(": ")[1].split(" ")

    locations = []

    for seed in seeds:
        seed_to_soil = lookup(int(seed), input[1][1:])
        soil_to_fertilizer = lookup(seed_to_soil, input[2][1:])
        fertilizer_to_water = lookup(soil_to_fertilizer, input[3][1:])
        water_to_light = lookup(fertilizer_to_water, input[4][1:])
        light_to_temperature = lookup(water_to_light, input[5][1:])
        temperature_to_humidity = lookup(light_to_temperature, input[6][1:])
        humidity_to_location = lookup(temperature_to_humidity, input[7][1:])

        locations.append(humidity_to_location)

    return min(locations)


def lookup(value, input):
    """Find the range that contains the given input and find
    the mapping by offset instead of building a full map"""
    ranges = [ranges.split(" ") for ranges in input]

    result = value
    for rang in ranges:
        source_start = int(rang[1])
        dest_start = int(rang[0])
        range_lenght = int(rang[2])

        if value >= source_start and value <= (source_start + range_lenght):
            result = dest_start + (value - source_start)

    return result


if __name__ == "__main__":
    input = [
        mapping.split("\n") for mapping in open("input/d5", "r").read().split("\n\n")
    ]
    print(get_lowest_location(input))
