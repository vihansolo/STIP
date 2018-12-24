import numpy as np

class LinearRegression() :

    def __init__(self) :
        pass

    def calculateLinearRegression(self, input2DData = []) :

        x_array = np.array([x for x, y in input2DData])
        y_array = np.array([y for x, y in input2DData])

        def best_fit_slope_intercept (x, y) :
            m = (((np.mean(x_array) * np.mean(y_array)) - np.mean(x_array * y_array)) / ((np.mean(x_array) ** 2) - np.mean(x_array ** 2)))
            b = np.mean(y_array) - m * np.mean(x_array)

            return m, b

        m,b = best_fit_slope_intercept(x_array, y_array)

        predict_x = 8
        predict_y = (m * predict_x) + b

        print('\tProbable point = (',predict_x,',',predict_y,')')
