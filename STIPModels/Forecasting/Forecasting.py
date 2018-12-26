import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model

class Forecasting() :

    def __init__(self) :
        pass

    def calculateForecasting(self) :

        def prepare_data(df,forecast_col,forecast_out,test_size) :

            label = df[forecast_col].shift(-forecast_out)

            X = np.array(df[[forecast_col]])
            X = preprocessing.scale(X)
            X_lately = X[-forecast_out:]
            X = X[:-forecast_out]

            label.dropna(inplace=True)
            y = np.array(label)

            X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size)

            response = [X_train,X_test , Y_train, Y_test , X_lately]
            return response

        df = pd.read_csv("STIPModels/Forecasting/prices.csv")
        df=df[df.symbol=='GOOG']

        forecast_col = 'close'
        forecast_out = 5
        test_size = 0.2

        X_train, X_test, Y_train, Y_test , X_lately = prepare_data(df,forecast_col,forecast_out,test_size)

        learner = linear_model.LinearRegression()

        learner.fit(X_train,Y_train)
        score = learner.score(X_test,Y_test)

        forecast = learner.predict(X_lately)

        print('Test Score :',score)
        print('Forecast Set : ',forecast)
