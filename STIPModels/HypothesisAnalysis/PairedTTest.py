from scipy.stats import ttest_rel

class PairedTTest() :

    def __init__(self) :
        pass

    def calculatePairedTTest(self, input2DData = []) :

        x = [x for x, y in input2DData]
        y = [y for x, y in input2DData]

        stat, p = ttest_rel(x, y)

        return stat, p
