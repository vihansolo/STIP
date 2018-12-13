class Median() :

    def __init__(self) :
        pass

    def calculateMedian(self, inputData = []) :

        if (len(inputData) % 2) != 0 :
            return inputData[len(inputData) // 2]

        else :
            return (inputData[len(inputData) // 2] + inputData[(len(inputData) // 2) - 1]) / 2
