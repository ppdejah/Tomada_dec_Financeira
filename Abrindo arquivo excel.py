# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:21:18 2019

@author: pepe8
"""
import pandas as pd
import random 
import numpy as np 
import matplotlib.pyplot as plt


alunos = ['joão', 'gabriel', 'gustavo']

sorteio = random.choices(alunos, k=1)
print(alunos)

## distribuição aleatoria triangular
start_time = datetime.now()
print('inicio: ', start_time)

distribuicao = np.random.triangular(3.20,4.15,5,500000)
# distribuição uniforme 

#distribuicao2 = np.random.uniform(3.20,5,1000000)

#distribuição normal
#distribuicao3 = np.random.normal(4.15,2,1000000)

#print('media é de: {:.4f}'.format(np.mean(distribuicao)))
#print('media é de: {:.4f}'.format(np.mean(distribuicao2)))
#print('media é de: {:.4f}'.format(np.mean(distribuicao3)))
plt.plot(distribuicao, bins = 100)
plt.show()

termino = datetime.now()

print('tempo ', termino - start_time)