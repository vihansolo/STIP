class Mean() :

    def __init__(self) :
        pass

    def calculateMean(self, inputData = []) :

        self.output = 0

        for x in inputData :
            self.output += x

        return self.output / len(inputData)
