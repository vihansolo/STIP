import tkinter as tk
from STIPModels.MeasureOfCentralTendencies import Mean, Median, Mode
from STIPModels.MeasureOfDispersions import Variance, StandardDeviation, InterquartileRange
from STIPModels.RegressionAnalysis import LinearRegression

def raiseFrame(frame) :
    frame.tkraise()

def generateMean() :
    output = "Mean   :   " + str(Mean.Mean().calculateMean([int(i) for i in enterMeanArrayToCompute.get().split(',')]))
    tk.Label(meanFrame, text = output, font = ("Gill Sans MT", 20)).pack(padx = 73, pady = 130, side = tk.TOP, anchor = "nw")
    calculateMeanButton.config(state = "disabled")

def generateMedian() :
    output = "Median   :   " + str(Median.Median().calculateMedian([int(i) for i in enterMedianArrayToCompute.get().split(',')]))
    tk.Label(medianFrame, text = output, font = ("Gill Sans MT", 20)).pack(padx = 73, pady = 130, side = tk.TOP, anchor = "nw")
    calculateMedianButton.config(state = "disabled")

def generateMode() :
    try :
        output = "Mode   :   " + str(Mode.Mode().calculateMode([int(i) for i in enterModeArrayToCompute.get().split(',')]))
    except :
        output = "Mode   :    Multiple Modes Found"

    tk.Label(modeFrame, text = output, font = ("Gill Sans MT", 20)).pack(padx = 65, pady = 130, side = tk.TOP, anchor = "nw")
    calculateModeButton.config(state = "disabled")

def generateVariance() :
    output = "Variance   :   " + str(float("%.4f" % Variance.Variance().calculateVariance([int(i) for i in enterVarianceArrayToCompute.get().split(',')])))
    tk.Label(varianceFrame, text = output, font = ("Gill Sans MT", 20)).pack(padx = 65, pady = 130, side = tk.TOP, anchor = "nw")
    calculateVarianceButton.config(state = "disabled")

def generateStandardDeviation() :
    output = "Standard Deviation   :   " + str(float("%.4f" % StandardDeviation.StandardDeviation().calculateStandardDeviation([int(i) for i in enterStandardDeviationArrayToCompute.get().split(',')])))
    tk.Label(standardDeviationFrame, text = output, font = ("Gill Sans MT", 20)).pack(pady = 130, side = tk.TOP, anchor = "w")
    calculateStandardDeviationButton.config(state = "disabled")

def generateInterquartileRange() :
    output = "Interquartile Range   :   " + str(float("%.4f" % InterquartileRange.InterquartileRange().calculateInterquartileRange([int(i) for i in enterInterquartileRangeArrayToCompute.get().split(',')])))
    tk.Label(interquartileRangeFrame, text = output, font = ("Gill Sans MT", 20)).pack(pady = 130, side = tk.TOP, anchor = "nw")
    calculateInterquartileRangeButton.config(state = "disabled")

def generateLinearRegression() :
    output = "Probable Point   :   (8, " + str(float("%.4f" % LinearRegression.LinearRegression().calculateLinearRegression([[int(i) for i in x.split(',')] for x in enterLinearRegressionArrayToCompute.get().split(';')]))) + ")"
    tk.Label(linearRegressionFrame, text = output, font = ("Gill Sans MT", 20)).pack(pady = 130, side = tk.TOP, anchor = "nw")
    calculateLinearRegressionButton.config(state = "disabled")

master = tk.Tk()

master.title("STIP")
master.geometry("1920x1080")
master.state('zoomed')

startFrame = tk.Frame(master)

# Measure Of Central Tendencies

measureOfCentralTendenciesFrame = tk.Frame(master)
meanFrame = tk.Frame(master)
medianFrame = tk.Frame(master)
modeFrame = tk.Frame(master)

# Measure of Dispersions
 
measureOfDispersionsFrame = tk.Frame(master)
varianceFrame = tk.Frame(master)
standardDeviationFrame = tk.Frame(master)
interquartileRangeFrame = tk.Frame(master)

# Regression Analysis

regressionAnalysisFrame = tk.Frame(master)
linearRegressionFrame = tk.Frame(master)
nonLinearRegressionFrame = tk.Frame(master)

# Forecasting

forecastingFrame = tk.Frame(master)

# Hypothesis Analysis

hypothesisAnalysisFrame = tk.Frame(master)
studentTTestFrame = tk.Frame(master)
pairedTTestFrame = tk.Frame(master)
anovaFrame = tk.Frame(master)
chiSquaredTestFrame = tk.Frame(master)
pearsonCoeffFrame = tk.Frame(master)

