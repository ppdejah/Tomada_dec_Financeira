# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:12:16 2019

@author: pepe8
"""

#blibliotecas uteis do python padans e numpy as é uma maneira de abreviar, agora pra chamar a bliblioteca chamano pela abreviação


import pandas as pd
import numpy as np
##import matplotlib.pyplot as plt


#input de dados
valor_finan = 500000
tax = 9
tax_mount = (1+tax/100)**(1/12) -1
print('Sua taxa desse contrato é de 9% ao ano e ao mês é: {}'.format(tax_mount))
nparcelas = 360
tabela = []


for i in range (0, nparcelas+1):
#primeira coluna onde o unico valor diferente de zero é Saldo Devedor
    if i == 0:
        a, j, Pmt = 0, 0, 0
        sd = valor_finan
#outras linhas da tabela de amortização 
    
    else:
        Pmt = round((valor_finan/((1-(1+tax_mount)**-nparcelas)/tax_mount)),2)
        j = round(sd*tax_mount,2)
        a = round(Pmt - j,2)
        sd = round(sd - a,2) 
        
    variaveis = [i, Pmt, a, j, sd]
    
    print(variaveis)
    tabela.append(variaveis)
    
#transformando a lista em matriz 
tabela  = np.array(tabela)

#colocando colunas na matriz 
tabela = pd.DataFrame(tabela, columns = ['Periodo', 'Prestação', 'amortização', 'juros', 'Saldo devedor'])

print('\n')


#gerando o arquivo em excel 
tabela.to_excel('amortização de emprestimo.xlsx', index = False)




    

    
    