# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:12:16 2019

@author: pepe8
"""

#blibliotecas uteis do python padans e numpy as é uma maneira de abreviar, agora pra chamar a bliblioteca chamano pela abreviação


import pandas as pd
import random 
import numpy as np
import matplotlib.pyplot as plt



#input de dados
valor_imovel = 500000
novo_Vimovel = 500000
entrada = valor_imovel*0.15
valor_finan = valor_imovel - entrada
tax = 9
tax_mount = (1+tax/100)**(1/12) -1
print('Sua taxa desse contrato é de 9% ao ano e ao mês é: {}'.format(tax_mount))
nparcelas = 360
tabela = []
cont_reajusteimovel = 0
cont_reajustealuguel = 0
EvoImovel = ['500000']
EvoInvestimento = [entrada]
EvoPatrimonio = [entrada]
Somatorio = entrada
patrimonio = entrada
aluguel = 2200.00
To_Aluguel = 0
variaveis = []
ganho = 0
#Distribuições
#VIM = VALORIZAÇÂO DO IMOVEL
distribuicaoVIM = np.random.triangular(1,6,8,50000)
# SAF = SALDO APLICADO AO FUNDO 
distribuicaoSAF = np.random.normal(0.4,0.15,50000)

distribuicaoAL = np.random.triangular(1,2,4,50000)

distribuicaoTR = np.random.normal(0.1, 0.05,50000)



for i in range (0, nparcelas+1):
#primeira coluna onde o unico valor diferente de zero é Saldo Devedor
    if i == 0:
        a, j, Pmt = 0, 0, 0
        sd = valor_finan
        a2, j2, Pmt2 = 0, 0, 0
        sd2 = sd
        trAcumulada = 0
#outras linhas da tabela de amortização 
    else:
        ##Construindo a tebela de amortização
        Pmt = round((valor_finan/((1-(1+tax_mount)**-nparcelas)/tax_mount)),2)
        j = round(sd*tax_mount,2)
        a = round(Pmt - j,2)
        sd = round(sd - a,2)
        #sorteando numero de indicie para pegar numeros na distribuicao
        ind = int(random.randint(0,50000))
        
        
        tr = round(distribuicaoTR[ind],2)
        trAcumulada = round(trAcumulada + tr,2)
        x = (8/100 + trAcumulada) + 1 
        
        a2= round(a * x,2)       
        j2= round(j * x ,2)
        Pmt2= round(Pmt * x,2)
        sd2= round(sd * x,2)
        
        
        #calculando investimento 
              
        Somatorio = (Pmt - aluguel) + Somatorio
        Rendimentos = round(((distribuicaoSAF[ind]/100)+1)*Somatorio,2)
        EvoInvestimento.append(Rendimentos)
        Somatorio = Rendimentos 
        
        #controle de tempo 
        cont_reajusteimovel = cont_reajusteimovel +1
        cont_reajustealuguel = cont_reajustealuguel +1
        
        if cont_reajustealuguel == 24:
            novo_aluguel = round((distribuicaoAL[ind]/100)*aluguel + aluguel,2)
            aluguel = novo_aluguel
            cont_reajustealuguel = 0
            
            
            
        ##calculando o preço do imovel 
        if cont_reajusteimovel == 12:
            novo_Vimovel = round((distribuicaoVIM[ind]/100)*valor_imovel + valor_imovel,2)
            ganho = novo_Vimovel - valor_imovel
            patrimonio = patrimonio + ganho
            valor_imovel = novo_Vimovel
            cont_reajusteimovel = 0
               
               
        EvoImovel.append(novo_Vimovel)
        patrimonio = patrimonio + a
        EvoPatrimonio.append(patrimonio)
        To_Aluguel = aluguel + To_Aluguel
        
    variaveis = [i, Pmt, a, j, sd, tr, trAcumulada, Pmt2, a2, j2, sd2]
    
    print(variaveis)
    print(aluguel)
    
    tabela.append(variaveis)
    
    plt.title('PATRIMONIO X INVESTIMENTO')
    plt.plot(EvoInvestimento)
    plt.plot(EvoPatrimonio)
    plt.show()

#transformando a lista em matriz 
tabela  = np.array(tabela)

#colocando colunas na matriz 

tabela = pd.DataFrame(tabela, columns = ['Periodo', 'Prestação', 'amortização', 'juros', 'Saldo-devedor', 'Taxa de referencia', 'Taxa de referencia acumulada', 'Prestacao corrigida', 'Amortizacao Corrigida', 'Juros corrigido', 'Saldo Devedor corrigido'])

print('\n')


#gerando o arquivo em excel 
tabela.to_csv ('amortização de emprestimo.xsl', index = False)

###Analisando


plt.title('Valor do imovel no tempo')
plt.plot(EvoImovel)
plt.show()

plt.title('Valor Investimento no tempo')
plt.plot(EvoInvestimento)
plt.show()

plt.title('Valor Investimento no tempo')
plt.plot(EvoPatrimonio)
plt.show()

print(patrimonio)
print(Rendimentos)








    

    
    
