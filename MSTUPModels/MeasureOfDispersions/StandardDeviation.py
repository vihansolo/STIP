from statistics import stdev
import math

class StandardDeviation() :

    def __init__(self) :
        pass
    
    def calculateStandardDeviation(self, inputData = []) :
        return stdev(inputData)
