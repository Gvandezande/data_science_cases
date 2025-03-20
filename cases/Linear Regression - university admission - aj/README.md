## LINEAR REGRESSION - Amrita

==========================================================================

This dataset "Data for Admission in the University" taken from Kaggle. This dataset contains data to take admission in the university for higher studies.

Link to dataset: https://www.kaggle.com/datasets/akshaydattatraykhare/data-for-admission-in-the-university/data


## About Dataset

This dataset includes various information like GRE score, TOEFL score, university rating, SOP (Statement of Purpose), LOR (Letter of Recommendation), CGPA, research and chance of admit. In this dataset, 400 entries are included.

GRE Scores (out of 340)
TOEFL Scores (out of 120)
University Rating (out of 5)
Statement of Purpose (SOP) and Letter of Recommendation (LOR) Strength (out of 5)
Undergraduate GPA (out of 10)
Research Experience (either 0 or 1)
Chance of Admit (ranging from 0 to 1).

==========================================================================

## Choosen Notebook:

The notebook I have choosen to improve is "Analysis of University Admissions Data".

Link to notebook: https://www.kaggle.com/code/yogesh239/analysis-of-university-admissions-data/notebook

My aim is to implement a model which would improve the model score in the notebook by this author.
==========================================================================

## Summary of original notebook:

The models the author used with correspponding scores are:

Model                           Score for Test Data     RMSE value
Linear Regression               0.7952 (0.8212)         0.0679
Decision Tree Regression        0.6766                  0.0914
Random Forest Regression        0.8072                  0.0706
KNN                             0.6535                  0.0946
XGBoost Regression              0.7991                  0.0721

**Error found**: the author put the score for train data instead of test data for Linear Regression model. It should have been 0.8212 not 0.7952. Rest is fine.


## My work:

I decided to implement polynomial regression, a type of linear regression.

**Note**: Instead of copying the whole original code and then improving it, I decided to first clean it and then only use the recommended part of code for my improvement in "analysis-university-admission-version-updated-aj.ipynb" file.

## STEPS:

1) First thing I did was to load the dataset and then check for missing values.
There were no missing values.

2) Next I checked for outliers.
There were no outliers.

3) I found that a few feature names had extra spaces at the end of the name which would have caused some problems. So I removed those extra spaces.

4) I then used correlation matrix to check the relationship between the variables
I found there was no negative correlation or multicollinearity (So, I did not have to remove any variables)

5) After splitting the dataset into 20:80 ratio, I implemented the linear regression model. Where the score for test data is 0.8212.
The author made an error there and accidently put score for train data instead of test data for linear regression.

6) I then implemented a polynomial regression model with degree 2 where the score for test data is 0.8254 an improvement of 0.42%. 

7) I also tried feature engineering to improve the model further. I decided to add a new feature by multiplying GRE score and TOEFEL score; GRE score and CGPA and CGPA and TOEFL score as they have strong correlation. I also decided to drop few features "SOP" and "CGPA" as SOP has moderate correlation and CGPA is highly correlated with GRE score and TOEFL score.
This now gives us a score for test data as 0.8408 which is 1.96% better than original model.

## Conclusion

The model that gives the highest score "0.8408" is polynomial regression with degree 2 and feature engineering (droping and adding few features).