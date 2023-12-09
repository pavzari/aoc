def get_lowest_location(input):
    """Initial brute force approach: works on sample data but causes
    an out-of-memory crash with actual input"""
    seeds = input[0][0].split(": ")[1].split(" ")

    seed_to_soil = make_mapping_dict(input[1][1:])
    soil_to_fertilizer = make_mapping_dict(input[2][1:])
    fertilizer_to_water = make_mapping_dict(input[3][1:])
    water_to_light = make_mapping_dict(input[4][1:])
    light_to_temperature = make_mapping_dict(input[5][1:])
    temperature_to_humidity = make_mapping_dict(input[6][1:])
    humidity_to_location = make_mapping_dict(input[7][1:])

    locations = []

    for seed in seeds:
        final = chained_lookup(
            int(seed),
            seed_to_soil,
            soil_to_fertilizer,
            fertilizer_to_water,
            water_to_light,
            light_to_temperature,
            temperature_to_humidity,
            humidity_to_location,
        )
        locations.append(final)

    return min(locations)


def chained_lookup(start_value, *dictionaries):
    result = start_value
    for d in dictionaries:
        result = d.get(result, result)
    return result


def make_mapping_dict(input):
    values = [ranges.split(" ") for ranges in input]

    dicts = []
    for rang in values:
        source = list(range(int(rang[1]), int(rang[1]) + int(rang[2])))
        destination = list(range(int(rang[0]), int(rang[0]) + int(rang[2])))
        mapping = {source[i]: destination[i] for i in range(len(source))}
        dicts.append(mapping)

    super_dict = {}

    for d in dicts:
        for k, v in d.items():
            super_dict[k] = v

    return super_dict


if __name__ == "__main__":
    input = [
        mapping.split("\n") for mapping in open("input/d5", "r").read().split("\n\n")
    ]
    print(get_lowest_location(input))
