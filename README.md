Software to create Flight Plans. Oriented specially in planes that does not have GPS and requires TACAN, RADIAL, Heading, to navigate

Example Of Use:
    tacan75x = Tacan(75.00, 'X', Coordinates(dms_to_dd(31,30,20), dms_to_dd(65,50,54)))
    tacan78x = Tacan(78.00, 'X', Coordinates(dms_to_dd(31,49,45), dms_to_dd(64,13,1)))
    Waypoint0 = Waypoint(Radial(tacan75x, 0, 0), 'Kandahar')
    Waypoint1 = Waypoint(Radial(tacan75x, 269, 37), 'ADDER')
    Waypoint2 = Waypoint(Radial(tacan78x, 291, 39), 'Bravo')
    Waypoint3 = Waypoint(Radial(tacan78x, 278, 105), 'Charlie')
    Waypoint4 = Waypoint(Radial(tacan78x, 287, 109), 'TGT2')

    flightplan = Flihtplan('Test', [Waypoint0, Waypoint1, Waypoint2, Waypoint3, Waypoint4])
    flightplan.get_flightplan()

    This few lines will create the flight plan with all the required heading distances to go to target and to return.