
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def get_data():
    data = pd.read_csv('prevendo-preço-casas/house_prices.csv')
    data = data.to_numpy()
    X = data[:,0]
    Y = data[:,1]
    return X,Y

def normalizar_data(X,Y):
    X_norm = (X - np.min(X)) / (np.max(X) - np.min(X))
    Y_norm = (Y - np.min(Y)) / (np.max(Y) - np.min(Y))
    return X_norm, Y_norm

def denormalizar(a,b,X,Y):
    maximoX = np.max(X)
    minimoX = np.min(X)
    maximoY = np.max(Y)
    minimoY = np.min(Y)

    a = a * ((maximoY - minimoY) / (maximoX-minimoX))
    b = b * (maximoY - minimoY) + minimoY - a * minimoX
    return a,b

def init_parametros(X_norm,Y_norm):
    a = (np.max(Y_norm)-np.min(Y_norm)) / (np.max(X_norm) - np.min(X_norm))
    b = np.min(Y_norm)
    return a,b

def fazer_predicao(X,a,b):
    Y_pred = X*a+b
    return Y_pred

def medir_erro_quadratico_medio(Y_pred,Y_norm):
    erro = np.sum((Y_norm-Y_pred)**2)
    # print("erro:",erro)
    return erro

def atualizar_parametros(X_norm,Y_pred,Y_norm,a,b,alpha):
    n = X_norm.size
    da = (-2/n) * np.sum(X_norm*(Y_norm-Y_pred))
    db = (-2/n) * np.sum(Y_norm-Y_pred)
    # print("da:",da,"db:",db)
    a -= alpha*da
    b -= alpha*db
    return a,b


def plotar_graficos(X_norm,Y_norm,a,b):
    plt.scatter(X_norm,Y_norm)
    plt.plot(X_norm,a*X_norm+b)
    plt.show()

def main(alpha,iteracoes):


    X,Y = get_data()
    X_norm , Y_norm = normalizar_data(X,Y)

    a,b = init_parametros(X_norm,Y_norm)

    # frames = np.array([a,b])

    for i in range(iteracoes):
        Y_pred = fazer_predicao(X_norm,a,b)
        a,b = atualizar_parametros(X_norm,Y_pred,Y_norm,a,b,alpha)
        # np.column_stack(frames,np.array([a,b]))

    print(medir_erro_quadratico_medio(Y_pred,Y_norm))
    print(a,b)
    plotar_graficos(X_norm=X_norm,Y_norm=Y_norm,a=a,b=b)
    # print(frames)
    a,b = denormalizar(a,b,X,Y)
    plt.scatter(X,Y)
    plt.plot(X,a*X+b)
    plt.plot(X,1492*X)
    plt.show()

    
# main(float(input()),int(input()))
main(1e-2,1000)

