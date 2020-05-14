from datetime import date, time, datetime, timedelta

def dia_atual():
    #salva a data atual no arquivo para o usuário não tentar burlar.
    data_hj = datetime.now()
    data_str = data_hj.strftime('%d/%m/%Y')
    str_data = str(data_str)
    arquivo = open('Arquivo', 'w')
    data_arq = str_data
    arquivo.write(data_arq)
    #print(data_arq)
    arquivo.close()


print('''
Esse progrma analisa a sua qualidade de sono.
Durante 7 dias, abra esse aplicativo e coloque o horário que você se deitou para dormir, e o horário que acordou.
Será feito uma análise dos dias e horário, e será retornado a sua qualidade de sono durante os 7 dias.''')

while True:
    opcao = int(input('''
    [1] Adicionar horario.
    [2] Verificar informações cadastradas.
    [3] Sair'''))

    if opcao == 1:
        dia_atual()
        dormir = str(input('Que horas você se deitou para dormir ontem: '))
        acordar = str(input('Que horas você acordou hoje: '))
        d1 = datetime.strptime(dormir, '%H:%M')
        d2 = datetime.strptime(acordar, '%H:%M')


    elif opcao == 2:
        solicitacao = open('Arquivo', 'r')
        #str(solicitacao)
        print(solicitacao)

    elif opcao == 3:
        break