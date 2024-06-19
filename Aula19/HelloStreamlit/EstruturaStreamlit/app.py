from logging import root
import streamlit as st
import pandas as pd

st.sidebar.title("Título na Barra Lateral")
st.sidebar.markdown("Texto na barra lateral.")

st.title("Título da Aplicação")
st.header("Cabeçalho da Aplicação")
st.subheader("Subcabeçalho da Aplicação")
st.text("Texto da Aplicação")
st.markdown("Texto em negrito da Aplicação")

col1, col2 = st.columns(2)
col1.write("Este é o conteúdo da primeira coluna.")
col2.write("Este é o conteúdo da segunda coluna.")

# botões
if col1.button("Clique aqui"):
    col1.write("Botão clicado!")

# Caixa de seleção
if col2.checkbox("Marque-me"):
    col2.write("Caixa marcada!")

# Sliders
age = st.slider("Selecione sua idade", 0, 100, 20)
st.write(f"Sua idade é: {age}")

# inputs
nome = st.text_input("Digite seu nome")
st.write(f"Seu nome é: {nome}")

data = {"Coluna 1": [1, 2, 3], "Coluna 2": [4, 5, 6]}
df = pd.DataFrame(data)
st.write(df)

# Tabela
st.table(df)


col3, col4 = st.columns(2)

# inputs
campo1 = col3.number_input("Digite um numero")

campo2 = col4.number_input("Digite outro numero")

operacao = st.selectbox("Escolha a operação", ("+", "-", "*", "/", "**"))

if operacao == "+":
    resultado = campo1 + campo2
elif operacao == "-":
    resultado = campo1 - campo2
elif operacao == "*":
    resultado = campo1 * campo2
elif operacao == "/":
    if campo2 == 0:
        st.error("Não é possível dividir por 0")
    else:
        resultado = campo1 / campo2
elif operacao == "**":
    resultado = campo1 ** campo2

resultadoConta = st.write(resultado)
