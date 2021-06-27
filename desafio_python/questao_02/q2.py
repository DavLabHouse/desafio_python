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

def get_state_no_repeat(matrix_data):
    list_state_no_repeat = []
    # Percorre as linhas
    for data in matrix_data:
        list_state_no_repeat.append(data[estado])
    #####################################################
    list_state_no_repeat = list(set(list_state_no_repeat))
    return list_state_no_repeat

def calc_pib_per_capita(matrix_data, list_state):
    sum_states_list = []
    # Percorre as linhas
    for state in list_state:
        sum_state = 0
        count_state = 0
###################################
        for data in matrix_data:
            if data[estado] == state:
                sum_state += float(data[pib_capita])
                count_state += 1
#####################################################
        sum_states_list.append( [sum_state,count_state] )

    return sum_states_list

def print_matrix(matrix_data):
    for data in matrix_data:
        print(data)

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


matrix_filter_age = []
list_state_no_repeat = []
state_sum_per_capita = []
state_average_per_capita = []
average = 0.0

read_file()
matrix_filter_age = filter_age(matrix, '2010')
list_state_no_repeat = get_state_no_repeat(matrix_filter_age)

sum_count_state_per_capita = calc_pib_per_capita(matrix_filter_age, list_state_no_repeat)


for state, values in zip(list_state_no_repeat, sum_count_state_per_capita):
    state_sum_per_capita.append([state, values])

for i in range(len(state_sum_per_capita)):
    average = state_sum_per_capita[i][1][0]/state_sum_per_capita[i][1][1]
    state = state_sum_per_capita[i][0]
    state_average_per_capita.append([average,state])

state_average_per_capita = sorted(state_average_per_capita, reverse=True)

write_file(state_average_per_capita)
