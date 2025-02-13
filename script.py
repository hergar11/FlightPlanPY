from Protected import Structures as Flight
from Protected import db as db


Waypoint0 = Flight.Waypoint(Flight.Radial(db.Afganistan.tacan75x, 0, 0), 'Kandahar')
Waypoint1 = Flight.Waypoint(Flight.Radial(db.Afganistan.tacan75x, 269, 37), 'ADDER')
Waypoint2 = Flight.Waypoint(Flight.Radial(db.Afganistan.tacan78x, 291, 39), 'Bravo')
Waypoint3 = Flight.Waypoint(Flight.Radial(db.Afganistan.tacan78x, 278, 105), 'Charlie')
Waypoint4 = Flight.Waypoint(Flight.Radial(db.Afganistan.tacan78x, 287, 109), 'TGT2')

flightplan = Flight.Flihtplan('Test', [Waypoint0, Waypoint1, Waypoint2, Waypoint3, Waypoint4])

with open('output.txt', 'w') as f:
    f.write(flightplan.get_flightplan())