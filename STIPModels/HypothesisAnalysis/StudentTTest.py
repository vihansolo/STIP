from scipy.stats import ttest_ind

class StudentTTest() :

    def __init__(self) :
        pass

    def calculateStudentTTest(self, input2DData = []) :

        x = [x for x, y in input2DData]
        y = [y for x, y in input2DData]

        stat, p = ttest_ind(x, y)

        return stat, p
