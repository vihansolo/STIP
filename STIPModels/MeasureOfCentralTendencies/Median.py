class Median() :

    def __init__(self) :
        pass

    def calculateMedian(self, inputData = []) :

        if (len(inputData) % 2) != 0 :
            return inputData[int(len(inputData) / 2)]

        else :
            return (inputData[int(len(inputData) / 2) - 1] + inputData[int((len(inputData) / 2) + 1) - 1]) / 2
