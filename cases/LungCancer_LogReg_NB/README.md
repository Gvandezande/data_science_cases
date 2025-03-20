lung_cancer_prediction_dataset
=================================

This project aims to give an example of logistic regression and other classification methods. 
It builds upon the work of https://www.kaggle.com/datasets/aizahzeeshan/lung-cancer-risk-in-25-countries (dataset)
and https://www.kaggle.com/code/sumitsinghlko/lung-cancer-analysis (analysis)

Variables: 

**ID:** A unique identifier for each record in the dataset.
**Country:** The country where the data was collected or where the individual resides (Object).
**Population_Size:** The total population size of the country or region under study (Int).
**Age:** The age of the individual (in years) included in the data (Int).
**Gender:** The gender of the individual (Male/Female).
**Smoker:** Indicates whether the individual is a smoker (Yes/No).
**Years_of_Smoking:** The number of years the individual has been smoking(Int).
**Cigarettes_per_Day:** The average number of cigarettes the individual smokes daily (Int).
**Passive_Smoker:** Whether the individual is exposed to secondhand smoke (Yes/No).
**Family_History:** Indicates if the individual has a family history of lung cancer (Yes/No).
**Lung_Cancer_Diagnosis:** Indicates whether Lung Cancer has been diagnosed (Yes/No) 
**Cancer_Stage:**   Post-Diagnosis feature indicating stage 1- 4 (NaN for all neg.diagosed)
**Survival_Years:** Post-Diagnosis follow-up years 1-10 (0 for all neg.diagnosed) 
**Adenocarcinoma_Type:**         Yes/No Object
**Air_Pollution_Exposure:** categoric object with tree levels:  medium, low, high
**Occupational_Exposure:** Yes/No        
**Indoor_Pollution:** Yes/No             
**Healthcare_Access:** good/poor 
**Early_Detection:** Yes/No                 
**Developed_or_Developing:** Yes/NO on country-level         
**Annual_Lung_Cancer_Deaths:** Int on country-level     
**Lung_Cancer_Prevalence_Rate:** float on country-level  
**Mortality_Rate:** float (NaN for all neg.diagnosed)

**Licence: MIT**

#### Code:

**2_Reanalyzing_lung-cancer-analyis.ipynb**
adapted work

#### Hints: where to look for changes

**Exploratory data analysis** 
focusses on finding the **features that give away the diagnoses**.
As such the features: 
* Cancer_Stage
* Treatment_Type
* Survival_Years
* Mortality_Rate
Have been identified as post-diagnosis parameters.

Equally **Adenocarcinoma_Type** seems to corresponde to cancer diagnosis

Further several features seem to correspond to **country characteristics** more than individual ones.

**Exploratory figures** have been pruned.

**ML Preparation & Pipeline**

* Feature selection
* setting ID as index
* splitting target & predictors
* numerical vs categorical features
* preprocessing: StandardScaler & OneHotEncoder
* *note: there were no missing values*
* definition of classifiers: 
    * Logistic regression, 
    * Decision Tree, 
    * Random Forest, 
    * GradientBoostingClassifier
    * AdaBoostClassifier
* train & evaluate 
* including possibility of cv
* including possibilit of sampling_method
* evaluate with recall or f1


