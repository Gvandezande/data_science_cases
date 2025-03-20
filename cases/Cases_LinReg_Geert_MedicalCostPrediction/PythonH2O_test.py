import h2o
import pandas as pd
from h2o.frame import H2OFrame
from h2o.estimators import H2ORandomForestEstimator

# Stap 1: Start de H2O-cluster
h2o.init()

# Stap 2: Laad een dataset (bijv. een CSV-bestand)
# Voor dit voorbeeld gebruiken we een ingebouwde dataset
data = h2o.import_file('data/insurance.csv')
print("Dataset geladen:", data.shape)


# Stap 3: Splits de data in train- en testset
train, test = data.split_frame(ratios=[0.8], seed=42)

# Stap 4: Definieer features (X) en target (y)
x = train.columns[0:-1]  
y = 'charges'

# Stap 5: Maak en train een Random Forest-model
rf_model = H2ORandomForestEstimator(ntrees=50, max_depth=20, seed=42)
rf_model.train(x=x, y=y, training_frame=train)

# Stap 6: Maak voorspellingen op de testset
predictions = rf_model.predict(test)
print("Voorspellingen:\n", predictions.head())

# Stap 7: Evalueer het model
performance = rf_model.model_performance(test)
print("Modelprestaties:\n", performance)

# Stap 8: Sluit de H2O-cluster (optioneel)
h2o.cluster().shutdown()