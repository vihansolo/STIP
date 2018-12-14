import numpy as np

class LinearRegression() :

    def __init__(self) :
        pass

    def calculateLinearRegression(self, x_array = [], y_array = []) :

        x_array = np.array(x_array)
        y_array = np.array(y_array)

        def best_fit_slope_intercept (x, y) :
            m = (((np.mean(x_array) * np.mean(y_array)) - np.mean(x_array * y_array)) / ((np.mean(x_array) ** 2) - np.mean(x_array ** 2)))
            b = np.mean(y_array) - m * np.mean(x_array)

            return m, b

        m,b = best_fit_slope_intercept(x_array, y_array)

        predict_x = 8
        predict_y = (m * predict_x) + b

        print('Probable point = (',predict_x,',',predict_y,')')
