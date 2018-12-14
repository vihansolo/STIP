from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange
from STIPModels.RegressionAnalysis import LinearRegression

inputData = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]
x_array =  [1, 2, 3, 4, 5, 6]
y_array = [5, 4, 6, 5, 6, 7]

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

# Regression Analysis

# Linear Regression

print()
print('Linear Regression : ')
LinearRegression.LinearRegression().calculateLinearRegression(x_array,y_array)
