from datetime import date, time, datetime, timedelta

def dia_atual():
    data_hj = datetime.now()
    print(data_hj.strftime('%d/%m/%Y'))


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