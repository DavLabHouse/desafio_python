#Definição das funções

#Função que possibilita a leitura do Dataset e a criação de uma matriz com os dados lidos
def read_file():
    data = open('../dataset/dataset.txt', 'r', encoding='utf-8')
    #Percorre as linhas
    for data_line in data.readlines():
        matrix.append(data_line.split(';'))
    data.close()

#Filtra a matriz dataset conforme a variavel é passada como parâmetro
def filter_city(city, matrix_data):
    matrix_city = []
    #Percorre as linhas
    for data in matrix_data:
        if (data[municipio] == city):
            matrix_city.append(data)
    return matrix_city

#Função que realiza a soma do pib per capita
def sum_pib_capita(matrix_filter):
    sum_pib_per_capita = 0
    # Percorre as linhas
    for data in matrix_filter:
        sum_pib_per_capita = sum_pib_per_capita + float(data[pib_capita])
    return sum_pib_per_capita

#Define uma média entre a soma do pib e número de linhas
def average_pib(sum_pib, number_matrix):
    return sum_pib/number_matrix

#Imprime os dados de qualquer matriz
def print_matrix(matrix_data):
    # Percorre as linhas
    for data in matrix_data:
        print(data)

#Função que permite criar um arquivo de saída com resultado final
def write_file(data, text):
    out = open('saida_q1.txt', 'w', encoding='utf-8')
    out.write(f'{text}{data:.2f}')
    out.close()

####################################################################

# Início do script
matrix = []

#Nome das colunas do Dataset
ano = 0
uf = 1
estado = 2
municipio = 3
regiao_intermediaria = 4
hierarquia_urbana = 5
bruto_pecoaria = 6
bruto_industria = 7
bruto_servicos = 8
bruto_adm = 9
bruto_total = 10
impostos = 11
pib = 12
pib_capita = 13

#Definição de Variáveis
matrix_filter_city = []
sum_pib_per_capita = 0
average_pib_per_capita = 0

read_file() #Executa função

matrix_filter_city = filter_city('Manaus', matrix)
sum_pib_per_capita = sum_pib_capita(matrix_filter_city)

number_matrix_filter_city = len(matrix_filter_city)

average_pib_per_capita = average_pib(sum_pib_per_capita, number_matrix_filter_city)

write_file(average_pib_per_capita, 'O valor médio de PIB per capita da cidade de Manaus é R$')


