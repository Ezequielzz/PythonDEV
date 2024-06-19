import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar os dados
def load_data():
    df = pd.read_csv('movies.csv')
    return df

df_filmes = load_data()

# Título da página
st.title('Análise de Filmes')

# Visualização das primeiras linhas do DataFrame
st.subheader('Visualização das primeiras linhas do DataFrame:')
st.write(df_filmes.head())

# Resumo estatístico dos dados numéricos
st.subheader('Resumo estatístico dos dados numéricos:')
st.write(df_filmes.describe())

# Gráfico de barras: Total de votos por gênero
st.subheader('Total de votos por gênero:')
total_votos_genero = df_filmes.groupby('genre')['votes'].sum()
st.bar_chart(total_votos_genero)

# Gráfico de barras: Média de rating por gênero
st.subheader('Média de rating por gênero:')
media_rating_genero = df_filmes.groupby('genre')['rating'].mean()
st.bar_chart(media_rating_genero)

# Barra lateral para filtros
st.sidebar.header('Filtros')

# Filtro por gênero
generos = df_filmes['genre'].unique()
genero_selecionado = st.sidebar.multiselect('Gênero', generos, default=generos)

# Filtro por ano
anos = df_filmes['year'].unique()
ano_selecionado = st.sidebar.multiselect('Ano', anos, default=anos)

# Aplicar filtros
df_filtrado = df_filmes[df_filmes['genre'].isin(genero_selecionado) & df_filmes['year'].isin(ano_selecionado)]

# Seção de visualização de dados
st.header('Visualização de Dados Filtrados')
st.write(df_filtrado)

# Seção de gráficos 
st.header('Gráficos Interativos')

# Seleção do tipo de gráfico
tipo_grafico = st.selectbox('Selecione o tipo de gráfico', ['Barra', 'Linha', 'Dispersão', 'Histograma'])

# Função para criar gráficos
def criar_grafico(tipo):
    if tipo == 'Barra':
        fig = px.bar(df_filtrado, x='title', y='rating', color='genre', title='Rating por Filme e Gênero')
    elif tipo == 'Linha':
        fig = px.line(df_filtrado, x='year', y='rating', color='genre', title='Rating por Ano e Gênero')
    elif tipo == 'Dispersão':
        fig = px.scatter(df_filtrado, x='votes', y='rating', color='genre', title='Dispersão de Votos e Rating')
    elif tipo == 'Histograma':
        fig = px.histogram(df_filtrado, x='rating', color='genre', title='Histograma de Ratings')
    st.plotly_chart(fig)

# Criar o gráfico selecionado
criar_grafico(tipo_grafico)

# Adicionar gráficos adicionais
st.header('Gráficos Adicionais')

# Gráfico de linha do tempo dos ratings
st.subheader('Linha do tempo dos ratings:')
fig_tempo = px.line(df_filtrado, x='year', y='rating', title='Evolução dos Ratings ao Longo do Tempo')
st.plotly_chart(fig_tempo)

# Gráfico de distribuição dos ratings
st.subheader('Distribuição dos Ratings:')
fig_box = px.box(df_filtrado, y='rating', title='Distribuição dos Ratings')
st.plotly_chart(fig_box)

# Heatmap de correlações
st.subheader('Mapa de Calor de Correlações:')
# Selecionar apenas as colunas numéricas
numerical_columns = df_filtrado.select_dtypes(include=['float64', 'int64']).columns
corr = df_filtrado[numerical_columns].corr()
fig_heatmap, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig_heatmap)

# Gráfico de pizza: Participação de cada gênero nos votos totais
st.subheader('Participação de cada Gênero nos Votos Totais:')
fig_pizza = px.pie(df_filtrado, names='genre', values='votes', title='Participação de cada Gênero nos Votos Totais')
st.plotly_chart(fig_pizza)

# Análise de crescimento: Comparar ratings em diferentes períodos
st.subheader('Análise de Crescimento:')
votos_ano = df_filtrado.groupby('year')['votes'].sum()
fig_crescimento = px.bar(votos_ano, x=votos_ano.index, y='votes', title='Crescimento dos Votos por Ano')
st.plotly_chart(fig_crescimento)

# Exibir as métricas
st.header('Métricas de Filmes')
st.metric('Total de Votos', f'{df_filtrado["votes"].sum():,}')
st.metric('Rating Médio', f'{df_filtrado["rating"].mean():.2f}')
