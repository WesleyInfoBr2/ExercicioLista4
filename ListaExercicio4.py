import pandas as pd  
import streamlit as st
import matplotlib.pyplot as plt
import ipeadatapy as ip

st.set_page_config(

page_title="Lista de Exercício 4", 
)

st.header("Exercício Projetos")

arquivo = "https://raw.githubusercontent.com/WesleyInfoBr2/ExercicioLista4/main/projetos.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.dataframe(df.tail())

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.write(df.groupby('ano')[colunas].sum())

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
df["Projeto1"].plot(kind = 'hist', ax=ax)
df["Projeto4"].plot(kind = 'hist', ax=ax)
st.pyplot(fig)

st.header("Exercício IPEADATA")

busca_selic = ip.list_series('Selic')
busca_selic

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic

fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)