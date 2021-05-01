import logging
import time
from Point2D import Point2D


class Building:
    """所有地点的基类"""
    buildingCount = 0

    def __init__(self, name="Building", position=Point2D(0, 0)):
        self.name = name
        self.position = position
        Building.buildingCount += 1

    def __str__(self):
        return self.name

    def displayCount(self):
        logging.debug("Total Building Count: %d" % Building.buildingCount)

    def displayBuilding(self, time):
        logging.debug("Name: " + self.name + ", Position: " + str(self.position))

class Dormitory(Building):
    """ Type Dormitory"""

    def __init__(self, dorm_index="-1", area="SJTU", name="Dormitory", position=Point2D(0, 0)):
        Building.__init__(self, name, position)
        self.dorm_index = dorm_index
        self.area = area

    def displayBuilding(self):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Dormitory--------" +
            "\nName: " + self.name + 
            "\nPosition: " + str(self.position) +
            "\nDorm Index: " + self.dorm_index +
            "\nArea: " + self.area
            )

class Classroom(Building):
    """Type Classroom"""

    def __init__(self, capacity=0, classroom_index="-1", area="SJTU", name="Classroom", position=Point2D(0, 0)):
        Building.__init__(self, name, position)
        self.classroom_index = classroom_index
        self.area = area
        self.capacity = capacity

    def displayBuilding(self, time):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Dormitory--------" +
            "\nName: " + self.name + 
            "\nPosition: " + str(self.position) +
            "\nClassroom Index: " + self.classroom_index +
            "\nArea: " + self.area +
            "\nCapacity: " + self.capacity
            )