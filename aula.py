from matplotlib import pyplot as plt
from collections import Counter

## gráfico de linha
def grafico_linha ():
  years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
  gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
  plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
  plt.title("GDP Nominal")
  plt.ylabel("Bilhões de $")
  plt.show()

## gráfico de barra
def grafico_barra():
  movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
  num_oscars = [5, 11, 3, 8, 10]
  xs = [i for i, _ in enumerate(movies)]
  plt.bar(xs, num_oscars)
  plt.ylabel ("# de Premiações")
  plt.xlabel("Filmes favoritos")
  plt.xticks([i for i, _ in enumerate(movies)], movies)
  plt.show()

def grafico_histograma():
  grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
  #lambda é uma função sem corpo
  decil = lambda grade: grade // 10 * 10
  decis = [decil (grade) for grade in grades]
  histograma = Counter (decis)
  plt.bar(
    [
      x for x in histograma.keys()
    ],
    histograma.values(),
    8
  )
  plt.axis([-5, 105, 0, 5])
  plt.xticks([10 * i for i in range (11)])
  plt.xlabel("Decil")
  plt.ylabel("# de Alunos")
  plt.title("Distribuição das notas do teste 1")
  plt.show()

##ERRO
def mencoes_data_science_sem_valor_zero():
  mencoes = [500, 505]
  anos = [2013, 2014]
  plt.bar(anos, mencoes, 0.4)
  plt.xticks(anos)
  plt.yticks("# de vezes que ouvimos alguem falar de data science ")
  plt.axis([2012.5, 2014.5, 499, 506])
  plt.title("Olhe a grade de aumento")
  plt.show()

def mencoes_data_science_com_valor_zero():
  mencoes = [500, 505]
  anos = [2013, 2014]
  plt.bar(anos, mencoes, 0.4)
  plt.xticks(anos)
  plt.yticks("# de vezes que ouvimos alguem falar de data science ")
  plt.axis([2012.5, 2014.5, 0, 506])
  plt.title("Veja a diferenca")
  plt.show()
### 

def grafico_dispersao():
  amigos = [70, 65, 72, 63, 71, 64, 60, 64, 67]
  minutos = [175, 170, 205, 120, 220, 130, 105, 145, 190]
  rotulos = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
  plt.scatter(amigos, minutos)
  for rotulo, num_amigos, total_minutos in zip (rotulos, amigos, minutos):
    plt.annotate(
      rotulo,
      xy = (num_amigos, total_minutos),
      xytext = (5, -5),
      textcoords = 'offset points'
    )
  plt.title("Minutos diários Vs Números de amigos")
  plt.xlabel("# amigos")
  plt.ylabel("Média de minutos diára passados na rede")
  plt.show()

###### ATIVIDADE ##########

def grafico_de_linha_amigos_por_usuarios():
  usuarios = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i']
  amigos = [15, 150, 23, 548, 54, 78, 98, 40, 68]
  plt.plot (usuarios, amigos, marker='o', linestyle='solid')
  plt.title ("amigos por usuário")
  plt.ylabel ("Amigos")
  plt.xlabel ("Usuarios")
  plt.show()

def grafico_dispersao_salário_e_tempo_de_experiência():
  salarios = [1500, 8000, 950, 3540, 5500, 2500, 1900]
  tempo_de_experiencia = [1, 5, 0, 3, 4, 3, 2]
  rotulos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  plt.scatter(tempo_de_experiencia, salarios)
  for rotulo, ano_exp, salario in zip (rotulos, tempo_de_experiencia, salarios):
    plt.annotate(
      rotulo,
      xy = (ano_exp, salario),
      xytext= (5, -5),
      textcoords = 'offset points'
    )
  plt.title ("Salário e tempo de experiência")
  plt.xlabel ("Anos de experiência")
  plt.ylabel ("Salário em R$")
  plt.show()


""""
3 Construa um histograma envolvendo dados de pagantes e não pagantes.
"""
def pagante_e_não_pagante():
  tipos = ["pagante", "não pagante", "pagante", "pagante", "não pagante", "pagante", "não pagante", "pagante"]
  conta = [0, 0]
  nome_x = ["pagante", "nao pagante"]
  for i in tipos:
    if( i == "pagante"):
      conta[0] = conta[0] + 1
    else:
      conta[1] = conta[1] + 1
  xs = [i for i, _ in enumerate(nome_x)]
  plt.bar(xs, conta)
  plt.xticks([i for i, _ in enumerate(nome_x)], nome_x)
  plt.ylabel("# de pessoas")
  plt.title("Dados de pagante e não pagante")
  plt.show()

"""
4  Construa um histograma de palavras em interesses. Por exemplo, 
a palavra learning pode aparecer em machine learning e em deep learning. 
Quebre cada interesse em palavras para fazera contagem e montar o histograma.
"""
def palavras_de_interesse():
  palavras_de_interesse = ["learning", "Java"]
  contagem = []
  interesses = [["machine learning"], ["deep learning"]]

  for i, frase in enumerate(interesses):
    interesses[i] = frase[0].split()
  cont = 0
  for i in interesses:
    for j in i:
      if j in palavras_de_interesse:
        cont = cont + 1
    contagem.insert(0, cont)
  xs = [i for i, _ in enumerate(palavras_de_interesse)]
  plt.bar(xs, contagem)
  plt.xticks([i for i, _ in enumerate(palavras_de_interesse)], palavras_de_interesse)
  plt.ylabel("# de vezes que aparece")
  plt.title("Palavras de interesse")
  plt.show()

    

def main ():
  #grafico_linha()
  #grafico_barra()
  #grafico_histograma()
  #mencoes_data_science_sem_valor_zero()
  #grafico_dispersao()
  #grafico_histograma()
  #pagante_e_não_pagante()
  palavras_de_interesse()
  #grafico_de_linha_amigos_por_usuarios()
  #grafico_dispersao_salário_e_tempo_de_experiência()


main()


