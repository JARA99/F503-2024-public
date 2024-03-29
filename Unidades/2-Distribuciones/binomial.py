# File: binomial.py
# Date: 2024-02-22

# importar librerias
from matplotlib import pyplot as plt
import numpy
import pandas
import math
from scipy import optimize as sciopt
import streamlit as st


# Funcion de distribucion binomial
def binomial(x,n,p,q):
    # Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion

    comb = math.comb(n,x)
    p_x = p**x
    q_nx = q**(n-x)

    return comb*p_x*q_nx

def binomial2(x,n,p):
    return binomial(x,n,p,1-p)

binomial2 = lambda x,n,p: binomial(x,n,p,1-p)

# eval_ = binomial(100,600,1/6,5/6)
# eval_ = binomial(n=600,x=100,p=1/6,q=5/6)
# eval_ = binomial(100,600,q=5/6,p=1/6)

# print(eval_)

n = 50
p = 1/2
q = 1/2

lista = numpy.arange(n+1)
print(lista)

# Esto es una lista:
# [3,4,5,6]
# Esto es un dict.
# a = {'pc1':67,'pc2':80}

data_table = pandas.DataFrame({'x':lista})
# data_table['Nueva'] = data_table['x'] - 50

#lambda
# f = lambda x: x+1
# def f(x):
#     return x+1
# print('Lambda:',f(7))

data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)
data_table['Pb_err'] = data_table['Pb'] + (numpy.random.random((n+1)))*0.01
print(data_table)

out = sciopt.curve_fit(binomial,data_table['x'],data_table['Pb_err'])

print(out)


binomial_plot, axis = plt.subplots()
axis.bar(data_table['x'],data_table['Pb_err'])
# axis.bar(data_table['x'],data_table['Pb'],color='C1')
# plt.show()
# binomial_plot.savefig('imagen.png')

#########################################################################################################
# Streamlit ########################################################################################################

st.title('Graficos binomiales')
st.pyplot(binomial_plot)


