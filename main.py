from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange
from STIPModels.RegressionAnalysis import LinearRegression, NonLinearRegression
from STIPModels.Forecasting import Forecasting
from STIPModels.HypothesisAnalysis import StudentTTest, PairedTTest

inputData = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]
input2DData = [(1,5), (2,4), (3,6), (4,5), (5,6), (6,7)]

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
LinearRegression.LinearRegression().calculateLinearRegression(input2DData)

# NonLinear Regression

print()
print('Non Linear Regression : ')
print()
NonLinearRegression.NonLinearRegression().calculateNonLinearRegression()

# Forecasting

print()
print('Forecasting :')
print()
Forecasting.Forecasting().calculateForecasting()

# Hypothesis Analysis

# Student T-Test

print()
print('Student T-Test : ')
print()
StudentTTest.StudentTTest().calculateStudentTTest(input2DData)

# Paired T-Test

print()
print('Paired T-Test : ')
print()
PairedTTest.PairedTTest().calculatePairedTTest(input2DData)
