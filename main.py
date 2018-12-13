from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange

inputData = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]

# Measure of Central Tendencies

# Mean

print()
meanObject = Mean.Mean()
print('Mean =',meanObject.calculateMean(inputData))

# Median

print()
medianObject = Median.Median()
print('Median =',medianObject.calculateMedian(inputData))

# Mode

print()
modeObject = Mode.Mode()

try :
    print('Mode =',modeObject.calculateMode(inputData))

except :
    print('Multiple Modes found')

# Measure of Dispersion

# Variance

print()
varianceObject = Variance.Variance()
print('Variance =',varianceObject.calculateVariance(inputData))

# Standard Deviation

print()
standardDeviationObject = StandardDeviation.StandardDeviation()
print('Standard Deviation =',standardDeviationObject.calculateStandardDeviation(inputData))

# Interquartile Range

print()
interquartileRangeObject = InterquartileRange.InterquartileRange()
print('Interquartile Range =',interquartileRangeObject.calculateInterquartileRange(inputData))
