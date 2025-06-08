# Instalar bibliotecas
!pip install scikit-learn pandas matplotlib seaborn

# Importações
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Dados simulados
data = {
    'desmatamento_km2': np.random.uniform(100, 10000, 100),
    'emissoes_CO2_milhoes_ton': np.random.uniform(50, 1000, 100),
    'impacto_ambiental_indice': []
}

# Gerar índice de impacto com algum padrão + ruído
for i in range(100):
    d = data['desmatamento_km2'][i]
    e = data['emissoes_CO2_milhoes_ton'][i]
    impacto = 0.6*d + 0.4*e + np.random.normal(0, 500)
    data['impacto_ambiental_indice'].append(impacto)

df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()

# Treinar modelo
X = df[['desmatamento_km2', 'emissoes_CO2_milhoes_ton']]
y = df['impacto_ambiental_indice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# Prever impacto
novo = pd.DataFrame({
    'desmatamento_km2': [5000],
    'emissoes_CO2_milhoes_ton': [400]
})

prev = model.predict(novo)
print(f"Previsão de impacto ambiental: {prev[0]:.2f}")