for frame in (startFrame,
                measureOfCentralTendenciesFrame, meanFrame, medianFrame, modeFrame, 
                measureOfDispersionsFrame, varianceFrame, standardDeviationFrame, interquartileRangeFrame, 
                regressionAnalysisFrame, linearRegressionFrame, nonLinearRegressionFrame, 
                forecastingFrame, 
                hypothesisAnalysisFrame, studentTTestFrame, pairedTTestFrame, anovaFrame, chiSquaredTestFrame, pearsonCoeffFrame) :
    frame.grid(row = 0, column = 0, sticky = "nsew", padx = 350)

tk.Label(startFrame, text = "Statistical Techniques Using Python", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)



# Measure Of Central Tendencies

tk.Button(startFrame, text = "1. Measure Of Central Tendencies", command = lambda:raiseFrame(measureOfCentralTendenciesFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(measureOfCentralTendenciesFrame, text = "Measure Of Central Tendencies", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Button(measureOfCentralTendenciesFrame, text = "<---", command = lambda:raiseFrame(startFrame)).pack(side = tk.BOTTOM)

# Mean

tk.Button(measureOfCentralTendenciesFrame, text = "1. Mean", command = lambda:raiseFrame(meanFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(meanFrame, text = "Mean", font = ("Gill Sans MT", 40)).pack(pady = 100, side = tk.TOP)

tk.Label(meanFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 50, pady = 15, side = tk.LEFT, anchor = "nw")

enterMeanArrayToCompute = tk.Entry(meanFrame, font = 14, width = 50)
enterMeanArrayToCompute.pack(pady = 19, padx = 10 , side = tk.TOP, anchor = "nw")

calculateMeanButton = tk.Button(meanFrame, text = "Calculate Mean", command = lambda:generateMean())
calculateMeanButton.pack(padx = 115, pady = 25, side = tk.TOP, anchor = "nw")

# Median

tk.Button(measureOfCentralTendenciesFrame, text = "2. Median", command = lambda:raiseFrame(medianFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(medianFrame, text = "Median", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Label(medianFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 50, pady = 15, side = tk.LEFT, anchor = "nw")

enterMedianArrayToCompute = tk.Entry(medianFrame, font = 14, width = 50)
enterMedianArrayToCompute.pack(pady = 19, padx = 10 , side = tk.TOP, anchor = "nw")

calculateMedianButton = tk.Button(medianFrame, text = "Calculate Median", command = lambda:generateMedian())
calculateMedianButton.pack(padx = 115, pady = 25, side = tk.TOP, anchor = "nw")

# Mode

tk.Button(measureOfCentralTendenciesFrame, text = "3. Mode", command = lambda:raiseFrame(modeFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(modeFrame, text = "Mode", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Label(modeFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 50, pady = 15, side = tk.LEFT, anchor = "nw")

enterModeArrayToCompute = tk.Entry(modeFrame, font = 14, width = 50)
enterModeArrayToCompute.pack(pady = 19, padx = 10 , side = tk.TOP, anchor = "nw")

calculateModeButton = tk.Button(modeFrame, text = "Calculate Mode", command = lambda:generateMode())
calculateModeButton.pack(padx = 115, pady = 25, side = tk.TOP, anchor = "nw")



# Measure Of Dispersions

tk.Button(startFrame, text = "2. Measure Of Dispersions", command = lambda:raiseFrame(measureOfDispersionsFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(measureOfDispersionsFrame, text = "Measure Of Dispersions", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Button(measureOfDispersionsFrame, text = "<---", command = lambda:raiseFrame(startFrame)).pack(side = tk.BOTTOM)

# Variance

tk.Button(measureOfDispersionsFrame, text = "1. Variance", command = lambda:raiseFrame(varianceFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(varianceFrame, text = "Variance", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Label(varianceFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 30, pady = 15, side = tk.LEFT, anchor = "nw")

enterVarianceArrayToCompute = tk.Entry(varianceFrame, font = 14, width = 50)
enterVarianceArrayToCompute.pack(pady = 19, padx = 10 , side = tk.TOP, anchor = "nw")

calculateVarianceButton = tk.Button(varianceFrame, text = "Calculate Variance", command = lambda:generateVariance())
calculateVarianceButton.pack(padx = 115, pady = 25, side = tk.TOP, anchor = "nw")

# Standard Deviation

tk.Button(measureOfDispersionsFrame, text = "2. Standard Deviation", command = lambda:raiseFrame(standardDeviationFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(standardDeviationFrame, text = "Standard Deviation", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Label(standardDeviationFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 50, pady = 15, side = tk.LEFT, anchor = "nw")

enterStandardDeviationArrayToCompute = tk.Entry(standardDeviationFrame, font = 14, width = 50)
enterStandardDeviationArrayToCompute.pack(pady = 19, padx = 10 , side = tk.TOP, anchor = "nw")

calculateStandardDeviationButton = tk.Button(standardDeviationFrame, text = "Calculate Standard Deviation", command = lambda:generateStandardDeviation())
calculateStandardDeviationButton.pack(padx = 85, pady = 30, side = tk.TOP, anchor = "nw")

# Interquartile Range

tk.Button(measureOfDispersionsFrame, text = "3. Interquartile Range", command = lambda:raiseFrame(interquartileRangeFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(interquartileRangeFrame, text = "Interquartile Range", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Label(interquartileRangeFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 50, pady = 15, side = tk.LEFT, anchor = "nw")

enterInterquartileRangeArrayToCompute = tk.Entry(interquartileRangeFrame, font = 14, width = 50)
enterInterquartileRangeArrayToCompute.pack(pady = 19, padx = 10 , side = tk.TOP, anchor = "nw")

calculateInterquartileRangeButton = tk.Button(interquartileRangeFrame, text = "Calculate Interquartile Range", command = lambda:generateInterquartileRange())
calculateInterquartileRangeButton.pack(padx = 115, pady = 25, side = tk.TOP, anchor = "nw")



# Regression Analysis

tk.Button(startFrame, text = "3. Regression Analysis", command = lambda:raiseFrame(regressionAnalysisFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(regressionAnalysisFrame, text = "Regression Analysis", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Button(regressionAnalysisFrame, text = "<---", command = lambda:raiseFrame(startFrame)).pack(side = tk.BOTTOM)

# Linear Regression

tk.Button(regressionAnalysisFrame, text = "1. Linear Regression", command = lambda:raiseFrame(linearRegressionFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(linearRegressionFrame, text = "Linear Regression", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Label(linearRegressionFrame, text = "Input Data           : ", font = ("Gill Sans MT", 14), anchor = "nw").pack(padx = 50, pady = 15, side = tk.LEFT, anchor = "nw")

enterLinearRegressionArrayToCompute = tk.Entry(linearRegressionFrame, font = 14, width = 50)
enterLinearRegressionArrayToCompute.pack(padx = 10, pady = 19, side = tk.TOP, anchor = "nw")

calculateLinearRegressionButton = tk.Button(linearRegressionFrame, text = "Calculate Linear Regression", command = lambda:generateLinearRegression())
calculateLinearRegressionButton.pack(padx = 115, pady = 25, side = tk.TOP, anchor = "nw")

# Non-Linear Regression

tk.Button(regressionAnalysisFrame, text = "2. Non-Linear Regression", command = lambda:raiseFrame(nonLinearRegressionFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(nonLinearRegressionFrame, text = "Non-Linear Regression", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)


# Forecasting

tk.Button(startFrame, text = "4. Forecasting", command = lambda:raiseFrame(forecastingFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(forecastingFrame, text = "Forecasting", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)



# Hypothesis Analysis

tk.Button(startFrame, text = "5. Hypothesis Analysis", command = lambda:raiseFrame(hypothesisAnalysisFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(hypothesisAnalysisFrame, text = "Hypothesis Analysis", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)

tk.Button(hypothesisAnalysisFrame, text = "<---", command = lambda:raiseFrame(startFrame)).pack(side = tk.BOTTOM)

# Student T-Test

tk.Button(hypothesisAnalysisFrame, text = "1. Student T-Test", command = lambda:raiseFrame(studentTTestFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(studentTTestFrame, text = "Student T-Test", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)


# Paired T-Test

tk.Button(hypothesisAnalysisFrame, text = "2. Paired T-Test", command = lambda:raiseFrame(pairedTTestFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(pairedTTestFrame, text = "Paired T-Test", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)


# ANOVA

tk.Button(hypothesisAnalysisFrame, text = "3. ANOVA", command = lambda:raiseFrame(anovaFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(anovaFrame, text = "ANOVA", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)


# Chi Squared Test

tk.Button(hypothesisAnalysisFrame, text = "4. Chi Squared Test", command = lambda:raiseFrame(chiSquaredTestFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(chiSquaredTestFrame, text = "Chi Squared Test", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)


# Pearson's Correlation Coefficient

tk.Button(hypothesisAnalysisFrame, text = "5. Pearson\'s Correlation Coefficient ", command = lambda:raiseFrame(pearsonCoeffFrame), 
                                       width = 75, height = 3).pack(pady = 25, side = tk.TOP)

tk.Label(pearsonCoeffFrame, text = "Person\'s Correlation Coefficient", font = ("Gill Sans MT", 40)).pack(pady = 80, side = tk.TOP)


raiseFrame(startFrame)
master.mainloop()
