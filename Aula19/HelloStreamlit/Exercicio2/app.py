import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def load_data():
    df = pd.read_csv('vendas.csv')
    return df

df_vendas = load_data()

# Título da página
st.title('Análise de Vendas')

# Visualização das primeiras linhas do DataFrame
st.subheader('Visualização das primeiras linhas do DataFrame:')
st.write(df_vendas.head())

# Resumo estatístico dos dados numéricos
st.subheader('Resumo estatístico dos dados numéricos:')
st.write(df_vendas.describe())

# Gráfico de barras: Total de vendas por categoria
st.subheader('Total de vendas por categoria:')
total_vendas_categoria = df_vendas.groupby('categoria')['vendas'].sum()
st.bar_chart(total_vendas_categoria)

# Gráfico de barras: Média de vendas por categoria
st.subheader('Média de vendas por categoria:')
media_vendas_categoria = df_vendas.groupby('categoria')['vendas'].mean()
st.bar_chart(media_vendas_categoria)

# Gráfico de barras: Total de vendas por subcategoria
st.subheader('Total de vendas por subcategoria:')
total_vendas_subcategoria = df_vendas.groupby('subcategoria')['vendas'].sum()
st.bar_chart(total_vendas_subcategoria)

# Gráfico de barras: Média de vendas por subcategoria
st.subheader('Média de vendas por subcategoria:')
media_vendas_subcategoria = df_vendas.groupby('subcategoria')['vendas'].mean()
st.bar_chart(media_vendas_subcategoria)

# Barra lateral para filtros
st.sidebar.header('Filtros')

# Filtro por categoria
categorias = df_vendas['categoria'].unique()
categoria_selecionada = st.sidebar.multiselect('Categoria', categorias, default=categorias)

# Filtro por subcategoria
subcategorias = df_vendas['subcategoria'].unique()
subcategoria_selecionada = st.sidebar.multiselect('Subcategoria', subcategorias, default=subcategorias)

# Aplicar filtros
df_filtrado = df_vendas[df_vendas['categoria'].isin(categoria_selecionada) & df_vendas['subcategoria'].isin(subcategoria_selecionada)]

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
        fig = px.bar(df_filtrado, x='data', y='vendas', color='categoria', title='Vendas por Data e Categoria')
    elif tipo == 'Linha':
        fig = px.line(df_filtrado, x='data', y='vendas', color='categoria', title='Vendas por Data e Categoria')
    elif tipo == 'Dispersão':
        fig = px.scatter(df_filtrado, x='vendas', y='quantidade', color='categoria', title='Dispersão de Vendas e Quantidade')
    elif tipo == 'Histograma':
        fig = px.histogram(df_filtrado, x='vendas', color='categoria', title='Histograma de Vendas')
    st.plotly_chart(fig)

# Criar o gráfico selecionado
criar_grafico(tipo_grafico)

# Adicionar gráficos adicionais
st.header('Gráficos Adicionais')

# Gráfico de linha do tempo das vendas
st.subheader('Linha do tempo das vendas:')
fig_tempo = px.line(df_filtrado, x='data', y='vendas', title='Evolução das Vendas ao Longo do Tempo')
st.plotly_chart(fig_tempo)

# Gráfico de distribuição das vendas
st.subheader('Distribuição das Vendas:')
fig_box = px.box(df_filtrado, y='vendas', title='Distribuição das Vendas')
st.plotly_chart(fig_box)

# Heatmap de correlações
st.subheader('Mapa de Calor de Correlações:')
corr = df_filtrado.select_dtypes(include=['float64', 'int64']).corr()
fig_heatmap, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig_heatmap)

# Análise de sazonalidade: Vendas por dia da semana
st.subheader('Vendas por Dia da Semana:')
df_filtrado['dia_da_semana'] = pd.to_datetime(df_filtrado['data']).dt.day_name()
vendas_dia_semana = df_filtrado.groupby('dia_da_semana')['vendas'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
st.bar_chart(vendas_dia_semana)

# Gráfico de pizza: Participação de cada categoria nas vendas totais
st.subheader('Participação de cada Categoria nas Vendas Totais:')
fig_pizza = px.pie(df_filtrado, names='categoria', values='vendas', title='Participação de cada Categoria nas Vendas Totais')
st.plotly_chart(fig_pizza)

# Análise de crescimento: Comparar vendas em diferentes períodos
st.subheader('Análise de Crescimento:')
df_filtrado['ano'] = pd.to_datetime(df_filtrado['data']).dt.year
vendas_ano = df_filtrado.groupby('ano')['vendas'].sum()
fig_crescimento = px.bar(vendas_ano, x=vendas_ano.index, y='vendas', title='Crescimento das Vendas por Ano')
st.plotly_chart(fig_crescimento)

# Exibir as métricas
st.header('Métricas de Vendas')
st.metric('Total de Vendas', f'R$ {df_filtrado["vendas"].sum():,.2f}')
st.metric('Quantidade Total de Produtos Vendidos', int(df_filtrado['quantidade'].sum()))
