from MSTUPModels.MeasureOfCentralTendencies import Mean, Median, Mode

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
