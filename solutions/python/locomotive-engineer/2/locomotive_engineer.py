"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    wagon_numbers = []
    for wagon_num in wagons:
        wagon_numbers.append(wagon_num)
    return wagon_numbers
        


def fix_list_of_wagons(each_wagons_id,  missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    a, b, c, *rest = each_wagons_id
    fixed_list = [c] + missing_wagons + rest + [a, b]
    return fixed_list


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    
    route["stops"] = [stop for stop in stops.values()]
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended_route = {**route, **more_route_information}
    return extended_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    wagons_rows_fixed = []
    transposed_wagons_rows = zip(*wagons_rows)
    for row in transposed_wagons_rows:
        wagons_rows_fixed.append(list(row))

    return list(wagons_rows_fixed)
