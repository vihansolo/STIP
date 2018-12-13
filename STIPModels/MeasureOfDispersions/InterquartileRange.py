from STIPModels.MeasureOfCentralTendencies import Median

class InterquartileRange() :

    def __init__(self) :
        pass

    def calculateInterquartileRange(self, inputData = []) :
        
        midIndex = len(inputData) // 2
        firstHalf = inputData[:midIndex]

        if (len(inputData) % 2) != 0 :            
            secondHalf = inputData[midIndex + 1:]

        else :
            secondHalf = inputData[midIndex:]

        return Median.Median.calculateMedian(self,secondHalf) - Median.Median.calculateMedian(self,firstHalf)
