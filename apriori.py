# Cargamos las librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
# Importamos el archivo de transacciones
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
# Resultados
results = list(rules)
def inspect(results):
    rh          = [tuple(result[2][0][0]) for result in results]
    lh          = [tuple(result[2][0][1]) for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(rh, lh, supports, confidences, lifts))
# Este comamdo crea un frame para ver los datos resultados
resultDataFrame=pd.DataFrame(inspect(results),
                columns=['rhs','lhs','support','confidence','lift'])
#Imprimimos el frame con las reglas
print(resultDataFrame)