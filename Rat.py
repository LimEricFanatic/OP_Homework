import numpy
import random
import logging
from Chrome import Chrome


class Rat:
    ratCount = 0

    def __init__(self, env):
        self.name = "RAT" + str(Rat.ratCount)
        self.chrome_list = []
        self.env = env
        self.fitness = 0
        self.relative_fitness = 0
        self.accumulation_probability = 0
        Rat.ratCount += 1

    def Copy(self):  # 在复制时可以考虑将 Initialize 删去
        n_Rat = Rat(self.env)
        for chrome in self.chrome_list:
            n_Chrome = chrome.Copy()
            n_Rat.chrome_list.append(n_Chrome)
        n_Rat.fitness = self.fitness
        n_Rat.relative_fitness = self.relative_fitness
        n_Rat.accumulation_probability = self.accumulation_probability
        return n_Rat

    def Initialize(self, depot_num, factory_num, agent_num, env):
        logging.debug("Rat Initialize begin!")
        for i in range(self.env.agent_num):
            self.chrome_list.append(Chrome(i))
        init_agent_list = list(range(0, agent_num))
        init_factory_list = list(range(0, factory_num))
        random.shuffle(init_factory_list)
        logging.debug("init allocate start!")
        while len(init_factory_list) != 0:
            test_factory = init_factory_list[0]
            test_agent = random.choice(init_agent_list)
            test_chrome = self.chrome_list[test_agent]
            if test_chrome.init_check(test_agent, test_factory, env):
                test_chrome.gene_list.append(test_factory)
                del init_factory_list[0]
                logging.debug("Factory 0%d has been allocated to Agent 0%d." % (test_factory, test_agent))
        self.Fitness_calculation()
        logging.debug("Rat Initialize Done!")

    def Delete_redundant_element(self, compare_list, chrome_number):
        logging.debug("Delete_redundant_element Begin!")
        for chrome in self.chrome_list:
            if chrome.agent_number != chrome_number:
                chrome.Delete_redundant_element(compare_list)
        logging.debug("Delete_redundant_element Done!")

    def Insert_element(self, insert_list):
        logging.debug("Crossover Insert Begin!")
        while len(insert_list) != 0:
            test_factory = insert_list[0]
            test_agent = random.choice(range(self.env.agent_num))
            test_chrome = self.chrome_list[test_agent]
            test_index = random.choice(range(len(test_chrome.gene_list) + 1))
            if test_chrome.cross_check(test_agent, test_factory, test_index, self.env):  # 检查但不插入
                test_chrome.gene_list.insert(test_index, test_factory)
                del insert_list[0]
                logging.debug(
                    "Factory 0%d has been allocated to Agent 0%d in index %d" % (test_factory, test_agent, test_index))
        logging.debug("Crossover Insert Done!")

    def Mutate(self, mutate_rate):
        mutate_list = []
        for chrome in self.chrome_list:
            chrome.Mutate(mutate_list, mutate_rate)
        self.Insert_element(mutate_list)
        # logging.debug("After insert, Mutation Box is clear?\t" + str(bool(not len(mutate_list))))

    def Fitness_calculation(self):
        """适应度计算"""
        self.fitness = 0
        for chrome in self.chrome_list:
            if len(chrome.gene_list) == 0:  # 未安排行程
                chrome.cost = 0
                chrome.work_duration = 0
                chrome.travel_distance = 0
                chrome.path = []
                continue
            self.fitness += chrome.Cost_calculation(self.env)

    def Relative_fitness_calculation(self, pop_fitness_max, pop_fitness_min, avg_cost):
        self.relative_fitness = (pop_fitness_max - self.fitness + avg_cost) / (
                    pop_fitness_max - pop_fitness_min + avg_cost)
        return self.relative_fitness

    def Display_log(self):
        logging.debug("---Rat Display---(%s)" % str(self.name))
        for chrome in self.chrome_list:
            name_list = []
            for building in chrome.path:
                name_list.append(str(building))
            logging.debug("Agent %s\tPlan %s\t Work duration: %s\t Travel Distance: %s" % (str(chrome.agent_number), str(name_list), str(chrome.work_duration), str(chrome.travel_distance)))
        logging.debug("Total Cost %f" % self.fitness)

    def Display(self):
        print("---Rat Display---(%s)" % str(self.name))
        for chrome in self.chrome_list:
            name_list = []
            meet_position_list = []
            for building in chrome.path:
                name_list.append(str(building))
            for position in chrome.meet_position:
                meet_position_list.append(str(position))
            print("Agent %s\tPlan %s\t Work duration: %s\t Travel Distance: %s" % (str(chrome.agent_number), str(name_list), str(chrome.work_duration), str(chrome.travel_distance)))
            print("Agent %s\tMEET position: %s" % (str(chrome.agent_number), str(meet_position_list)))
        print("Cost %f" % self.fitness)

    def BestRatDisplay_log(self):
        logging.debug("---Best Rat Display---(%s)" % str(self.name))
        for chrome in self.chrome_list:
            name_list = []
            meet_position_list = []
            for building in chrome.path:
                name_list.append(str(building))
            for position in chrome.meet_position:
                meet_position_list.append(str(position))
            logging.debug("Agent %s\tPlan %s\t Work duration: %s\t Travel Distance: %s" % (str(chrome.agent_number), str(name_list), str(chrome.work_duration), str(chrome.travel_distance)))
            logging.debug("Agent %s\tMEET position: %s" % (str(chrome.agent_number), str(meet_position_list)))
        logging.debug("Total Cost %f" % self.fitness)