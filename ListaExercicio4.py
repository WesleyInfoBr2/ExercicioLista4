import pandas as pd  
import streamlit as st
import matplotlib.pyplot as plt
import ipeadatapy as ip

st.set_page_config(

page_title="Lista de Exercício 4", 
)

st.header("Exercício Projetos")

st.write("Os dados se referem aos valores futuros previstos para receita mensal de 5 projetos diferentes. A análise dos dados permitirá a decisão sobre o investitmento em um ou mais alternativas de projetos. Neste cenário, os dados futuros se referem ao período de 2022 e 2023, logo, a data referência da análise é de dezembro/2021")

arquivo = "https://raw.githubusercontent.com/WesleyInfoBr2/ExercicioLista4/main/projetos.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))

st.write("O dataframe foi atualizado adicionando mais uma linha ao final com os dados referentes ao mês de dezembro de 2023.")
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.dataframe(df.tail())

st.write("Apresentação da soma dos valores de cada projeto agrupado por ano")
colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.write(df.groupby('ano')[colunas].sum())

st.write("Gráfico de dispersão cruzando os dados do Projeto1 e Projeto2, com marcadores verdes e em formato de estrela")
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

st.write("Gráfico do tipo histograma com os dados do Projeto 1 e Projeto4")
fig, ax = plt.subplots()
df["Projeto1"].plot(kind = 'hist', ax=ax)
df["Projeto4"].plot(kind = 'hist', ax=ax)
st.pyplot(fig)

st.header("Exercício IPEADATA")

st.write("Busca na base do IPEADATA os indicadores relacionados a taxa de juros Selic. O objetivo é encontrar o código correspondente ao indicador 'Taxa de juros - Over / Selic - acumulada no mês'")
busca_selic = ip.list_series('Selic')
busca_selic

st.write("Utilização da biblioteca do IPEADATA para apresentar os valores do indicador 'Taxa de juros - Over / Selic - acumulada no mês' dos anos de 2022 e 2023")         
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic

st.write("Gráficos de linha, apresentando os meses e valores das taxas, um para o ano de 2022 e outro para o ano de 2023")         
fig, ax = plt.subplots()
plt.title('2022')
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
fig, ax = plt.subplots()
plt.title('2022')
ip.timeseries('BM12_TJOVER12', year=2023).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)