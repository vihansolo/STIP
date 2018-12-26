from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange
from STIPModels.RegressionAnalysis import LinearRegression, NonLinearRegression
from STIPModels.Forecasting import Forecasting
from STIPModels.HypothesisAnalysis import StudentTTest, PairedTTest, Anova, ChiSquared, PearsonCoeff
import numpy as np

inputData = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]
input2DData = [(1,5), (2,4), (3,6), (4,5), (5,6), (6,7)]
chiData = np.array([[1,3,4],[2,4,5],[5,3,4],[8,5,1]])

print()
print('Enter Choice :')
print()
print('1. Measure of Central Tendencies')
print('2. Measure Of Dispersions')
print('3. Regression Analysis')
print('4. Forecasting')
print('5. Hypothesis Analysis')
print()

choice = int(input('Enter Choice : '))
print()

if choice == 1 :

    # Measure of Central Tendencies

    print('Enter choice : ')
    print()
    print('1. Mean')
    print('2. Median')
    print('3. Mode')
    print()

    choice = int(input('Enter Choice : '))
    print()

    if choice == 1 :

        # Mean
        print('Mean =',Mean.Mean().calculateMean(inputData))

    if choice == 2 :

        # Median
        print('Median =',Median.Median().calculateMedian(inputData))

    if choice == 3 :

        # Mode
        try :
            print('Mode =',Mode.Mode().calculateMode(inputData))

        except :
            print('Multiple Modes found')

if choice == 2 :

    # Measure of Dispersion

    print('Enter choice : ')
    print()
    print('1. Variance')
    print('2. Standard Deviation')
    print('3. Interquartile Range')
    print()

    choice = int(input('Enter Choice : '))
    print()

    if choice == 1 :

        # Variance
        print('Variance =',Variance.Variance().calculateVariance(inputData))

    if choice == 2 :

        # Standard Deviation
        print('Standard Deviation =',StandardDeviation.StandardDeviation().calculateStandardDeviation(inputData))

    if choice == 3 :

        # Interquartile Range
        print('Interquartile Range =',InterquartileRange.InterquartileRange().calculateInterquartileRange(inputData))

if choice == 3 :

    # Regression Analysis

    print('Enter choice : ')
    print()
    print('1. Linear Regression')
    print('2. Non-Linear Regression')
    print()

    choice = int(input('Enter Choice : '))
    print()

    if choice == 1 :

        # Linear Regression

        print('Linear Regression : ')
        print()
        LinearRegression.LinearRegression().calculateLinearRegression(input2DData)

    if choice == 2 :

        # NonLinear Regression

        print('Non Linear Regression : ')
        print()
        NonLinearRegression.NonLinearRegression().calculateNonLinearRegression()

if choice == 4 :

    # Forecasting

    print('Forecasting :')
    print()
    Forecasting.Forecasting().calculateForecasting()

if choice == 5 :

    # Hypothesis Analysis

    print('Enter choice : ')
    print()
    print('1. Student T-Test')
    print('2. Paired T-Test')
    print('3. ANOVA')
    print('4. Chi Squared Test')
    print('5. Pearson\'s Correlation Coefficient')
    print()

    choice = int(input('Enter Choice : '))
    print()

    if choice == 1 :

        # Student T-Test

        print('Student T-Test : ')
        print()
        StudentTTest.StudentTTest().calculateStudentTTest(input2DData)

    if choice == 2 :

        # Paired T-Test

        print('Paired T-Test : ')
        print()
        PairedTTest.PairedTTest().calculatePairedTTest(input2DData)

    if choice == 3 :

        # ANOVA

        print('Analysis Of Variance (ANOVA) : ')
        print()
        Anova.Anova().calculateANOVA(input2DData)

    if choice == 4 :

        # Chi Squared

        print('Chi Squared Test : ')
        print()
        ChiSquared.ChiSquared().calculateChiSquared(chiData)

    if choice == 5 :

        # Pearson's Correlation Coefficient

        print('Pearson\'s Correlation Coefficient : ')
        print()
        PearsonCoeff.PearsonCoeff().calculateCorrelationCoefficient(input2DData)
