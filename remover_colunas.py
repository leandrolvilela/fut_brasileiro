import pandas as pd

# Carregar o arquivo CSV
nome_do_arquivo = "brasileirao_matches_result.csv"  # Substitua pelo nome do seu arquivo
data = pd.read_csv(nome_do_arquivo)

# Remover a primeira coluna
data_sem_primeira_coluna = data.drop("datetime", axis=1)

# Salvar o arquivo sem a primeira coluna
nome_do_novo_arquivo = "brasileirao_matches_result_scol.csv"  # Nome do novo arquivo
data_sem_primeira_coluna.to_csv(nome_do_novo_arquivo, index=False)