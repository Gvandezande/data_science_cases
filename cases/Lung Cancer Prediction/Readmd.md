# Lung Cancer Prediction
Samira Tahriou


# ** Stappen van mijn Notebook:

# Importing libraries
# Data inladen
# Data exploreren: kijken naar het aantal kolommen,rijen, kolomnamen, kolomtypes, aantal not null waardes, statistische samenvatting (counts, means..), nulwaardes per kolomn, aantal duplicaten checken..
# Duplicaten verwijderen
# Dubbelchecken of er uiteindelijk nog duplicaten zijn
# Verdere Data Analyse dmv Data Profiler Sweetviz
# Targetlabels 'LUNG_CANCER' omzetten naar 0 en 1
# Correlatie Matrix voor numerieke features
# Scatterplot: de relatie tussen AGE en LUNG_CANCER
# Staafdiagram die het aantal mensen toont die wel of geen longkanker hebben in de dataset (TARGET).
# valuecounts met normalize=True om proporties te zien van het aantal waardes met longkanker / aantal geen longkanker (proporties in plaats van absolute aantallen)
    #   De verhouding is 86,23% Ywaardes met 1 (yes cancer) vs. 13,76% Ywaardes met 0 (no cancer) => de dataset is sterk onbalanced.
    #   M.a.w. het model kan een nauwkeurigheid van 86% kan behalen door altijd LUNG_CANCER = 1 te voorspellen. 
    #   Bij onbalanced data is accuracy (nauwkeurigheid) vaak misleidend. Om die reden gebruik ik de metrieken:
            # Precision: hoeveel van de voorspelde positieven zijn daadwerkelijk positief?
            # Recall: hoeveel van de werkelijke positieven zijn correct voorspeld
            # F1-score: gemiddelde van precision en recall.
# Age distributie dmv histplot  
    #Als ik mijn outliers leeftijd <30 verwijder: dan zie ik dat de resultaten iets minder zijn 
    # Als ik de AGE opsplits in leeftijdsgroepen, zie ik dat het resultaat ook iets minder wordt
# StandardScaler op de kolom Age & vervolgens boxplot gemaakt na het standaardiseren van Age (om het effect van standardscale te zien op leeftijd t.o.z.v andere features)
# Train-test split
# Pipeline bouwen
# Model trainen
# Voorspellingen maken
# Evaluatie