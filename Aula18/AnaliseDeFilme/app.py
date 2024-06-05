from numpy import size
import pandas as pd
import plotly.express as pl
from flask import Flask, render_template


def analise_dados(file_path):
    df = pd.read_csv(file_path)

    resumo = df.describe()
    head = df.head()

    fig1 = pl.histogram(df, x="rating", title="Distribuição de Avaliação dos Filmes")
    fig1.write_html("Templates/plot1.html")

    fig2 = pl.box(df, x="genre", y="rating", title="Box Plot das Avaliações por Gênero")
    fig2.write_html("Templates/plot2.html")

    fig3 = pl.scatter(
        df,
        x="votes",
        y="rating",
        size="duration",
        color="genre",
        title="Relação Entre Votos, Avaliações e Duração dos Filmes",
    )
    fig3.write_html("Templates/plot3.html")

    return resumo, head


app = Flask(__name__)


@app.route("/")
def index():
    resumo, head = analise_dados("movies.csv")

    return render_template("index.html", resumo=resumo.to_html(), head=head.to_html())


@app.route("/plot1")
def plot1():
    return render_template("plot1.html")

@app.route("/plot2")
def plot2():
    return render_template("plot2.html")

@app.route("/plot3")
def plot3():
    return render_template("plot3.html")

if __name__ == "__main__":
    app.run(debug=True)
