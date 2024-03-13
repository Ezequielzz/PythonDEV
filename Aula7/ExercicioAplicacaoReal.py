import pandas as pd

igm_df = pd.read_csv("Aula7/igm_modificado.csv")

print(igm_df.municipio)

# nome_do_municipio = "NomeDoMunicipio"
# municipio_procurado = igm_df.loc[igm_df['municipio'] == nome_do_municipio]
# print(municipio_procurado)