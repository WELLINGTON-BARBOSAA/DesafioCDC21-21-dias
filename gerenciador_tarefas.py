print('*' *50)
print(  'SEJA BEM VINDO AO SEU GERENCIADOR DE TAREFAS')
print('*' *50)

tarefas = []
# DesafioCDC21-21-dias

# COLOCAR UM COMENTARIO EM CADA FUNCIONALIDADE DO PROGRAMA
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

    
    if usu_tar == 4:
        print('FECHANDO O GERENCIADOR DE TAREFAS')
        break
