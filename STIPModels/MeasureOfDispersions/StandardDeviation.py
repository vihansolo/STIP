from statistics import stdev

class StandardDeviation() :

    def __init__(self) :
        pass
    
    def calculateStandardDeviation(self, inputData = []) :
        return stdev(inputData)
