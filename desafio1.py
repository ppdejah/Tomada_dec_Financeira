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
##import matplotlib.pyplot as plt


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
X = []
cont_reajusteimovel = 0
cont_reajustealuguel = 0
EvoImovel = ['500000']
EvoInvestimento = [entrada]
EvoPatrimonio = [entrada]
Somatorio = entrada
patrimonio = entrada
aluguel = 1800.00
#Distribuições
#VIM = VALORIZAÇÂO DO IMOVEL
distribuicaoVIM = np.random.triangular(1,2,4,50000)
# SAF = SALDO APLICADO AO FUNDO 
distribuicaoSAF = np.random.normal(1.1,0.5,50000)

distribuicaoAL = np.random.triangular(-1,2,4,50000)






for i in range (0, nparcelas+1):
#primeira coluna onde o unico valor diferente de zero é Saldo Devedor
    if i == 0:
        a, j, Pmt = 0, 0, 0
        sd = valor_finan
#outras linhas da tabela de amortização 
    else:
        ##Construindo a tebela de amortização
        Pmt = round((valor_finan/((1-(1+tax_mount)**-nparcelas)/tax_mount)),2)
        j = round(sd*tax_mount,2)
        a = round(Pmt - j,2)
        sd = round(sd - a,2) 
        #calculando investimento 
        DifInvestida = Pmt - aluguel
        Somatorio = DifInvestida + Somatorio
        
        indSAF = int(random.randint(0,50000))
        Rendimentos = round((distribuicaoSAF[indSAF]/100)*Somatorio + Somatorio,2)
        Rendimento = Somatorio
        EvoInvestimento.append(Rendimentos)
        
        patrimonio = patrimonio + a
        EvoPatrimonio.append(patrimonio)
        
        #controle de tempo 
        cont_reajusteimovel = cont_reajusteimovel +1
        cont_reajustealuguel = cont_reajustealuguel +1
        
        if cont_reajustealuguel == 24:
            ind = int(random.randint(0,50000))
            novo_aluguel = round((distribuicaoAL[ind]/100)*aluguel + aluguel,2)
            print("Com a taxa de juros de: {:.2f}".format(distribuicaoAL[ind]))
            print("Agora o valor do aluguel é: {:.2f}".format(novo_aluguel))
            aluguel = novo_aluguel
            cont_reajustealuguel = 0
        ##calculando o preço do imovel 
        if cont_reajusteimovel == 36:
            indVIM = int(random.randint(0,50000))
            novo_Vimovel = round((distribuicaoVIM[indVIM]/100)*novo_Vimovel + novo_Vimovel,2)
            ganho = novo_Vimovel - valor_imovel
            EvoImovel.append(novo_Vimovel)
            print("Com a taxa de juros de: {:.2f}".format(distribuicaoVIM[indVIM]))
            print("Agora o valor do imovel é: {:.2f}\n Seu ganho foi: {:.2f}".format(novo_Vimovel, ganho))
            cont_reajusteimovel = 0
            patrimonio = patrimonio + ((distribuicaoVIM[indVIM]/100)*novo_Vimovel)
            
            
        variaveis = [i, Pmt, a, j, sd]
    
    print(variaveis)
    tabela.append(variaveis)
    X.append(i)
#transformando a lista em matriz 
tabela  = np.array(tabela)

#colocando colunas na matriz 
tabela = pd.DataFrame(tabela, columns = ['Periodo', 'Prestação', 'amortização', 'juros', 'Saldo devedor'])

print('\n')


#gerando o arquivo em excel 
tabela.to_excel('amortização de emprestimo.xlsx', index = False)
   

r = np.arange(0,360,1)
plt.title('Valor do imovel no tempo')
plt.plot(EvoImovel)
plt.show()

plt.title('Valor Investimento no tempo')
plt.plot(EvoInvestimento)
plt.show()

plt.title('Valor Investimento no tempo')
plt.plot(EvoPatrimonio)
plt.show()


plt.title('Valor do Patrimonio X Investimento ')
plt.plot(EvoPatrimonio)
plt.plot(EvoInvestimento)
plt.show()



    

    
    