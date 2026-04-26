import numpy as np
import pandas as pd

def get_data():
    data = pd.read_csv('prevendo-preço-casas/house_prices.csv')
    data = data.to_numpy()
    X = data[:,0]
    Y = data[:,1]
    return X,Y

X,Y = get_data()

metro_casa = Y/X

metro_medio = np.sum(metro_casa) / X.size

print(metro_medio)