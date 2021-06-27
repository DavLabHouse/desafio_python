#Inicialização das Funções

#Função que permite a leitura do dataset
def read_file():
    data = open('../dataset/dataset.txt', 'r',  encoding='utf-8')
    #Percorre as linhas
    for data_line in data.readlines():
        matrix.append(data_line.split(';'))
    data.close()

#Filtra o ano dentro da matriz conforme a variável é passada como parâmetro
def filter_age(age, matrix_data):
    matrix_age = []
    for data in matrix_data:
        if(data[ano] == age):
            matrix_age.append(data)

    return matrix_age

#Filtra o estado dentro da matriz conforme a variavel é passada como parâmetro
def filter_state(state, matrix_data):
    matrix_state = []
    for data in matrix_data:
        if (data[estado] == state):
            matrix_state.append(data)

    return matrix_state

#Soma do valor filtrado e número de colunas
def sum(matrix_filter, column):
    sum = 0
    for data in matrix_filter:
        sum = sum + float(data[column])

    return sum

#Imprime os dados de qualquer matriz
def print_matrix(matrix_data):
    for data in matrix_data:
        print(data)

#Função que permite criar um arquivo de saída com resultado final
def write_file(data, text):
    out = open('saida_q3.txt', 'w', encoding='utf-8')
    out.write(f'{text}{data*100:.2f}%')
    out.close()

#Definição de variáveis
matrix = []
matrix_filter_age = []
matrix_filter_state = []
sum_services = 0.0
sum_total = 0.0


#Nome das colunas do Dataset
ano= 0
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


read_file() #Executa função

matrix_filter_age = filter_age('2018', matrix)
matrix_filter_state = filter_state('Amazonas', matrix_filter_age)

sum_services = sum(matrix_filter_state, bruto_servicos)
sum_total = sum(matrix_filter_state, bruto_total)

number_rows_matrix = len(matrix_filter_state)

average_services = sum_services/number_rows_matrix
average_total = sum_total/number_rows_matrix

ratio_services_total = average_services/average_total

write_file(ratio_services_total, 'A proporção do valor adicionado bruto médio do setor de serviços em relação ao valor adicionado bruto total \n'
      f'médio no estado do Amazonas no ano de 2018 é de ')
