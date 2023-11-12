import pandas as pd
import numpy as np
from pathlib import Path

# Lê o arquivo CSV
df = pd.read_csv('brasileirao_matches.csv')

# Cria uma cópia do DataFrame para não modificar o original
df_copy = df.copy()

# Converte as colunas de gols para inteiro
df_copy['home_goal'] = df_copy['home_goal'].fillna(-1).astype(int)
df_copy['away_goal'] = df_copy['away_goal'].fillna(-1).astype(int)

# Cria a nova coluna 'result' baseada nas condições
conditions = [
    (df_copy['home_goal'] > df_copy['away_goal']),
    (df_copy['home_goal'] < df_copy['away_goal']),
    (df_copy['home_goal'] == df_copy['away_goal'])
]

# choices = [3, 0, 1]
choices = [1, 0, 0]

result = np.select(conditions, choices, default=np.nan)
df_copy['result'] = result.astype('int') 

new_file = Path("brasileirao_matches_result.csv")
if new_file.is_file():
    # Se o arquivo existir, faça a substituição
    new_file.unlink()  # Deleta o arquivo existente

# Salva o novo DataFrame em um novo arquivo CSV
df_copy.to_csv(new_file, index=False)
