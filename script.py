import Structures as Flight

tacan75x = Flight.Tacan(75.00, 'X', Flight.Coordinates(Flight.dms_to_dd(31,30,20), Flight.dms_to_dd(65,50,54)))
tacan78x = Flight.Tacan(78.00, 'X', Flight.Coordinates(Flight.dms_to_dd(31,49,45), Flight.dms_to_dd(64,13,1)))
Waypoint0 = Flight.Waypoint(Flight.Radial(tacan75x, 0, 0), 'Kandahar')
Waypoint1 = Flight.Waypoint(Flight.Radial(tacan75x, 269, 37), 'ADDER')
Waypoint2 = Flight.Waypoint(Flight.Radial(tacan78x, 291, 39), 'Bravo')
Waypoint3 = Flight.Waypoint(Flight.Radial(tacan78x, 278, 105), 'Charlie')
Waypoint4 = Flight.Waypoint(Flight.Radial(tacan78x, 287, 109), 'TGT2')

flightplan = Flight.Flihtplan('Test', [Waypoint0, Waypoint1, Waypoint2, Waypoint3, Waypoint4])
flightplan.get_flightplan()