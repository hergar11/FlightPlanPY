import math
from tabulate import tabulate
#distance is is nm
def dms_to_dd(degrees: int, minutes: int, seconds: float) -> float:
    return degrees + (minutes / 60) + (seconds / 3600)

def dd_to_dms(decimal_degrees: float) -> tuple:
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600
    return degrees, minutes, seconds
class Path:
    def __init__(self, heading: float = 0, distance:float = 0) -> None:
        self.Heading    = heading
        self.distanceNm = distance

class Coordinates:
    # Constructor that takes latitude in longitude in degrees
    def __init__(self, latitude: float = None, longitude: float = None) -> None:
        #NOTE if latiude is Nord it is positive, if it is Sud it is negative
        #NOTE if longitude is East it is positive, if it is West it is negative
        if  latitude is None or longitude is None:
            raise ValueError("latitude, longitude must be provided")
        self.LatitudeRad  = math.radians(latitude)
        self.LongitudeRad = math.radians(longitude)

    def shift_coordinates(self, Radial: float, DME: float) -> 'Coordinates':
        # source of the formula: https://www.movable-type.co.uk/scripts/latlong.html && https://chatgpt.com/c/67ab320e-8360-8002-9129-2d3daf88878a
        if (Radial < 0 or Radial > 360):
            raise ValueError("Radial must be between 0 and 360")
        if (DME < 0):
            raise ValueError("DME must be greater than 0")

        RadialRad = math.radians(Radial)

        new_latitude = math.asin(math.sin(self.LatitudeRad) * math.cos(DME / 3440.065) + math.cos(self.LatitudeRad) * math.sin(DME / 3440.065) * math.cos(RadialRad))

        new_longitude = self.LongitudeRad + math.atan2(math.sin(RadialRad) * math.sin(DME / 3440.065) * math.cos(self.LatitudeRad), math.cos(DME / 3440.065) - (math.sin(self.LatitudeRad) * math.sin(new_latitude)))

        return Coordinates(math.degrees(new_latitude), math.degrees(new_longitude))

    def calculate_path(self, new_coordinates: 'Coordinates') -> Path:
        # Source Distance Calculation Harvesine Formula https://chatgpt.com/c/67ab320e-8360-8002-9129-2d3daf88878a
        a = math.sin((new_coordinates.LatitudeRad - self.LatitudeRad) / 2) ** 2 + math.cos(self.LatitudeRad) * math.cos(new_coordinates.LatitudeRad) * math.sin((new_coordinates.LongitudeRad - self.LongitudeRad) / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = 3440.065 * c
        # Source Heading Calculation  (Initial Bearing) Formula https://chatgpt.com/c/67ab320e-8360-8002-9129-2d3daf88878a
        phi = math.atan2(math.sin(new_coordinates.LongitudeRad - self.LongitudeRad) * math.cos(new_coordinates.LatitudeRad), math.cos(self.LatitudeRad) * math.sin(new_coordinates.LatitudeRad) - math.sin(self.LatitudeRad) * math.cos(new_coordinates.LatitudeRad) * math.cos(new_coordinates.LongitudeRad - self.LongitudeRad))
        heading = (phi * 180 / math.pi + 360) % 360

        return Path(heading, distance)

    def get_coordinates_in_degrees(self) -> tuple:
        print(f"Coordinates: {math.degrees(self.LatitudeRad)} {math.degrees(self.LongitudeRad)}")


class PointToPoint:
    # Structure that will hold the PointToPoint definition
    def __init__(self) -> None:
        self.heading = 0
        self.distance = 0

class Tacan:
    # Structure that will hold the Tacan definition
    #x and y coordinates are in meters and uses CCS(DCS coordinates)
    def __init__(self, freq: float = None, letter: str = None, coordinates: Coordinates = None) -> None:
        if freq is None or letter is None or Coordinates is None:
            raise ValueError("Freq, Letter, XCoordinates, and ZCoordinates must be provided")
        self.Freq = freq
        self.Letter = letter
        self.Coordinates = coordinates

class Radial:

    def __init__(self, Tacan: Tacan = None, angle: float = None, DME: float = None) -> None:
        if Tacan is None or DME is None or angle is None:
            raise ValueError("Tacan, DME, and angle must be provided")
        self.Tacan = Tacan
        self.DME   = DME
        self.angle = angle
        self.Coordinates = self.Tacan.Coordinates.shift_coordinates(self.angle, self.DME)

class Waypoint:
    def __init__(self, radial: Radial = None, waypoint_name: str = '') -> None:
        if radial is None or not waypoint_name:
            raise ValueError("Radial and WaypointName must be provided")
        self.Radial = radial
        self.WaypointName   = waypoint_name
        self.Coordinates    = self.Radial.Coordinates
        self.path           = Path()

class Flihtplan:
    def __init__(self, name: str = '', flightpoints: list = None) -> None:
        if not name or flightpoints is None:
            raise ValueError("Name and flightpoints must be provided")
        self.Name = name
        self.Flightpoints     = flightpoints
        self.FlightPlanPoints = flightpoints
        for each in self.FlightPlanPoints:
            if self.FlightPlanPoints.index(each) < len(self.FlightPlanPoints) - 1:
                next_point = self.FlightPlanPoints[self.FlightPlanPoints.index(each) + 1]
                path = each.Radial.Coordinates.calculate_path(next_point.Radial.Coordinates)
                self.FlightPlanPoints[self.FlightPlanPoints.index(each)].path = path
            else:
                path = each.Radial.Coordinates.calculate_path(self.FlightPlanPoints[len(self.FlightPlanPoints) - 2].Radial.Coordinates)
                self.FlightPlanPoints[self.FlightPlanPoints.index(each)].path = path
# DEPRECATED
    def get_flightplanConsole(self,TwoWay: bool = True) -> None:
        #TwoWay will print the flightplan go and return.
        for each in self.FlightPlanPoints:
            print(f"Waypoint: {each.WaypointName} Heading: {round(each.path.Heading)} Distance: {round(each.path.distanceNm)}")

        reversed_points = list(reversed(self.FlightPlanPoints))
        reversed_points.pop(0)
        if TwoWay:
            for each in reversed_points:
                if  reversed_points.index(each) != len(reversed_points) - 1:
                    next_point = reversed_points[reversed_points.index(each) + 1]
                    print(f"Waypoint: {each.WaypointName} Heading: {round((next_point.path.Heading + 180) % 360)} Distance: {round(next_point.path.distanceNm)}")
                else:
                    print(f"Waypoint: {each.WaypointName} Arrival")
#End of DEPRECATED

    def get_flightplan(self,TwoWay: bool = True) -> None:
        table = []
        for each in self.FlightPlanPoints:
            pointDefstr = ''
            if each.Radial.DME == 0:
                pointDefstr= f"{round(each.Radial.Tacan.Freq)}{each.Radial.Tacan.Letter}"
            else:
                pointDefstr= f"{round(each.Radial.Tacan.Freq)}{each.Radial.Tacan.Letter}/{each.Radial.angle}-{round(each.Radial.DME)}nm"# Definiton of the point
            table.append([self.FlightPlanPoints.index(each),each.WaypointName, pointDefstr, round(each.path.Heading), round(each.path.distanceNm)])

        reversed_points = list(reversed(self.FlightPlanPoints))
        reversed_points.pop(0)
        if TwoWay:
            for each in reversed_points:
                pointDefstr = ''
                if each.Radial.DME == 0:
                    pointDefstr= f"{round(each.Radial.Tacan.Freq)}{each.Radial.Tacan.Letter}"
                else:
                    pointDefstr= f"{round(each.Radial.Tacan.Freq)}{each.Radial.Tacan.Letter}/{each.Radial.angle}-{round(each.Radial.DME)}nm"# Definiton of the point
                if reversed_points.index(each) != len(reversed_points) - 1:
                    next_point = reversed_points[reversed_points.index(each) + 1]
                    table.append([self.FlightPlanPoints.index(each),each.WaypointName,pointDefstr, round((next_point.path.Heading + 180) % 360), round(next_point.path.distanceNm)])
                else:
                    table.append([self.FlightPlanPoints.index(each),each.WaypointName,pointDefstr, "Arrival"])

        table = tabulate(table, headers=["ID","Waypoint","Tacan/Radial/DME(nm)", "Heading", "Distance (nm)"], tablefmt="grid")
        with open('output.txt', 'w') as f:
            f.write(table)