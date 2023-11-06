import os
import matplotlib.pyplot as plt

# Diretório onde as imagens comprimidas estão localizadas
diretorio = "./imagens"

# Lista para armazenar a porcentagem de valores singulares mantidos
porcentagens = []

# Lista para armazenar o tamanho dos arquivos em KB
tamanhos = []

# Itera sobre os arquivos no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".jpg"):
        partes_nome = arquivo.split("_")
        if len(partes_nome) == 3:
            porcentagem = float(partes_nome[2].replace(".jpg", ""))
            tamanho_kb = os.path.getsize(os.path.join(diretorio, arquivo)) / 1024
            porcentagens.append(porcentagem)
            tamanhos.append(tamanho_kb)

# Plota o gráfico
plt.plot(porcentagens, tamanhos, marker='o')
plt.xlabel("Porcentagem de Valores Singulares Mantidos")
plt.ylabel("Tamanho do Arquivo Resultante (KB)")
plt.title("Relação entre Porcentagem de Valores Singulares Mantidos e Tamanho do Arquivo")
plt.grid()
plt.show()
