import time

class Major:
    """Type Major"""
    majorCount = 0

    def __init__(self, index, department, major, population):
        self.index = index
        self.department = department
        self.major = major
        self.population = population
        Major.majorCount += 1

    def displayMajorCount(self):
        logging.debug(
            "Current Major Num: %d" % Major.majorCount
        )

    def displayMajor(self):
        logging.debug(
            "Log TIME: " + time.time() +
            "--------Major--------" +
            "\nIndex: " + self.index + 
            "\nDepartment: " + self.department +
            "\nMajor: " + self.major +
            "\nPopulation: " + self.population
            )