#Inicialização das Funções

#Função que permite a leitura do dataset
def read_file():
    data = open('../dataset/dataset.txt', 'r',  encoding='utf-8')
    # Percorre as linhas
    for data_line in data.readlines():
        matrix.append(data_line.split(';'))
    data.close()

#Filtra a matriz dataset conforme a variavel é passada como parâmetro
def filter_age(matrix_data, age):
    matrix_age = []
    # Percorre as linhas
    for data in matrix_data:
        if(data[ano] == age):
            matrix_age.append(data)

    return matrix_age

#Elimina informações repetidas e converte em uma lista
def get_state_no_repeat(matrix_data):
    list_state_no_repeat = []
    # Percorre as linhas
    for data in matrix_data:
        list_state_no_repeat.append(data[estado])
    list_state_no_repeat = list(set(list_state_no_repeat))
    return list_state_no_repeat

#Soma do pib per capita por estado e quantidade de somas
def calc_pib_per_capita(matrix_data, list_state):
    sum_states_list = []
    # Percorre as linhas
    for state in list_state: #for1
        sum_state = 0 #Variável pib per capita
        count_state = 0 #Variável quantidade de somas
        # Percorre as linhas
        for data in matrix_data: #for2
            if data[estado] == state: #Comparativo entre estado atual do 'for1' e 'for2'
                sum_state = sum_state + float(data[pib_capita])
                count_state = count_state + 1
        sum_states_list.append( [sum_state,count_state] )

    return sum_states_list

##Imprime os dados de qualquer matriz
def print_matrix(matrix_data):
    for data in matrix_data:
        print(data)

#Função que permite criar um arquivo de saída com resultado final
def write_file(data):
    out = open('saida_q2.txt', 'a', encoding='utf-8')
    for line in data:
        out.writelines(f'Estado: {line[1]} - R$ {line[0]:.2f}\n')
    out.close()

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
matrix_filter_age = []
list_state_no_repeat = []
state_sum_per_capita = []
state_average_per_capita = []
average = 0.0

read_file() #Executa função

matrix_filter_age = filter_age(matrix, '2010')
list_state_no_repeat = get_state_no_repeat(matrix_filter_age)

sum_count_state_per_capita = calc_pib_per_capita(matrix_filter_age, list_state_no_repeat)

#Percorre duas listas de forma simultânea e acrescenta os dados na lista state_sum_per_capita
for state, values in zip(list_state_no_repeat, sum_count_state_per_capita):
    state_sum_per_capita.append([state, values])

#Percorre por cada registro da state_sum_per_capita e calcula a média do pib per capita de cada estada
for i in range(len(state_sum_per_capita)):
    sum_pib_per_capita = state_sum_per_capita[i][1][0]
    count = state_sum_per_capita[i][1][1]

    average = sum_pib_per_capita / count
    state = state_sum_per_capita[i][0]
    state_average_per_capita.append([average, state])

#Ordena os estados por média de pib per capita de forma decrescente
state_average_per_capita = sorted(state_average_per_capita, reverse=True)

write_file(state_average_per_capita)
