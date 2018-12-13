from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange

inputData = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]

print()
meanObject = Mean.Mean()
print('Mean =',meanObject.calculateMean(inputData))

print()
medianObject = Median.Median()
print('Median =',medianObject.calculateMedian(inputData))

print()
modeObject = Mode.Mode()
try :
    print('Mode =',modeObject.calculateMode(inputData))
except :
    print('Multiple Modes found')

print()
varianceObject = Variance.Variance()
print('Variance =',varianceObject.calculateVariance(inputData))

print()
standardDeviationObject = StandardDeviation.StandardDeviation()
print('Standard Deviation =',standardDeviationObject.calculateStandardDeviation(inputData))

print()
interquartileRangeObject = InterquartileRange.InterquartileRange()
print('Interquartile Range =',interquartileRangeObject.calculateInterquartileRange(inputData))
