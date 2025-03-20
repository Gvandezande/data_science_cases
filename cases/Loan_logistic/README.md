Loan_Logistic_Regressie

Created by Herman Steurs

Structure:
cases/
├── Loan_Logistic/
│ ├── data/
│ │ ├── FuelConsumption_dataset
│ ├── Loan_Logistic.ipynb/
│ ├── Sweetviz_Loan_data.html
│ ├── Kaggle_Approval.ipynb
│ ├── requirements.txt
│ ├── README1.md 


More info see kaggle:
https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data
https://www.kaggle.com/code/dilrubayasmin095/loan-approval-classification-dataset-92-accuracy

# Over de file
Deze dataset bevat informatie over leningsaanvragen en de kenmerken van de aanvragers. Het doel van de dataset is om te bepalen of een lening wordt goedgekeurd of afgewezen op basis van verschillende persoonlijke en financiële factoren.
Doelvariabele is loan_status.


Kolomnaam:	
person_age: De leeftijd van de aanvrager. 
person_gender: Het geslacht van de aanvrager. (man of vrouw)
person_education: Het hoogst behaalde diploma.  
person_income: Het jaarlijkse inkomen van de aanvrager.
person_emp_exp: Het aantal jaren werkervaring van de aanvrager.
person_home_ownership: Geeft aan of de aanvrager in een gehuurd pand, in een pand met een hypotheek erop of in een pand zonder hypotheek woont.	
person_cred_hist_length: Hoe lang de kredietgeschiedenis van de persoon is (in jaren).
loan_intent: Het doel van de lening (bijv. educatie, auto, medische kosten, etc.).
loan_amnt: Het aangevraagde leenbedrag.
loan_int_rate: De rentevoet van de lening (uitgedrukt als percentage).
loan_percent_income: Verhouding lenen bedrag / inkomen.
credit_score: Een kredietwaardigheidscore.
previous_loan_defaults_on_file	Geeft aan of de aanvrager eerdere wanbetalingen heeft gehad (binaire waarde: 0 = nee, 1 = ja). 
loan_status: Geeft aan of de lening is goedgekeurd/geweigerd (binaire variabele: 0 = geweigerd, 1 = goedgekeurd).


# Bevindingen
De Kaggle bereikt een modelscore van 92%.  (model.score(X_test, y_test))

Ik kom tot de volgende resultaten:

## model 1
Log Transformatie
Stratify
Scaler

Met 5 % van de outliers verwijderen 
Accuracy: 0.8985  
Precision: 0.7725 --> 77% van de 100 geweigerde leningen is dat in 77 gevallen correct
Recall: 0.7282 --> van de 100 slechte leningen zijn er 72 leningen correct afgewezen
F1 Score: 0.7497 

met 10% van de outliers verwijderen 

Accuracy: van 0.8985 naar 0.9056
Precision: van .7725 naar 0.7645
Recall: van 0.7282 naar 0.7365
F1 Score: van 0.7497 0.7502

## model 2
RFE: beste feature kiezen 
Accuracy: van 0.8924
Precision: van 0.7585
Recall: van 0.7108 
F1 Score: van 0.7339

met 10% van de outliers verwijderen 

Accuracy: van 0.8924 naar 0.8963
Precision: van 0.7585 naar 0.7469
Recall: van 0.7108 naar 0.6979
F1 Score: van 0.7339 naar 0.7215


## model 3
Feature Engineering
Accuracy: van 0.8985 
Precision: van 0.7725 
Recall: van 0.7282 
F1 Score: van 0.7497 

met 10% van de outliers verwijderen 

Accuracy: van 0.8985 naar 0.8639
Precision: van 0.7725 naar 0.6850
Recall: van 0.7282 naar 0.6446
F1 Score: van 0.7497 naar 0.6642




