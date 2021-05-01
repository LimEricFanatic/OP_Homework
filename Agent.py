from Building import *
from ClassSchedule import ClassSchedule
import logging
import numpy as np
import time


class Agent:
    """工程师基类"""

    def __init__(self, grade, major, classSchedule, name="Agent", dorm=Dormitory()):
        self.name = name
        self.dorm = dorm
        self.position = dorm.position
        self.grade = grade
        self.major = major
        self.classSchedule = classSchedule
        self.classroomList = []

    def displayAgent(self):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Agent--------" +
            "\nName: " + self.name + 
            "\nPosition: " + str(self.position) +
            "\nDorm: " + self.dorm +
            "\nGrade: " + self.grade +
            "\nMajor: " +  self.major +
            "\nClassSchedule: " + str(self.classSchedule) +
            "\nClassroomList: " + str(self.classroomList)
            )

    def Copy(self):
        n_Agent = Agent()
        n_Agent.name = self.name
        n_Agent.dorm = self.dorm
        n_Agent.position = self.position
        n_Agent.grade = self.grade
        n_Agent.major = self.major
        n_Agent.classSchedule = self.classSchedule
        n_Agent.classroomList = self.classroomList      # list copy might wrong
        return n_Agent