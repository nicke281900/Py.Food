print('PayFood\n')

print('1. Cadastrar restaurante')
print('2. Lista de restaurante')
print('3. Ativar restalrante')
print('4. Sair')

opcao_escolhida = int(input('Escolha uma opcao: '))
print(f'voce escolheu a opcao{opcao_escolhida}')

def finalizar_app():
    print('finaliszar o app')
if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurante')
elif opcao_escolhida == 3:
    print('Ativar resturante')
else:
   finaliszar_app()