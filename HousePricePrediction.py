'''
Compétition Kaggle: House Price Prediction

Itération 1
Résultat présent: Non terminé

Variable a prédire: SalePrice
Colonnes à fournir: Id, SalePrice

Métrique d'évaluation: RMSE (entre log(pred_y) et log(test_y))

Approche privilégiée: apprentissage supervisé
Model présent: Non terminé
'''

#%%
# Imports
import pandas as pd


# Loading data
train_set = pd.read_csv("HousePricePrediction_Data/train.csv",
                        index_col="Id")


'''
Sommaire de l'analyse exploratoire

- Beaucoup de variables catégoriques:
    -MSSubClass: 16 colonnes en OHE
    -MSZoning: 8 colonnes en OHE
    -LotFrontage: float64, 259 valeurs manquantes, très étiré sur la longueur
    -LotArea: int64, aucune valeur manquante, aussi très étiré sur la longueur
    -Street: 2 colonnes en OHE
    -Alley: 3 colonnes en OHE
    -LotShape: 4 colonnes en OHE
    -LandContour: 4 colonnes en OHE
    -Utilities: 4 colonnes en OHE
    -LotConfig: 5 colonnes en OHE
    -LandSlope: 3 colonnes en OHE
    -Neighborhood: 25 colonnes en OHE
    -Condition1: 9 colonnes en OHE
    -Condition2: 9 colonnes en OHE
    -BldgType: 5 colonnes en OHE
    -HouseStyle: 8 colonnes en OHE
    -OverallQual: 10 colonnes en OHE
    -OverallCond: 10 colonnes en OHE
    -YearBuilt: int64, à vagues, aucune valeur manquante
    -YearRemodAdd: int64, à vagues, aucune valeur manquante


'''

# %%
