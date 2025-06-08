
import numpy as np
import matplotlib.pyplot as plt

# Políticas públicas simuladas
politicas = {
    'Sem políticas': 1.0,
    'Política leve': 0.9,
    'Política moderada': 0.75,
    'Política agressiva': 0.5
}

anos = np.arange(2025, 2101)
emissao_inicial = 10000  # MtCO2/ano
cenario_temp = {}

for nome, fator in politicas.items():
    emissao = [emissao_inicial]
    temperatura = [1.1]  # aquecimento global inicial
    for ano in anos[1:]:
        nova_emissao = emissao[-1] * fator
        emissao.append(nova_emissao)
        temperatura.append(temperatura[-1] + 0.01 * np.log1p(nova_emissao / 10000))
    cenario_temp[nome] = temperatura

# Plotar
plt.figure(figsize=(12, 6))
for nome, temp in cenario_temp.items():
    plt.plot(anos, temp, label=nome)

plt.title("Projeção de Temperatura Global por Política Climática")
plt.ylabel("Aumento de Temperatura (°C)")
plt.xlabel("Ano")
plt.legend()
plt.grid(True)
plt.show()