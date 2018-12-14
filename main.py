from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange

inputData = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]

# Measure of Central Tendencies

# Mean

print()
print('Mean =',Mean.Mean().calculateMean(inputData))

# Median

print()
print('Median =',Median.Median().calculateMedian(inputData))

# Mode

print()

try :
    print('Mode =',Mode.Mode().calculateMode(inputData))

except :
    print('Multiple Modes found')

# Measure of Dispersion

# Variance

print()
print('Variance =',Variance.Variance().calculateVariance(inputData))

# Standard Deviation

print()
print('Standard Deviation =',StandardDeviation.StandardDeviation().calculateStandardDeviation(inputData))

# Interquartile Range

print()
print('Interquartile Range =',InterquartileRange.InterquartileRange().calculateInterquartileRange(inputData))
