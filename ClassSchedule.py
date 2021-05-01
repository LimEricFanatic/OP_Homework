import numpy as np

class ClassSchedule:
    """ClassSchedule Type"""

    def __init__(self, class_matrix, ):
        if class_matrix.size != 25:
            logging.debug("Class Matrix Size Wrong! Size = %d", class_matrix.size)
            exit()
        self.classSchedule = np.zeros([5,5])
        self.dorm = dorm
        self.position = dorm.position
        self.grade = grade
        self.major = major
        self.classSchedule = classSchedule