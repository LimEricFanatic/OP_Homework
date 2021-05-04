from Building import *
from ClassSchedule import ClassSchedule
import logging
import numpy as np
import time


class Agent:
    """工程师类"""

    def __init__(self, agent_index, major_index, dorm_index, class_table=[]):
        self.agent_index = agent_index
        self.major_index = major_index
        self.dorm_index = dorm_index
        self.class_table = class_table      # [25 items]
        self.path = []     # [25 items] -> -1:dorm 0-...:classroom

    def displayAgent(self):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Agent--------" +
            "\nAgent Index: " + self.agent_index + 
            "\nMajor Index: " + self.major_index +
            "\nDorm Index: " + self.dorm_index +
            "\nClass Table: " + str(self.class_table) +
            "\nPath: " +  str(self.path) 
            )

    def Copy(self):
        n_Agent = Agent()
        n_Agent.agent_index = self.agent_index
        n_Agent.major_index = self.major_index
        n_Agent.dorm_index = self.dorm_index
        n_Agent.class_table = self.class_table      # array copy might wrong
        if len(n_Agent.classroomList) != 0:
            logging.debug("New Agent Classroom List is not Empty!")
            exit()
        for classroom in self.classroomList:
            n_Agent.classroomList.append(classroom)
        return n_Agent