print('*' *50)
print(  'SEJA BEM VINDO AO SEU GERENCIADOR DE TAREFAS')
print('*' *50)

tarefas = []

while True:
    print('MENU')
    print('Digite [1] para adicionar tarefa')
    print('Digite [2] para listar tarefa')
    print('Digite [3] para remover tarefa')
    print('Digite [4] para sair do programa')
    print('*' *50)

    try:
        usu_tar = int(input('Qual tarefa deseja fazer: '))

    except ValueError:
        print('DIGITE APENAS NUMEROS')
        continue

    if usu_tar == 1:
        print('Você selecionou adicionar tarefa')
        tar_adicionada = input('Digite qual tarefa deseja adicionar: ')
        print('Tarefa adicionada com sucesso')
        tarefas.append(tar_adicionada)

    elif usu_tar == 2:
        if tarefas == []:
            print('LISTA SE ENCONTRA VAZIA')
            continue
        print('Você selecionou listar')
        for i in enumerate(tarefas, start=0):
            print(i)
    
    elif usu_tar == 3:
        if tarefas == []:
            print('LISTA SE ENCONTRA VAZIA')
            continue
        print('Você selecionou remover item da lista: ')
        for i in enumerate(tarefas, start=0):
            print(i)
        tar_removida = input('Digite qual tarefa deseja remover: ')
        if not tar_removida.isnumeric():
            print('Digite o numero ao lado da tarefa para remove-la')
            continue
        tar_removida = int(tar_removida)
        if tar_removida < 0 or tar_removida >= len(tarefas):
            print('Digitou um indice que não existe')
            print('Ao lado da tarefa tem um numero que remete a ele, digite-o de acordo com a tarefa')
            continue
        tarefas.pop(tar_removida)
    
    elif usu_tar == 4:
        print('FECHANDO O GERENCIADOR DE TAREFAS')
        break

    else:
        print('NUMEROS INVALIDOS.')
        print('*' *30)
        continue