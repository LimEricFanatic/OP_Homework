import matplotlib
import logging
import myLog
import numpy as np
import random
import time
import matplotlib.pyplot as plt

from tqdm import tqdm
from tqdm._tqdm import trange

from Environment import Environment
from Rat import Rat
from Chrome import Chrome


class GASA:
    """Gene Arithmetic"""

    def __init__(self, env, pop_size, max_gen, cross_rate, mutate_rate, T_max, T_min, SA_rate):
        self.env = env
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.cross_rate = cross_rate
        self.mutate_rate = mutate_rate
        self.T_max = T_max
        self.T_min = T_min
        self.SA_rate = SA_rate

        self.rat_list = []
        self.rat_best = Rat(self.env)
        self.best_cost_list = []
        self.best_in_history = Rat(self.env)

    def Run(self):
        """execute function"""
        random.seed()
        self.Initialize(self.max_gen, self.env)
        for i in trange(self.max_gen):
            time.sleep(0.01)
            # logging.info("\n------This is the %d generation------" % i)
            random.shuffle(self.rat_list)
            self.Crossover_and_Mutation()
            # self.Select()
            self.Elite_select()
            self.rat_best.BestRatDisplay_log()

    def Display(self):
        """display function"""
        print("POP SIZE: %d" % (len(self.rat_list)))
        print("---Best Rat---")
        self.best_in_history.Display()
        self.best_in_history.Display_log()


        # Pyplot制图
        plt.figure(("遗传算法收敛图"))
        x1 = np.arange(1, self.max_gen+1)
        y1 = self.best_cost_list
        plt.title("GA Best Fitness Curve")
        plt.plot(x1, y1)

        plt.figure("路径图")
        colorlist= ["blue", "green", "yellow", "purple", "black"]
        depot_colorlist = ["navy","brown","deeppink"]
        markers = ["D", "x", "h", ".", "^", ">", "v"]
        for i in range(len(self.env.depot_list)):
            print("%s\t%s" % (self.env.depot_list[i].position.x, self.env.depot_list[i].position.y))
            plt.scatter(self.env.depot_list[i].position.x, self.env.depot_list[i].position.y, color=depot_colorlist[i], s=200, label="Depot" +str(i))
        x_list = []
        y_list = []
        label_list = []
        for chrome in self.rat_best.chrome_list:
            label_list.append(chrome.agent_number)
            n_list_x = []
            n_list_y = []
            n_list_x.append(self.env.agent_list[chrome.agent_number].start_depot.position.x)
            n_list_y.append(self.env.agent_list[chrome.agent_number].start_depot.position.y)
            for pos in chrome.meet_position:
                n_list_x.append(pos.x)
                n_list_y.append(pos.y)
            x_list.append(n_list_x)
            y_list.append(n_list_y)
        for i in range(len(label_list)):
            for j in range(len(x_list[i])):
                # print(str(x_list[i][j]) + "\t" +str(y_list[i][j]) + "\t" + str(x_list[i][j+1]) + "\t" + str(y_list[i][j+1]))
                plt.arrow(x_list[i][j], y_list[i][j], x_list[i][j+1]-x_list[i][j], y_list[i][j+1]-y_list[i][j],head_width=3, lw=2, color=colorlist[i])
                plt.text(x_list[i][j], y_list[i][j], s=j, fontsize=8, color='red')  # ⽂本
                if j == len(x_list[i])-2:
                    # plt.text(x_list[i][j], y_list[i][j], s=j, fontsize=8, color='red')  # ⽂本
                    break
        plt.legend()

        plt.show()

    def Initialize(self, max_gen, env):
        # logging.info("------Initialize begin------")
        for i in range(self.pop_size):
            rat = Rat(env)
            rat.Initialize(self.env.dorm_num, self.env.classroom_num, self.env.agent_num, self.env)
            self.rat_list.append(rat)
        self.best_in_history = self.rat_list[0].Copy()
        self.best_in_history.Fitness_calculation()

    def Crossover_and_Mutation(self):
        logging.debug("------Crossover and Mutate begin------")
        rat_num = len(self.rat_list)
        T = self.T_max
        while T >= self.T_min:
            logging.debug("Temperature MAX\t now %f" % T)
            # crossover
            for i in range(rat_num-1):
                j = i + 1
                if random.random() < self.cross_rate:
                    logging.debug("Total Rat is %d\tRatA index %d\tRatB index %d" % (len(self.rat_list), i, j))
                    self.Crossover(self.rat_list[i], self.rat_list[j], T, i, j)
            # mutate
            for i in range(rat_num):
                if random.random() < self.mutate_rate:
                    logging.debug("Mutate Index:%d" % i)
                    self.Mutate(self.rat_list[i], T, i)
            T *= self.SA_rate
            logging.debug("Now Temperature is %f" % T)
        logging.debug("Temperature < T_min, SA END")

    def Crossover(self, rat_A, rat_B, T, index_a, index_b):
        """对A，B个体进行操作，注意要改变个体本身，不产生新个体"""








        
        logging.debug("---Crossover Begin---(%s, %s)" % (rat_A.name, rat_B.name))
        chrome_number = random.choice(range(self.env.agent_num))
        n_rat_A = rat_A.Copy()
        n_rat_B = rat_B.Copy()
        a = n_rat_A.chrome_list[chrome_number]
        b = n_rat_B.chrome_list[chrome_number]
        a.Display_log()
        b.Display_log()
        if len(a.gene_list) == 0 and len(b.gene_list) == 0:
            logging.debug("No gene exist in these chromes, RETRY!")
            return
        F_ab = [x for x in a.gene_list if x in b.gene_list]
        F_a = [y for y in a.gene_list if y not in F_ab]
        F_b = [z for z in b.gene_list if z not in F_ab]
        logging.debug("F_ab:" + str(F_ab) + "\tF_a:" + str(F_a) + "\tF_b:" + str(F_b))

        logging.debug("Before Duplicate, rat num is: %d, following is RatA, RatB" % len(self.rat_list))
        rat_A.Display_log()
        rat_B.Display_log()

        logging.debug("After Duplicate, rat num is: %d" % len(self.rat_list))

        logging.debug("---Before Switch--- (A,B)")
        n_rat_A.chrome_list[chrome_number].Display_log()
        n_rat_B.chrome_list[chrome_number].Display_log()
        tmp = a.Copy()
        n_rat_A.chrome_list[chrome_number] = n_rat_B.chrome_list[chrome_number].Copy()
        n_rat_B.chrome_list[chrome_number] = tmp
        logging.debug("---After Switch--- (A,B)")
        n_rat_A.chrome_list[chrome_number].Display_log()
        n_rat_B.chrome_list[chrome_number].Display_log()

        n_rat_A.Delete_redundant_element(F_b, chrome_number)
        n_rat_B.Delete_redundant_element(F_a, chrome_number)

        n_rat_A.Insert_element(F_a)
        n_rat_B.Insert_element(F_b)

        logging.debug("RatA, RatB, newRatA, newRatB")
        rat_A.Display_log()
        rat_B.Display_log()
        n_rat_A.Display_log()
        n_rat_B.Display_log()

        self.rat_list[index_a] = self.SA_deal(rat_A, n_rat_A, T)
        self.rat_list[index_b] = self.SA_deal(rat_B, n_rat_B, T)

    def Mutate(self, rat, T, index):
        logging.debug("------RAT Mutate Begin------(%s)" % rat.name)
        n_rat = rat.Copy()
        n_rat.Mutate(self.mutate_rate)
        self.rat_list[index] = self.SA_deal(rat, n_rat, T)

    # def Select(self):
    #     if len(self.rat_list) == 0:
    #         logging.error("No rat survive!")
    #         exit()
    #     for rat in self.rat_list:
    #         rat.Fitness_calculation()
    #     pop_fitness_max = self.rat_list[0].fitness
    #     pop_fitness_min = self.rat_list[0].fitness
    #     for rat in self.rat_list:
    #         if rat.fitness > pop_fitness_max:
    #             pop_fitness_max = rat.fitness
    #             break
    #         if rat.fitness < pop_fitness_min:
    #             pop_fitness_min = rat.fitness
    #             break

    #     relative_fitness_sum = 0
    #     for rat in self.rat_list:
    #         tmp = rat.Relative_fitness_calculation(pop_fitness_max, pop_fitness_min, self.env.avg_cost)
    #         relative_fitness_sum += tmp

    #     prob_sum = 0
    #     for rat in self.rat_list:
    #         prob_sum += rat.relative_fitness
    #         rat.accumulation_probability = prob_sum / relative_fitness_sum

    #     n_rat_list = []
    #     for i in range(self.pop_size):
    #         select_prob = random.random()
    #         logging.debug("select_prob is %f" % select_prob)
    #         for j in range(len(self.rat_list)):
    #             if self.rat_list[j-1].accumulation_probability < select_prob <= self.rat_list[j].accumulation_probability:
    #                 logging.debug("The %d Rat is selected. It's accumulation_probability is %f, Former one is %f" % (
    #                     j, self.rat_list[j].accumulation_probability, self.rat_list[j-1].accumulation_probability))
    #                 n_rat_list.append(self.rat_list[j])
    #                 logging.debug("New Rat List has %d members." % len(n_rat_list))
    #                 break
    #     self.rat_list = n_rat_list

    def Elite_select(self):
        best_index = 0
        worst_index = 0
        logging.debug("Before Elite select, Survive Rat Num: %d" % len(self.rat_list))
        pop_fitness_min = self.rat_list[0].fitness
        pop_fitness_max = self.rat_list[0].fitness
        for i in range(len(self.rat_list)):
            if self.rat_list[i].fitness < pop_fitness_min:
                pop_fitness_min = self.rat_list[i].fitness
                best_index = i
                break
            if self.rat_list[i].fitness > pop_fitness_max:
                pop_fitness_max = self.rat_list[i].fitness
                worst_index = i
                break
        logging.debug("The best index %d\tCost is: %f\nThe worst index %d\tCost is: %f" % (\
            best_index, self.rat_list[best_index].fitness, worst_index, self.rat_list[worst_index].fitness))
        logging.debug("Before replace, rat num is %d" % len(self.rat_list))
        self.rat_best = self.rat_list[best_index].Copy()
        del self.rat_list[worst_index]
        logging.debug("After Delete, rat num is %d" % len(self.rat_list))
        self.rat_list.append(self.rat_best)
        self.best_cost_list.append(self.rat_best.fitness)
        logging.debug("After replace, rat num is %d" % len(self.rat_list))
        if self.rat_best.fitness < self.best_in_history.fitness:
            self.best_in_history = self.rat_best.Copy()
            logging.debug("Better RAT appear!")
            self.best_in_history.Display_log

    def SA_deal(self, parent_rat, son_rat, T):
        logging.debug("SA_deal. Parent: %s\t Son: %s" % (parent_rat.name, son_rat.name))
        parent_rat.Fitness_calculation()
        son_rat.Fitness_calculation()
        delta = parent_rat.fitness - son_rat.fitness
        logging.debug("Delta: %s\tParent: %s\tSon: %s" % (delta,parent_rat.fitness,son_rat.fitness))
        if delta > 0:
            logging.debug("Delta > 0, Replace!")
            del parent_rat
            return son_rat
        else:
            logging.debug("Delta < 0, Prob!")
            prob = np.exp(delta / T)
            if prob > random.random():
                logging.debug("Prob YES, Replace!")
                del parent_rat
                return son_rat
            else:
                logging.debug("Prob NO, Reserve!")
                del son_rat
                return parent_rat


    # def Test(self):
