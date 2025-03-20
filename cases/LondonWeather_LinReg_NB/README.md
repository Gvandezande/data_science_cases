# data_science_cases
Predicting Temperature in London
based on: https://www.kaggle.com/code/abdelazizsami/project-predicting-temperature-in-london 

## Dataset: 
 `london_weather.csv`contains the following columns:
- **date** - recorded date of measurement - (**int**)
- **cloud_cover** - cloud cover measurement in oktas - (**float**)
- **sunshine** - sunshine measurement in hours (hrs) - (**float**)
- **global_radiation** - irradiance measurement in Watt per square meter (W/m2) - (**float**)
- **max_temp** - maximum temperature recorded in degrees Celsius (°C) - (**float**)
- **mean_temp** - **target** mean temperature in degrees Celsius (°C) - (**float**)
- **min_temp** - minimum temperature recorded in degrees Celsius (°C) - (**float**)
- **precipitation** - precipitation measurement in millimeters (mm) - (**float**)
- **pressure** - pressure measurement in Pascals (Pa) - (**float**)
- **snow_depth** - snow depth measurement in centimeters (cm) - (**float**)

## Notebooks:
While the original notebook is experimenting with regressions, decisiontree & randforest, without taking into account specific time series characteristics (e.g. train test split, etc. ) I wanted to focus on time series.
**2_TimeSeriesPrediction**
In this notebook the analysis is more focoused on time series.

**Preparations**
* import packages
* load data
* set MLFlow

**Exploratory Data Analysis**
* Explore dataset & data types
* fix index, missing values
* Visuals (target feature, decomposition, anual mean fluctuations)
* ACF/PACF-plots
* testing stationarity


**Train & Evaluate Models** 
* baseline model
* Arima 
* Sarima
* Lasso (variables not lagged)
* Predicts on test data and calculates RMSE (Root Mean Squared Error).
* Logs models and performance metrics using MLflow.

**Main disadvantage of the approach:**
- The most interesting models of Arima & Sarima need more fine tuning. 
- Probably a more complex model including different variables with lags would perform best?

