from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation

inputData = [1, 1, 2, 3, 3, 3, 3, 4]

print()
meanObject = Mean.Mean()
print('Mean =',meanObject.calculateMean(inputData))
print()
medianObject = Median.Median()
print('Median =',medianObject.calculateMedian(inputData))
print()
modeObject = Mode.Mode()
print('Mode =',modeObject.calculateMode(inputData))
print()
varianceObject = Variance.Variance()
print('Variance =',varianceObject.calculateVariance(inputData))
print()
standardDeviationObject = StandardDeviation.StandardDeviation()
print('Standard Deviation =',standardDeviationObject.calculateStandardDeviation(inputData))
