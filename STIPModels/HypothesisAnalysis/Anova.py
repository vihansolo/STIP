from scipy.stats import f_oneway

class Anova() :

    def __init__(self) :
        pass

    def calculateANOVA(self, input2DData = []) :

        x = [x for x, y in input2DData]
        y = [y for x, y in input2DData]

        stat, p = f_oneway(x, y)

        return stat, p
