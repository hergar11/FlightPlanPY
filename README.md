Software to create Flight Plans. Oriented specially in planes that does not have GPS and requires TACAN, RADIAL, Heading, to navigate
NOTE DO Not change files in Protected
# How to Run
Firts time running the script please run [FritsRun.bat] then do proper modifications and run [Run.bat]
**How to use:**
The software defines the waypoint as a displacement from a Tacan(Radial+DME).
How to create a Tacan { Tacan(Freq, Letter, Coordinates(dms_to_dd(), dms_to_dd())) }:
    - To create a Tacan you need to fill the following values: TacanFreq(Number) TacanLetter(Text) Coordinates. Internally Coordinates are using a      custom structure that will pack latitude & longitude. The units used for latitude & longitude are Degress.Decimals, to help the user dms_to_dd is created, this function will take as an input the latitude/lognitude as Degress,Minutes,Seconds. ** Note to indicate S or W coordinates ar negative**
    Example of how to create a Tacan:
        Tacan(75.00, 'X', Coordinates(dms_to_dd(31,30,20), dms_to_dd(65,50,54))). The previous tacan will be set in 75X and placed in 31.30.20N 65.50.54E
    Some tacans are already saved in a DataBase. This database is located in Protected/db.py. 

Example of how to create a Radial { Radial(Tacan, Radial, DME) }:
    - Radial is the name for the spatial point that where will be placed the waypoint. This Radial is defined by a Tacan, Radial(degress), DME(nm)
    Radial will be a point displaced Radial(degress) and DME(nm) from the coordinates of Tacan

Example of how to create a Waypoint:
    - A waypoint is bassically a radial with a name. So each Waypoint will require a Radial and a Name.

Example of how to create a FlightPlan { Flihtplan(Name, Waypoints) }:
    - A flightplan will require a name and a list of Waypoints.

Example of how to output a FlighPlan:
    -Run FlighPlan.get_flightplan() and output.txt will appear in your current directory with the whole flightplan.
    Note flightplan can take a bool(True/False) as an input. As a defalut is True.
    If True is given, flightplan will show go and return.
    If False is given, flightplan will show just go.





**Example Of Use:**


    tacan75x = Tacan(75.00, 'X', Coordinates(dms_to_dd(31,30,20), dms_to_dd(65,50,54)))
    tacan78x = Tacan(78.00, 'X', Coordinates(dms_to_dd(31,49,45), dms_to_dd(64,13,1)))
    Waypoint0 = Waypoint(Radial(tacan75x, 0, 0), 'Kandahar')
    Waypoint1 = Waypoint(Radial(tacan75x, 269, 37), 'ADDER')
    Waypoint2 = Waypoint(Radial(tacan78x, 291, 39), 'Bravo')
    Waypoint3 = Waypoint(Radial(tacan78x, 278, 105), 'Charlie')
    Waypoint4 = Waypoint(Radial(tacan78x, 287, 109), 'TGT2')

    flightplan = Flihtplan('Test', [Waypoint0, Waypoint1, Waypoint2, Waypoint3, Waypoint4])
    flightplan.get_flightplan() #This few lines will create the flight plan with all the required heading distances to go to target and to return.
