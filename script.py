import Structures as Flight
import db

Waypoint0 = Flight.Waypoint(Flight.Radial(db.tacan75x, 0, 0), 'Kandahar')
Waypoint1 = Flight.Waypoint(Flight.Radial(db.tacan75x, 269, 37), 'ADDER')
Waypoint2 = Flight.Waypoint(Flight.Radial(db.tacan78x, 291, 39), 'Bravo')
Waypoint3 = Flight.Waypoint(Flight.Radial(db.tacan78x, 278, 105), 'Charlie')
Waypoint4 = Flight.Waypoint(Flight.Radial(db.tacan78x, 287, 109), 'TGT2')

flightplan = Flight.Flihtplan('Test', [Waypoint0, Waypoint1, Waypoint2, Waypoint3, Waypoint4])
flightplan.get_flightplan()