def trabalho_do_mes (ganho, horas):
    return (ganho * horas) * 30 

while True:
    try:
        ganho_hora = float(input('Digite quanto é seu ganho por hora: '))
        horas_trabalhadas = float(input('Digite sua carga horaria por dia: '))   
        
        if ganho_hora < 0 or horas_trabalhadas < 0 :
            print('As horas tem que ser positivas, tente novamente')
            continue
        
        
        ganho_mensal = trabalho_do_mes(ganho_hora,horas_trabalhadas)
        print(f'Seu ganho mensal é de {ganho_mensal:.2f}')
        break

    except ValueError:
        print('Voce não digitou nada')