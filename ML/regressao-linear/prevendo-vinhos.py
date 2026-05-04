import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def ler_csvs():
    vinho_tinto_data = pd.read_csv("ML-supervised-learning-master/ML-supervised-learning-master/game-of-wines/data/winequality-red.csv",sep=";")
    vinho_branco_data = pd.read_csv("ML-supervised-learning-master/ML-supervised-learning-master/game-of-wines/data/winequality-white.csv",sep=";")
    return vinho_branco_data,vinho_tinto_data

def separar_dados(vinho_tinto_data,vinho_branco_data):
    treino_vinho_tinto = vinho_tinto_data.iloc[:1300,:]
    arr_treino_vinho_tinto = np.array(treino_vinho_tinto)

    teste_vinho_tinto = vinho_tinto_data.iloc[1300:,:]
    arr_teste_vinho_tinto = np.array(teste_vinho_tinto)

    treino_vinho_branco = vinho_branco_data.iloc[:1300,:]
    arr_treino_vinho_branco = np.array(treino_vinho_branco)

    teste_vinho_branco = vinho_branco_data.iloc[1300:,:]
    arr_teste_vinho_branco = np.array(teste_vinho_branco)

    return arr_treino_vinho_tinto,arr_treino_vinho_branco,arr_teste_vinho_tinto,arr_teste_vinho_branco


def normalizar_colunas(X: np.array):
    min_ = X.min(axis=0)
    max_ = X.max(axis=0)
    den = max_ - min_
    return ((X - min_) / den),min_,max_

def set_parametros(num_features):
    parametros = np.random.rand(1,num_features)
    return parametros

def calcular_previsao(X,parametros):
    previsao = X @ parametros.T
    return previsao

def calcular_erro_medio_quadratico(Y,previsao):
    erro = np.mean((Y-previsao)**2)
    return erro

def for_prop(X,parametros):
    previsao = calcular_previsao(X,parametros)
    return previsao

def backprop(X,Y,previsao,parametros,alpha):

    n = X.shape[0]

    dparametro = (-2/n)*(X.T @ (previsao-Y))

    parametros = parametros + alpha*dparametro.T

    return parametros

def hyperparametros():
    return float(input("Insira o alpha: ")),int(input("Insira n: "))

def treinar(treino,alpha,n):
    
    X = treino[:,:-1]
    X = np.column_stack((X , np.ones((X.shape[0],1))))

    Y = treino[:,-1:]

    num_features = treino.shape[1]-1

    parametros = set_parametros(num_features+1)

    for i in range(n):

        previsao = calcular_previsao(X,parametros)

        erro = calcular_erro_medio_quadratico(Y,previsao)
        
        if i%100 == 0:
            print(erro)
        
        parametros = backprop(X,Y,previsao,parametros,alpha)
    
    return parametros

def testar(teste_vinho,parametros):

    n = random.randint(0,teste_vinho.shape[0]-1)

    X = teste_vinho[n,:-1].reshape(1,-1)
    X = np.column_stack((X, np.ones((1,1))))
    
    Y = teste_vinho[n,-1:]

    previsao = (calcular_previsao(X,parametros))

    return previsao, Y

def calcular_precisao_teste(teste_vinho,parametros_vinho):

    print(teste_vinho.shape)
    X = teste_vinho[:,:-1]
    X = np.column_stack((X, np.ones((X.shape[0],1))))

    Y = teste_vinho[:,-1:]
    
    previsao = calcular_previsao(X,parametros_vinho)

    previsao = np.round(previsao,1)


    acertos = 0
    total = previsao.shape[0]
    for i in range(previsao.shape[0]):
        if previsao[i] == Y[i]:
            acertos += 1
    print(acertos/total)

def main():

    vinho_branco_data, vinho_tinto_data = ler_csvs()

    vinho_tinto_data, min_tinto, max_tinto = normalizar_colunas(vinho_tinto_data)
    vinho_branco_data, min_branco, max_branco = normalizar_colunas(vinho_branco_data)

    treino_vinho_tinto,treino_vinho_branco,teste_vinho_tinto,teste_vinho_branco = separar_dados(vinho_branco_data=vinho_branco_data,vinho_tinto_data=vinho_tinto_data)

    alpha, n = 0.1,10000


    parametros_vinho_tinto = treinar(treino_vinho_tinto,alpha,n)
    
    testar(teste_vinho_tinto,parametros_vinho_tinto)

    calcular_precisao_teste(teste_vinho_tinto,parametros_vinho_tinto)

main()