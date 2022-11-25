#Data Science Aula 06 
#Usar Anaconda Jupyter Notebook 


#O módulo matplotlib
#usada para criar representações gráficas de dados em diversos formatos e imagens.


#1. Plotando uma série de dados
import matplotlib.pyplot as plt
import numpy as np

#fig = usado para salvar o gráfico em um arquivo de imagem
#ax = usado para configurar o gráfico
fig, ax = plt.subplots()
#plota os pontos no eixo
#também podemos usar tuplas ou arrays
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()


#2. Plotando três séries de dados em um único gráfico

#retorna um conjunto de dados de distribuição linear
#com 100 valores, niciando em 0 e terminando em 2
d = np.linspace(0, 2, 100)

#cria figura e um eixo
fig, ax = plt.subplots()

#plota a primeira série de dados
ax.plot(d, d, label='linear')

#plota segunda série de dados
ax.plot(d, d ** 2, label='quadrático')

#plota terceira série de dados
ax.plot(d, d ** 3, label='cúbico')

#adiciona rótulos
ax.set_xlabel('rótulo x')
ax.set_ylabel('rótulo y')

#adiciona título
ax.set_title('Plotagem de dados')

#adiciona legenda
ax.legend()

plt.show()


#3. O mesmo exemplo anterior, porém agora no estilo pyplot
d = np.linspace(0, 2, 100)

plt.plot(d, d, label='linear')
plt.plot(d, d ** 2, label='quadrático')
plt.plot(d, d ** 3, label='cúbico')
plt.xlabel('rótulo x')
plt.ylabel('rótulo y')
plt.title('Plotagem de dados')
plt.legend()
plt.show()


#4. Criando um gráfico de pizza (no anti-horário)
labels = 'Aves', 'Peixes', 'Insetos', 'Mamíferos'
sizes = [15, 30, 45, 10] #total 100
explode = (0, 0.1, 0, 0)

fig, ax = plt.subplots()

#autopct = porcentagem de fatias
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
#assegura que o gráfico será um  círculo
#ax.axis('equal')
plt.show()


#5. Gráfico de barras com uma série de dados
#dados
langs =  'Python', 'C', 'Java', 'C++', 'C#', 'Visual Basic'
#valores gráficos
valores = [17,15,12,9,4,3]
#posições das barras
index = np.arange(len(langs))
#plota a série
plt.bar(index, valores, align='center')
#define os rótulos
plt.xticks(index, langs)
#rótulo e título
plt.ylabel('Uso')
plt.title('Ranking de linguagens - TIOBE Index')
plt.show()


#6. Gráfico de barras com duas séries de dados
import matplotlib.pyplot as plt
import numpy as np

meses = 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN'
receitas = [10000, 8000, 6000, 7400, 9000, 5000]
despesas = [5000, 3000, 4000, 2100, 6200, 1200]

index = np.arange(len(meses))
largura = 0.3

plt.bar(index - largura/2, receitas, largura, label='Receitas')
plt.bar(index + largura/2, despesas, largura, label='Receitas')

plt.xticks(index, meses)
plt.ylabel('Valores')
plt.title('Receitas e Gastos durante o ano')
plt.legend()
plt.show()

#7. Lendo e exibindo imagens com matplotlib
#imagens podem ser lidas e processadas como arrays NumPy
#array 2d para imagens monocromáticas
#array 3d para imagens coloridas
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#deve estar na mesma pasta do código
#armazena um array 3d
img = mpimg.imread('imagem.png') #ou .jpg
print(img.shape) #linhas, colunas, prof: ex (1200, 1920, 3)
#print(img)
plt.imshow(img)

