import logging
import time
from Point2D import Point2D


class Building:
    """所有地点的基类"""
    buildingCount = 0

    def __init__(self, index=-1, name="Building", position=Point2D(0, 0)):
        self.index = index
        self.name = name
        self.position = position
        Building.buildingCount += 1

    def __str__(self):
        return self.name

    def displayCount(self):
        logging.debug("Total Building Count: %d" % Building.buildingCount)

    def displayBuilding(self, time):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Building--------" +
            "\nName: " + self.name + 
            "\nPosition: " + str(self.position) +
            "\nIndex: " + self.index
            )

class Dormitory(Building):
    """ Type Dormitory"""

    def __init__(self, index=-1, name="Dormitory", position=Point2D(0, 0)):
        Building.__init__(self, index, name, position)

    def displayBuilding(self):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Dormitory--------" +
            "\nName: " + self.name + 
            "\nPosition: " + str(self.position) +
            "\nDorm Index: " + self.index
            )

class Classroom(Building):
    """Type Classroom"""

    def __init__(self, index=-1, name="Classroom", area="SJTU", capacity=0, position=Point2D(0, 0)):
        Building.__init__(self, index, name, position)
        self.area = area
        self.capacity = capacity

    def displayBuilding(self, time):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Classroom--------" +
            "\nName: " + self.name + 
            "\nPosition: " + str(self.position) +
            "\nClassroom Index: " + self.index +
            "\nArea: " + self.area +
            "\nCapacity: " + self.capacity
            )