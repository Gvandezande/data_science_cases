# Fuel Consumption  
## Lineaire regressie

Samira Tahriou

# ** Stappen van mijn Notebook:

# Importing libraries
# Data inladen
# Data exploreren: kijken naar het aantal kolommen,rijen, kolomnamen, kolomtypes, aantal not null waardes, statistische samenvatting, nulwaardes per kolomn, aantal duplicaten checken..
# Verdere Data Analyse dmv Data Profiler Sweetviz
# X en y definiëren
# Boxplots van alle X variabelen om schaalverschillen te zien, Outliers te detecteren & inzicht in spreiding van de data
# Boxplots van X variabelen na het verwijderen van bepaalde features
# Numerieke en categorische kolommen opgesplitst
# Correlatiematrix & dmv Correlatiematrix, data
# Nieuwe lijst met numerieke features gemaakt (zonder de onderling gecorreleerde kolommen)
# Outliers verwijderen met Isolation Forest
# Mijn pipeline
# R² score & MSE:
# Mijn score van de Lineaire regressie vergelijken met die van in de orginele document 
# K-Fold Cross-Validatie uitgevoerd: Controleren of mijn model goed presteert op verschillende folds van de data & of het consistent goed presteert zonder overfitting