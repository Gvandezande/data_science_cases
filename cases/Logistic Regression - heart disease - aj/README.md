## LOGISTIC REGRESSION - Amrita

==========================================================================

This dataset "Logistic regression To predict heart disease" taken from Kaggle. This dataset contains data to predict heart disease.

Link to dataset: https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression/data


## About Dataset

World Health Organization has estimated 12 million deaths occur worldwide, every year due to Heart diseases. Half the deaths in the United States and other developed countries are due to cardio vascular diseases. The early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications. This research intends to pinpoint the most relevant/risk factors of heart disease as well as predict the overall risk using logistic regression


==========================================================================

## Choosen Notebook:

The notebook I have choosen to improve is "Predict heart disease (Logistic regression)".

Link to notebook: https://www.kaggle.com/code/aryantyagi19/predict-heart-disease-logistic-regression#Logistic-Regression

My aim is to implement a model which would improve the model score in the notebook by this author.
==========================================================================

## Summary of original notebook:

The models the author used with correspponding scores are:

Testing accuracy :  0.8423


## My work:

I decided to implement feature engineering to improve the model.


## STEPS:

1) First thing I did was to load the dataset.

2) Next I checked for missing values and outliers.
There were a lot of missing values. So I decided to fill them using median.There were outliers too as in histogram skewness can be seen. So, I also decided to remove those outliers using quantile and multiplier.

3) I decided to improve the model by scaling the continous features.

4) Next I printed the correlation matrix to check the correlations between the features, I found that sysBP and diaBP are highly correlated followed by sysBP and prevalentHyp.

5) After splitting the dataset into 20:80 ratio, I implemented the logistic regression model. Where the score for test data is 0.8573 which is better than the original code "0.8423".


## Conclusion

This now gives us a score for test data as "0.8573" which is 1.5% better than original model "0.8423".