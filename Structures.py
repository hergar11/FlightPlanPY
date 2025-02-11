import math
#distance is is nm
class Path:
    def __init__(self, heading: float = None, distance:float = None) -> None:
        if heading is None or distance is None:
            raise ValueError("Heading & distance must be provided")
        self.Heading    = heading
        self.distanceNm = distance

class Coordinates:
    # Constructor that takes latitude in longitude in degrees
    def __init__(self, latitude: float = None, longitude: float = None) -> None:
        #NOTE if latiude is Nord it is positive, if it is Sud it is negative
        #NOTE if longitude is East it is positive, if it is West it is negative
        if  latitude is None or longitude is None:
            raise ValueError("latitude, longitude, and Z must be provided")
        self.LatitudeRad  = math.radians(latitude)
        self.LongitudeRad = math.radians(longitude)

    def shift_coordinates(self, Radial: float, DME: float) -> 'Coordinates':
        # source of the formula: https://www.movable-type.co.uk/scripts/latlong.html && https://chatgpt.com/c/67ab320e-8360-8002-9129-2d3daf88878a
        if (Radial < 0 or Radial > 360):
            raise ValueError("Radial must be between 0 and 360")
        if (DME < 0):
            raise ValueError("DME must be greater than 0")

        geograficRadial = 450 - Radial
        new_latitude = math.asin(math.sin(self.LatitudeRad) * math.cos(DME/60) + math.cos(self.LatitudeRad) * math.sin(DME/60) * math.cos(geograficRadial))
        new_longitude = self.LongitudeRad + math.atan2(math.sin(geograficRadial) * math.sin(DME/60) * math.cos(self.LatitudeRad), math.cos(DME/60) - math.sin(self.LatitudeRad) * math.sin(new_latitude))
        return Coordinates(new_latitude, new_longitude)

    def calculate_path(self, new_coordinates: 'Coordinates') -> Path:
        # Source Distance Calculation Harvesine Formula https://chatgpt.com/c/67ab320e-8360-8002-9129-2d3daf88878a
        a = math.sin((new_coordinates.LatitudeRad - self.LatitudeRad) / 2) ** 2 + math.cos(self.LatitudeRad) * math.cos(new_coordinates.LatitudeRad) * math.sin((new_coordinates.LongitudeRad - self.LongitudeRad) / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = 3440.065 * c
        # Source Heading Calculation  (Initial Bearing) Formula https://chatgpt.com/c/67ab320e-8360-8002-9129-2d3daf88878a
        phi = math.atan2(math.sin(new_coordinates.LongitudeRad - self.LongitudeRad) * math.cos(new_coordinates.LatitudeRad), math.cos(self.LatitudeRad) * math.sin(new_coordinates.LatitudeRad) - math.sin(self.LatitudeRad) * math.cos(new_coordinates.LatitudeRad) * math.cos(new_coordinates.LongitudeRad - self.LongitudeRad))
        heading = (phi * 180 / math.pi + 360) % 360

        return Path(heading, distance)


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
        self.DME = DME
        self.angle = angle
        self.Coordinates = Coordinates()

class Waypoint:
    def __init__(self, radial: Radial = None, waypoint_name: str = '') -> None:
        if radial is None or not waypoint_name:
            raise ValueError("Radial and WaypointName must be provided")
        self.Radial = radial
        self.WaypointName = waypoint_name
        self.Coordinates = Coordinates()

# Prueba
#tacan = Tacan(75, 'X', 270488, 29608)
#radial = Radial(tacan,269,59545.7)
#print(f"X Coordinates: {radial.XCoordinates}, Z Coordinates: {radial.ZCoordinates}")
tacan75x = Tacan(75, 'X', Coordinates(36.713, -6.349))