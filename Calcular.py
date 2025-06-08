
import pandas as pd
import matplotlib.pyplot as plt

# Emissões históricas por região (simuladas)
dados = {
    'Região': ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'],
    'Emissão_atual_MtCO2': [150, 200, 180, 300, 220],
    'Meta_reducao_%': [20, 25, 15, 30, 18]
}

df = pd.DataFrame(dados)

# Calcular meta em toneladas
df['Meta_emissao_MtCO2'] = df['Emissão_atual_MtCO2'] * (1 - df['Meta_reducao_%']/100)
df['Redução_necessária_MtCO2'] = df['Emissão_atual_MtCO2'] - df['Meta_emissao_MtCO2']

print(df)

# Gráfico comparativo
plt.figure(figsize=(10, 6))
plt.bar(df['Região'], df['Emissão_atual_MtCO2'], label='Atual')
plt.bar(df['Região'], df['Meta_emissao_MtCO2'], label='Meta')
plt.ylabel('Milhões de toneladas de CO2')
plt.title('Emissões de Carbono e Metas por Região')
plt.legend()
plt.show()