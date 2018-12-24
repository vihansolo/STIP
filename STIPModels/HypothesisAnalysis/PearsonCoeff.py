from scipy.stats import pearsonr

class PearsonCoeff() :

    def __init__(self) :
        pass

    def calculateCorrelationCoefficient(self, input2DData = []) :

        x = [x for x, y in input2DData]
        y = [y for x, y in input2DData]

        corr, p = pearsonr(x, y)

        print('\tCorr :',corr)
        print('\tP :',p)
