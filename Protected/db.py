from . import Structures as Structures

class Afganistan:
    tacan75x = Structures.Tacan(75.00, 'X', Structures.Coordinates(Structures.dms_to_dd(31,30,20), Structures.dms_to_dd(65,50,54))) # Khandahar Afganistan
    tacan78x = Structures.Tacan(78.00, 'X', Structures.Coordinates(Structures.dms_to_dd(31,49,45), Structures.dms_to_dd(64,13,1)))  # Camp Bastion Afganistan

class Syria:
    tacan21x = Structures.Tacan(21.00, 'X', Structures.Coordinates(Structures.dms_to_dd(37,00,56), Structures.dms_to_dd(35,26,53))) # Incirlick Turkey
    tacan107x = Structures.Tacan(107.00, 'X', Structures.Coordinates(Structures.dms_to_dd(34,34,35), Structures.dms_to_dd(32,57,46))) # Acrotiri Airport
    tacan84x = Structures.Tacan(84.00, 'X', Structures.Coordinates(Structures.dms_to_dd(32,39,58), Structures.dms_to_dd(35,11,2))) # Ramat David
class ColdWarGermany:
    tacan89x = Structures.Tacan(89.00, 'X', Structures.Coordinates(Structures.dms_to_dd(50, 3, 13), Structures.dms_to_dd(8, 38, 13))) # Ramstein AFB