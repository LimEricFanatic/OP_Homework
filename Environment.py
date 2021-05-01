from Building import *
from Agent import *
from Point2D import *

import logging


class Environment:
    def __init__(self):
        self.dorm_list = []
        self.classroom_list = []
        self.agent_list = []
        self.notFullRoom = {}       # {'class_index': classroom_index}
        self.dorm_num = 0
        self.classroom_num = 0
        self.agent_num = 0

        self.avg_cost = 0       #平均固定成本

    def Initialize(self):
        self.depot_list.append(Depot("Depot00", Point2D(100, 100)))
        self.depot_list.append(Depot("Depot01", Point2D(-100, -100)))

        self.factory_list.append(Factory("Factory00", Point2D(0, 10), 3, Point2D(0, 1), 5, 10, 10, 1))
        self.factory_list.append(Factory("Factory01", Point2D(-62, 90), 1, Point2D(2, 1), 5, 20, 30, 1))
        self.factory_list.append(Factory("Factory02", Point2D(3, 67), 1, Point2D(-3, -1), 5, 20, 0, 1))
        self.factory_list.append(Factory("Factory03", Point2D(44, 24), 1, Point2D(4, 11), 5, 20, 50, 1))
        self.factory_list.append(Factory("Factory04", Point2D(5, 34), 2, Point2D(15, -13), 5, 15, 20, 1))
        self.factory_list.append(Factory("Factory05", Point2D(-40, 10), 2, Point2D(6, -12), 5, 15, 5, 1))

        self.agent_list.append(GoodAgent("Agent00", self.depot_list[0]))
        self.agent_list.append(BadAgent("Agent01", self.depot_list[0]))

        self.dorm_num = len(self.dorm_list)
        self.classroom_num = len(self.classroom_list)
        self.agent_num = len(self.agent_list)

        self.avg_cost = self.Average_cost_calculation()

        logging.info("Environment Initialize Done!")

    # def Average_cost_calculation(self):
    #     """计算平均固定成本"""
    #     cost_sum = 0
    #     for agent in self.agent_list:
    #         cost_sum += agent.repair_cost
    #     avg = cost_sum / self.agent_num
    #     return avg

    def displayEnvironment(self):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Environment--------" +
            "\nDorm Num: " + self.dorm_num + 
            "\nAgent Num: " + self.agent_num +
            "\nClassroom Num: " + self.classroom_num +
            "\nNot Full Room: " + str(self.notFullRoom)
            )
